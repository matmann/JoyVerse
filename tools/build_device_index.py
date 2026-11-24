#!/usr/bin/env python3
"""Rebuild the device index and the .js copies of each device file.

devices/<id>.json are the device files (made with the device designer) – the only ones to edit.
The mapper opened from disk can load .js files but not .json, so this writes a .js copy of each
into devices/built/, plus devices/built/index.js listing them for the Add device dropdown.
It also refreshes the devices inside JoyVerse-offline.html (the one-file copy), so that stays current too.
GitHub runs it after every push that changes a device file. Run from the repository root.
"""
import json, os, glob, hashlib

D = 'devices'
B = os.path.join(D, 'built')
os.makedirs(B, exist_ok=True)
index = []
for path in sorted(glob.glob(os.path.join(D, '*.json'))):
    name = os.path.basename(path)
    if name == 'index.json':
        continue
    with open(path, 'rb') as f:
        raw = f.read()
    dev = json.loads(raw.decode('utf-8'))
    if not isinstance(dev, dict) or 'controls' not in dev:
        continue
    did = dev.get('id') or name[:-5]
    did = name[:-5]   # the file name is the id the mapper uses
    index.append({'id': did, 'name': dev.get('name', did), 'maker': dev.get('maker', ''), 'model': dev.get('model', ''),
                  'short': dev.get('short', ''), 'head': dev.get('head', ''), 'side': dev.get('side', ''),
                  'saved': dev.get('saved', ''), 'v': hashlib.sha1(raw).hexdigest()[:12]})   # v: changes with the file, so copies can tell they're out of date
    js = '(window.VPCM_DEVICES=window.VPCM_DEVICES||{})[' + json.dumps(did) + ']=' + json.dumps(dev, separators=(',', ':')) + ';\n'
    with open(os.path.join(B, did + '.js'), 'w', encoding='utf-8') as f:
        f.write(js)
index.sort(key=lambda d: (d['maker'], d['name']))
with open(os.path.join(B, 'index.json'), 'w', encoding='utf-8') as f:
    json.dump({'format': 1, 'devices': index}, f, indent=1)
with open(os.path.join(B, 'index.js'), 'w', encoding='utf-8') as f:
    f.write('window.VPCM_DEVICE_INDEX=' + json.dumps(index, indent=1) + ';\n')
# copies of devices whose .json was removed
keep = {d['id'] for d in index} | {'index'}
for js in glob.glob(os.path.join(B, '*.js')):
    if os.path.basename(js)[:-3] not in keep:
        os.remove(js)
print(len(index), 'devices:', ', '.join(d['id'] for d in index))

# the one-file copy carries the devices inside it: swap in the current ones
SHARE = 'JoyVerse-offline.html'
if os.path.exists(SHARE):
    with open(SHARE, encoding='utf-8') as f:
        page = f.read()
    tag = '<script id="vpcm-devices">\n'
    i = page.find(tag)
    if i < 0:
        print(SHARE, 'has no device block – rebuild it with the mapper build once')
    else:
        j = page.find('\n</script>', i + len(tag))
        parts = [open(os.path.join(B, 'index.js'), encoding='utf-8').read()]
        parts += [open(os.path.join(B, d['id'] + '.js'), encoding='utf-8').read() for d in sorted(index, key=lambda d: d['id'])]
        bundle = '\n'.join(parts).replace('</', '<\\/')
        page = page[:i + len(tag)] + bundle + page[j:]
        with open(SHARE, 'w', encoding='utf-8') as f:
            f.write(page)
        print(SHARE, 'devices refreshed')
