#!/usr/bin/env python3
"""Search and fetch indexed Poloniex dark illustrations (standard library only)."""
import argparse,hashlib,json,os,tempfile,urllib.request
from pathlib import Path
INDEX=Path(__file__).resolve().parents[1]/'references/illustrations-manifest.json'
URL='https://raw.githubusercontent.com/nikoyam303-alt/htx-creativeos/main/assets/illustrations/poloniex-dark/manifest.json'
def main():
 p=argparse.ArgumentParser();p.add_argument('--query',default='');p.add_argument('--id');p.add_argument('--output',type=Path);p.add_argument('--refresh',action='store_true');a=p.parse_args()
 if a.refresh:
  with urllib.request.urlopen(URL,timeout=60) as r:data=r.read()
  m=json.loads(data)
  if m.get('theme')!='dark' or not isinstance(m.get('assets'),list):p.error('Invalid remote manifest')
  INDEX.write_bytes(data)
 m=json.loads(INDEX.read_text());q=a.query.casefold();items=[v for v in m['assets'] if (not a.id or v['id']==a.id) and q in json.dumps(v,ensure_ascii=False).casefold()]
 if a.output:
  if not a.id or len(items)!=1:p.error('--output requires one exact --id')
  if a.output.exists():p.error('Output already exists; choose a new file')
  v=items[0]
  with urllib.request.urlopen(v['downloadUrl'],timeout=60) as r:data=r.read()
  if hashlib.sha256(data).hexdigest()!=v['sha256']:p.error('SHA-256 mismatch')
  if not data.startswith(b'\x89PNG\r\n\x1a\n'):p.error('Not a PNG')
  a.output.parent.mkdir(parents=True,exist_ok=True)
  with a.output.open('xb') as f:f.write(data)
  print(str(a.output.resolve()))
 else:
  print(json.dumps([{'id':v['id'],'name':v['name'],'number':v['catalogNumber'],'figmaUrl':v['figmaUrl'],'url':v['downloadUrl']} for v in items],ensure_ascii=False,indent=2))
if __name__=='__main__':main()
