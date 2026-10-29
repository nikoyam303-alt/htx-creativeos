#!/usr/bin/env python3
"""Search HTX L3 daylight assets; download a selected asset with SHA-256 verification."""
import argparse
import hashlib
import json
from pathlib import Path
import urllib.request

BASE = 'https://raw.githubusercontent.com/nikoyam303-alt/htx-creativeos/main/'
MANIFEST = BASE + 'assets/illustrations/l3-standard-light/manifest.json'

def read_url(url):
    request = urllib.request.Request(url, headers={'User-Agent': 'htx-brand-skill/1.0'})
    with urllib.request.urlopen(request, timeout=60) as response:
        return response.read()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--query', help='Chinese or English topic keywords')
    parser.add_argument('--id', help='Exact asset ID from the manifest')
    parser.add_argument('--output', type=Path, help='Destination PNG; requires --id')
    parser.add_argument('--manifest', type=Path, help='Optional local manifest for offline search')
    parser.add_argument('--limit', type=int, default=8)
    args = parser.parse_args()
    if args.output and not args.id:
        parser.error('--output requires --id')
    manifest = json.loads(args.manifest.read_text() if args.manifest else read_url(MANIFEST))
    assets = manifest['assets']
    if args.id:
        selected = next((a for a in assets if a['id'] == args.id), None)
        if selected is None:
            parser.error('Unknown asset ID: ' + args.id)
        if args.output:
            if args.output.exists():
                if hashlib.sha256(args.output.read_bytes()).hexdigest() != selected['sha256']:
                    parser.error('Destination exists with different content; choose another path')
            else:
                data = read_url(BASE + selected['path'])
                if hashlib.sha256(data).hexdigest() != selected['sha256']:
                    raise RuntimeError('Asset checksum mismatch; refresh manifest and retry')
                args.output.parent.mkdir(parents=True, exist_ok=True)
                args.output.write_bytes(data)
            selected = dict(selected, localPath=str(args.output.resolve()))
        print(json.dumps(selected, ensure_ascii=False, indent=2))
        return
    query = (args.query or '').casefold()
    def score(asset):
        labels = [asset.get('label', asset['name']), asset['description'], *asset['keywords']]
        return sum(len(term) for term in labels if term.casefold() in query and term) + sum(2 for term in query.split() if term in ' '.join(labels).casefold())
    ranked = sorted(assets, key=score, reverse=True) if query else assets
    if query:
        ranked = [a for a in ranked if score(a) > 0]
    print(json.dumps({'matches': ranked[:max(1, args.limit)], 'totalMatches': len(ranked), 'contactSheets': manifest['contactSheets']}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
