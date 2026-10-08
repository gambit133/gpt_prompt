# -*- coding: utf-8 -*-
"""Remove an opaque, dark background from a sticker sheet whose stickers have thick black outlines.
Keeps everything enclosed by a neutral-black outline; the brownish/coloured background and glow go.
usage: python tools/cut_outline_bg.py in.png out.png [--white] [x0,y0,x1,y1 ...]
  --white: stickers have a white die-cut border instead of a black outline
  optional boxes get stronger gap closing (for a sticker whose outline has a small gap)
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as nd


def cut(black, it):
    f = nd.binary_fill_holes(nd.binary_closing(black, iterations=it))
    lab, n = nd.label(f); idx = range(1, n + 1)
    size = nd.sum(f, lab, idx); blackness = nd.mean(black, lab, idx)
    # drop tiny bits and pieces that are almost all black (scraps of dark background)
    return np.isin(lab, [i + 1 for i in range(n) if size[i] >= 400 and blackness[i] < .75])


WHITE = '--white' in sys.argv
src, dst, *boxes = [a for a in sys.argv[1:] if a != '--white']
A = np.array(Image.open(src).convert('RGBA')); rgb = A[:, :, :3].astype(int)
black = ((rgb.min(2) > 238) if WHITE else (rgb.max(2) < 60)) & (rgb.max(2) - rgb.min(2) < 14)
keep = cut(black, 3)
loose = (rgb.min(2) > 200) & (rgb.max(2) - rgb.min(2) < 50) if WHITE else black  # cream borders
for b in boxes:
    x0, y0, x1, y1 = (int(v) for v in b.split(','))
    for it in (6, 8, 10, 14):
        loc = cut(loose[y0:y1, x0:x1], it)
        if loc.mean() > .45: break
    keep[y0:y1, x0:x1] |= loc
A[:, :, 3] = np.where(keep, A[:, :, 3], 0)
Image.fromarray(A).save(dst)
print(dst, 'kept', round(keep.mean(), 3))
