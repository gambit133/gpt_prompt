# -*- coding: utf-8 -*-
"""Split a sticker sheet using hand-set boxes when stickers sit too close for auto splitting.
Each connected shape goes to the box holding its centre, so touching neighbours are not cut.
usage: python tools/split_boxes.py sheet.png out_dir "x0,y0,x1,y1;x0,y0,x1,y1;..."
"""
import os, sys
import numpy as np
from PIL import Image
from scipy import ndimage as nd

sheet, out, spec = sys.argv[1:4]
boxes = [tuple(int(v) for v in b.split(',')) for b in spec.split(';') if b.strip()]
A = np.array(Image.open(sheet).convert('RGBA'))
lab, n = nd.label(nd.binary_dilation(A[:, :, 3] > 20, iterations=1))
own = np.full(n + 1, -1)
for i, (cy, cx) in enumerate(nd.center_of_mass(np.ones_like(lab), lab, range(1, n + 1))):
    for k, (x0, y0, x1, y1) in enumerate(boxes):
        if x0 <= cx < x1 and y0 <= cy < y1:
            own[i + 1] = k; break
os.makedirs(out, exist_ok=True)
for f in os.listdir(out):
    if f.endswith('.png'): os.remove(os.path.join(out, f))
for k in range(len(boxes)):
    m = np.isin(lab, np.where(own == k)[0]) & (A[:, :, 3] > 8)
    ys, xs = np.where(m)
    assert len(ys), f'box {k + 1} is empty'
    y0, y1, x0, x1 = ys.min(), ys.max() + 1, xs.min(), xs.max() + 1
    s = A[y0:y1, x0:x1].copy(); s[~m[y0:y1, x0:x1]] = 0
    o = Image.fromarray(s); o.thumbnail((400, 400))
    o.quantize(256, Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(os.path.join(out, f'{k + 1:02d}.png'), optimize=True)
print(out, len(boxes), 'files')
