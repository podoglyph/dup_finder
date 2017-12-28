import os, hashlib, pprint

hashmap = {}

for path, dirs, files in os.walk('./files'):
    for filename in files:
        fullname = os.path.join(path, filename)
        with open(fullname, 'rb') as f:
            d = f.read()
        h = hashlib.md5(d).hexdigest()
        filelist = hashmap.setdefault(h, [])
        filelist.append(fullname)

pprint.pprint(hashmap)