"""Stage one selected article and its real attachment for Pages publication."""
from pathlib import Path
import argparse, json, re, shutil

ROOT=Path(__file__).resolve().parents[1]
ALLOWED={'.pdf','.docx','.pptx','.xlsx','.txt','.png'}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--slug',required=True)
    parser.add_argument('--article',type=Path,required=True)
    parser.add_argument('--attachment',type=Path,required=True)
    parser.add_argument('--label',default='阿斯哈图石林资料摘录')
    args=parser.parse_args()
    if not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*',args.slug):raise SystemExit('Use a lowercase slug separated by hyphens.')
    article=args.article.resolve();attachment=args.attachment.resolve()
    if not article.is_file() or not attachment.is_file():raise SystemExit('Article or attachment is missing.')
    if attachment.suffix.lower() not in ALLOWED:raise SystemExit('Unsupported attachment extension.')
    if attachment.stat().st_size>95*1024*1024:raise SystemExit('Attachment exceeds this repository\'s 95 MiB limit.')
    body=article.read_text(encoding='utf-8-sig').strip()
    if body.startswith('---'):raise SystemExit('Pass a body-only Markdown file, without internal front matter.')
    first=body.splitlines()[0]
    if not first.startswith('# '):raise SystemExit('Start the article with a level-one title.')
    if body.count('[[ATTACHMENT]]')>1:raise SystemExit('Only one attachment marker is allowed.')
    target_article=ROOT/'_articles'/(args.slug+'.md')
    target_dir=ROOT/'files'/args.slug
    target_attachment=target_dir/('asihatu-notes'+attachment.suffix.lower())
    if target_article.exists() or target_attachment.exists():raise SystemExit('Destination already exists; review it before replacing.')
    path='/files/'+args.slug+'/'+target_attachment.name
    link='['+args.label+"]({{ '"+path+"' | relative_url }})"
    body=body.replace('[[ATTACHMENT]]',link) if '[[ATTACHMENT]]' in body else body+'\n\n'+link
    content='---\ntitle: '+json.dumps(first[2:].strip(),ensure_ascii=False)+'\n---\n'+body+'\n'
    target_dir.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(attachment,target_attachment)
    target_article.write_text(content,encoding='utf-8')
    print('Prepared: '+str(target_article.relative_to(ROOT)))
    print('Article: https://flasoda.github.io/zxyblog/articles/'+args.slug+'/')
    print('File: https://flasoda.github.io/zxyblog'+path)

if __name__=='__main__':main()
