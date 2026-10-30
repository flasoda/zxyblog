"""Check the files actually selected for this public Pages site."""
from pathlib import Path
import re, zipfile

ROOT=Path(__file__).resolve().parents[1]
count=0
for article in (ROOT/'_articles').glob('*.md'):
    text=article.read_text(encoding='utf-8')
    assert text.startswith('---\n') and '\ntitle:' in text, f'Missing title: {article.name}'
    assert '[[ATTACHMENT]]' not in text, f'Unreplaced attachment marker: {article.name}'
    paths=re.findall(r"'(/files/[^']+)'\s*\|\s*relative_url",text)
    assert len(paths)==1, f'Expected one file link in {article.name}'
    path=(ROOT/paths[0].lstrip('/')).resolve()
    assert path.is_relative_to((ROOT/'files').resolve()) and path.is_file(), f'Missing or invalid file: {paths[0]}'
    assert path.stat().st_size>0 and path.stat().st_size<=95*1024*1024
    if path.suffix in ('.docx','.pptx','.xlsx'):
        assert zipfile.is_zipfile(path), f'Not a real Office file: {path.name}'
    elif path.suffix=='.pdf':assert path.read_bytes().startswith(b'%PDF-')
    elif path.suffix=='.png':assert path.read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
    count+=1
assert (ROOT/'index.md').is_file() and (ROOT/'index2.md').is_file()
print(f'Checked {count} selected articles; original pages are present.')
