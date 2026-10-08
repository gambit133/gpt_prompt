# -*- coding: utf-8 -*-
"""Split a transparent sticker sheet into individual trimmed PNGs.

Usage: python tools/split_stickers.py <sheet.png> <out_dir> [--min-area 2500] [--gap 18]
Pieces closer than --gap px (e.g. light-bulb rays) are merged into one sticker.
Writes NN.png per sticker (reading order) and prints a JSON list of {file, w, h, x, y}.
"""
import sys, os, json, argparse
import numpy as np
from PIL import Image
from scipy import ndimage

ap = argparse.ArgumentParser()
ap.add_argument('sheet'); ap.add_argument('out')
ap.add_argument('--min-area', type=int, default=2500)
ap.add_argument('--gap', type=int, default=18)
ap.add_argument('--max-side', type=int, default=512)
ap.add_argument('--grid', default='', help='COLSxROWS: cut by equal grid cells instead (for touching stickers)')
ap.add_argument('--expect', type=int, default=0, help='try gaps until exactly this many stickers are found')
a = ap.parse_args()

im = Image.open(a.sheet).convert('RGBA')
alpha = np.array(im.getchannel('A'))
mask = alpha > 24
def detect(gap):
    grown = ndimage.binary_dilation(mask, iterations=gap) if gap else mask   # join nearby fragments
    labels, n = ndimage.label(grown)
    boxes = []
    for i, sl in enumerate(ndimage.find_objects(labels), 1):
        if sl is None: continue
        region = (labels[sl] == i) & mask[sl]
        if region.sum() < a.min_area: continue
        ys, xs = np.where(region)
        boxes.append((sl[0].start + ys.min(), sl[1].start + xs.min(), sl[0].start + ys.max() + 1, sl[1].start + xs.max() + 1, i))
    return labels, boxes
gaps = [a.gap] if not a.expect else sorted(set([a.gap] + list(range(40, 1, -2))), key=lambda g: -g)
best = None
for g in gaps:
    labels, boxes = detect(g)
    if not a.expect or len(boxes) == a.expect: best = (labels, boxes); break
    if best is None or abs(len(boxes) - a.expect) < abs(len(best[1]) - a.expect): best = (labels, boxes)
labels, boxes = best
if a.grid:
    # assign each blob to the grid cell holding its centre; only blobs spanning several cells are cut at cell lines
    gc, gr = map(int, a.grid.lower().split('x')); H, W = mask.shape
    lab0, n0 = ndimage.label(mask)
    cell_of = lambda y, x: min(int(y * gr / H), gr - 1) * gc + min(int(x * gc / W), gc - 1)
    owner = np.full(mask.shape, -1, int)
    for i, sl in enumerate(ndimage.find_objects(lab0), 1):
        if sl is None: continue
        reg = lab0[sl] == i
        h, w = reg.shape
        if h <= H / gr * 1.1 and w <= W / gc * 1.1:          # fits in one cell: keep whole
            ys, xs = np.where(reg); owner[sl][reg] = cell_of(sl[0].start + ys.mean(), sl[1].start + xs.mean())
        else:                                                   # spans cells: cut by cell
            ys, xs = np.where(reg)
            owner[sl[0].start + ys, sl[1].start + xs] = [cell_of(y, x) for y, x in zip(sl[0].start + ys, sl[1].start + xs)]
    labels = np.zeros(mask.shape, int); boxes = []
    for c in range(gc * gr):
        m = owner == c
        if m.sum() < a.min_area: continue
        k = len(boxes) + 1; labels[m] = k
        ys, xs = np.where(m); boxes.append((ys.min(), xs.min(), ys.max() + 1, xs.max() + 1, k))

# reading order: group into rows by vertical center
boxes.sort(key=lambda b: (b[0] + b[2]) / 2)
rows, cur = [], []
for b in boxes:
    if cur and (b[0] + b[2]) / 2 - (cur[-1][0] + cur[-1][2]) / 2 > (cur[-1][2] - cur[-1][0]) * 0.5:
        rows.append(cur); cur = []
    cur.append(b)
if cur: rows.append(cur)
ordered = [b for r in rows for b in sorted(r, key=lambda b: b[1])]

os.makedirs(a.out, exist_ok=True)
out = []
arr = np.array(im)
for k, (y0, x0, y1, x1, i) in enumerate(ordered, 1):
    piece = arr[y0:y1, x0:x1].copy()
    keep = (labels[y0:y1, x0:x1] == i)
    piece[~keep] = 0                                                  # drop neighbours' pixels inside the box
    if a.grid:                                                         # drop a neighbour's sliver cut off at the top/bottom
        lab, _ = ndimage.label(piece[..., 3] > 24); h = lab.shape[0]
        for j, sl in enumerate(ndimage.find_objects(lab), 1):
            if sl is None: continue
            if (sl[0].start == 0 or sl[0].stop == h) and (sl[0].stop - sl[0].start) < h * 0.08: piece[lab == j] = 0
        ys, xs = np.where(piece[..., 3] > 0); piece = piece[ys.min():ys.max() + 1, xs.min():xs.max() + 1]
    p = Image.fromarray(piece, 'RGBA')
    pad = 6
    canvas = Image.new('RGBA', (p.width + pad * 2, p.height + pad * 2), (0, 0, 0, 0)); canvas.paste(p, (pad, pad))
    canvas.thumbnail((a.max_side, a.max_side), Image.LANCZOS)
    fn = f'{k:02d}.png'; canvas.save(os.path.join(a.out, fn), optimize=True)
    out.append({'file': fn, 'w': canvas.width, 'h': canvas.height, 'x': int(x0), 'y': int(y0), 'sw': im.width, 'sh': im.height})
print(json.dumps(out))
