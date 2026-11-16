#!/usr/bin/env python3
"""Validate and deterministically package public goodWriter files; no network or install."""
import hashlib
import json
from pathlib import Path
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / 'plugin.json').read_text())
assert manifest['$schema'] == 'https://agent-plugins.org/schemas/1.0.0/plugin.schema.json'
assert manifest['name'] == 'good-writer'
assert re.fullmatch(r'\d+\.\d+\.\d+', manifest['version'])
assert not any((ROOT / name).exists() for name in ['mcp.json', '.mcp.json', '.app.json', 'hooks'])
catalog = json.loads((ROOT / '.agents/plugins/marketplace.json').read_text())
entry = catalog['plugins'][0]
assert entry['name'] == manifest['name'] and entry['source']['path'] == './'
skill = ROOT / 'skills/good-writer/SKILL.md'
text = skill.read_text()
assert text.startswith('---\nname: good-writer\n')
for target in re.findall(r'\]\((references/[^)]+)\)', text):
    assert (skill.parent / target).is_file(), target
cases = json.loads((skill.parent / 'evals/cases.json').read_text())
assert cases, 'Empty eval suite'
assert 'allow_implicit_invocation: true' in (skill.parent / 'agents/openai.yaml').read_text()
files = [ROOT / p for p in ['plugin.json', 'LICENSE', 'README.md', 'PLUGIN.md', '.agents/plugins/marketplace.json', 'scripts/package_plugin.py']]
files += sorted(p for p in (ROOT / 'skills').rglob('*') if p.is_file())
assert all(not p.is_symlink() and ROOT in p.resolve().parents for p in files)
out = ROOT / 'dist'
out.mkdir(exist_ok=True)
archive = out / f"{manifest['name']}-{manifest['version']}.zip"
with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
    for path in sorted(files):
        info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 1, 1, 0, 0, 0))
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o100644 << 16
        z.writestr(info, path.read_bytes())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert 'plugin.json' in z.namelist() and 'skills/good-writer/SKILL.md' in z.namelist()
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
archive.with_suffix('.zip.sha256').write_text(f'{digest}  {archive.name}\n')
print(f'PASS: {len(files)} files; references, metadata, eval JSON and archive integrity checked')
print(f'{archive}\nSHA256 {digest}')
