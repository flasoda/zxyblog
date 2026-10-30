# ZXY 札记

GitHub Pages站点：<https://flasoda.github.io/zxyblog/>

文章目录：<https://flasoda.github.io/zxyblog/journal/>

保留原有`index.md`与`index2.md`及对应访问路径。站点继续沿用`main`分支根目录的GitHub Pages发布方式，不需要额外托管服务。

## 添加文章与附件

1. 在本地准备好已经选定发布的文章Markdown与原始附件。
2. 运行`python tools/prepare_article.py --slug asihatu-01 --article 完整文章路径 --attachment 完整附件路径`。
3. 运行`python tools/check_site.py`检查文章中的附件路径与文件。
4. 检查`git diff`，提交并推送到`main`。GitHub Pages会自动更新。

正文中的`[[ATTACHMENT]]`会替换为文件链接；没有该标记时，工具在文末添加链接。每次工具只添加指定的一篇文章和一个附件，不会复制草稿目录或研究记录。

新增文章存于`_articles/`，发布到`/zxyblog/articles/文章slug/`。附件位于`files/文章slug/`，可通过同一Pages域名直接访问。

## 目录

- `_articles/`：已决定公开的文章源文件。
- `files/`：已决定公开的附件。
- `_layouts/`、`assets/`：页面布局与样式。
- `templates/`：文章模板，不进入站点输出。
- `tools/`：本地发布辅助工具，不进入站点输出。

上传附件时保留实际格式及扩展名。图片也使用普通文件链接，不会自动改成正文内嵌图片。仓库中不存放本地凭据、未公开草稿或内部判定材料。
