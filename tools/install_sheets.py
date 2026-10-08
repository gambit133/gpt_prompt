# -*- coding: utf-8 -*-
"""Split generated sticker sheets into assets/stickers/<pack>/NN.png.
usage: python tools/install_sheets.py <sheet_dir> key[:expect][:grid] ...
  key ending in 2 (e.g. capy2) appends to the existing pack 'capy' as 13.png, 14.png ...
"""
import os, sys, shutil, subprocess, tempfile
from PIL import Image
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src_dir = sys.argv[1]
for spec in sys.argv[2:]:
    key, expect, *grid = spec.split(':') + ['12']
    grid = [g for g in grid if 'x' in g]
    sheet = os.path.join(src_dir, key + '.png')
    if not os.path.exists(sheet): print('skip', key); continue
    tmp = tempfile.mkdtemp()
    args = [sys.executable, os.path.join(ROOT, 'tools', 'split_stickers.py'), sheet, tmp]
    args += ['--grid', grid[0]] if grid else ['--expect', expect]
    subprocess.run(args, check=True)
    files = sorted(f for f in os.listdir(tmp) if f.endswith('.png'))
    pack = key[:-1] if key.endswith('2') else key
    dst = os.path.join(ROOT, 'assets', 'stickers', pack); os.makedirs(dst, exist_ok=True)
    start = len([f for f in os.listdir(dst) if f.endswith('.png')]) + 1 if key.endswith('2') else 1
    for i, f in enumerate(files):
        im = Image.open(os.path.join(tmp, f)).convert('RGBA'); im.thumbnail((400, 400))
        im.quantize(256, Image.Quantize.FASTOCTREE, dither=Image.Dither.NONE).save(os.path.join(dst, f'{start + i:02d}.png'), optimize=True)
    shutil.rmtree(tmp)
    print(key, '->', pack, len(files), 'files from', start)
