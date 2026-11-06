#!/usr/bin/env python3
"""Recompute every hash and the release manifest; fail on any mismatch or any personal/employer identifier."""
import json,hashlib,unicodedata,re,sys,glob,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def norm(s): return re.sub(r'\s+',' ',unicodedata.normalize('NFC',s or '')).strip()
def sha(s): return hashlib.sha256(norm(s).encode()).hexdigest()
bad=0; rows=[]; ids=set()
for f in sorted(glob.glob(R+'/records/F*.json')):
    for r in json.load(open(f)):
        if r['id'] in ids: print('dup',r['id']); bad+=1
        ids.add(r['id'])
        if sha(r['source']['passage'])!=r['source']['passageSHA256']: print('passage hash',r['id']); bad+=1
        if sha(r['wording'])!=r['wordingSHA256']: print('wording hash',r['id']); bad+=1
        if r.get('binding',True) and r.get('status')!='unsourced': rows.append([r['id'],r['wordingSHA256'],r['source']['docId'],r['source']['paragraph'],r['source']['passageSHA256']])
rows.sort(); man=hashlib.sha256(json.dumps(rows,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
FORBID=re.compile(r'(ldhdz|hensiek|@gmail|@dzsos|lockheed|northrop\s*grumman|[A-Za-z]:\\Users|/Users/|chatgpt-projects)',re.I)
for f in glob.glob(R+'/**/*.*',recursive=True):
    if '/.git/' in f or f.endswith(('.png','.pdf')) or f.endswith('tools/verify.py'): continue
    t=open(f,errors='ignore').read()
    for m in FORBID.finditer(t): print('identifier',os.path.relpath(f,R),m.group(0)); bad+=1
print(f'records {len(ids)} baseline rows {len(rows)} manifest {man}')
sys.exit(1 if bad else 0)
