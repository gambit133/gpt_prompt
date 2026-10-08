# -*- coding: utf-8 -*-
"""Split a sticker sheet using hand-set boxes when stickers sit too close for auto splitting.
Each connected shape goes to the box holding its centre, so touching neighbours are not cut.
usage: python tools/split_boxes.py sheet.png out_dir "x0,y0,x1,y1;x0,y0,x1,y1;..."
       python tools/split_boxes.py sheet.png out_dir grid:4x3   (even cells, row by row)
"""
import os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as nd

sheet, out, spec = sys.argv[1:4]
A = np.array(Image.open(sheet).convert('RGBA'))
if spec.startswith('grid:'):
    C, R = (int(v) for v in spec[5:].split('x')); H, W = A.shape[:2]
    boxes = [(c * W // C, r * H // R, (c + 1) * W // C, (r + 1) * H // R) for r in range(R) for c in range(C)]
else:
    boxes = [tuple(int(v) for v in b.split(',')) for b in spec.split(';') if b.strip()]
lab, n = nd.label(nd.binary_dilation(A[:, :, 3] > 20, iterations=1))
own = np.full(n + 1, -1)
for i, (cy, cx) in enumerate(nd.center_of_mass(np.ones_like(lab), lab, range(1, n + 1))):
    for k, (x0, y0, x1, y1) in enumerate(boxes):
        if x0 <= cx < x1 and y0 <= cy < y1:
            own[i + 1] = k; break
# a shape far larger than its box means touching neighbours merged: split it by pixel position
pix = np.full(lab.shape, -1, np.int32); pix_lab = own[lab]; pix[:] = pix_lab
for i, s in enumerate(nd.find_objects(lab)):
    k = own[i + 1]
    if k < 0 or s is None: continue
    x0, y0, x1, y1 = boxes[k]; bw, bh = x1 - x0, y1 - y0
    if (s[1].stop - s[1].start) > bw * 1.15 or (s[0].stop - s[0].start) > bh * 1.15:
        ys, xs = np.where(lab[s] == i + 1); ys += s[0].start; xs += s[1].start
        for kk, (a0, b0, a1, b1) in enumerate(boxes):
            sel = (xs >= a0) & (xs < a1) & (ys >= b0) & (ys < b1); pix[ys[sel], xs[sel]] = kk
os.makedirs(out, exist_ok=True)
for f in os.listdir(out):
    if f.endswith('.png'): os.remove(os.path.join(out, f))
for k in range(len(boxes)):
    m = (pix == k) & (A[:, :, 3] > 8)
    # drop small slivers that touch the box edge (bits of a neighbour), keep inner sparkles
    bx0, by0, bx1, by1 = boxes[k]; ml, mn = nd.label(m); tot = m.sum()
    for j, s in enumerate(nd.find_objects(ml)):
        area = (ml[s] == j + 1).sum()
        edge = s[1].start <= bx0 + 3 or s[1].stop >= bx1 - 3 or s[0].start <= by0 + 3 or s[0].stop >= by1 - 3
        thin = (s[0].stop - s[0].start) < (by1 - by0) * .1 or (s[1].stop - s[1].start) < (bx1 - bx0) * .1
        if edge and (area < tot * .04 or (thin and area < tot * .15)): m[s][ml[s] == j + 1] = False
    ys, xs = np.where(m)
    assert len(ys), f'box {k + 1} is empty'
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    s = A[y0:y1, x0:x1].copy(); s[~m[y0:y1, x0:x1]] = 0
    o = Image.fromarray(s); o.thumbnail((400, 400))
    o.quantize(256, Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(os.path.join(out, f'{k + 1:02d}.png'), optimize=True)
print(out, len(boxes), 'files')
