---
title: 文章
permalink: /journal/
---
# 文章

一些旅行、食物和日常见闻。

<ul class="article-list">
{% for article in site.articles reversed %}
{% unless article.listed == false %}
  <li><a href="{{ article.url | relative_url }}">{{ article.title | escape }}</a>{% if article.description %}<p>{{ article.description | escape }}</p>{% endif %}</li>
{% endunless %}
{% endfor %}
  <li><a href="{{ '/' | relative_url }}">周末试做圣诞面包，先把准备工作排好</a><p>从备料到出炉的一次家庭烘焙安排。</p></li>
  <li><a href="{{ '/index2.html' | relative_url }}">德累斯顿圣诞面包：一块面包背后的数百年德国圣诞传统</a><p>一份关于圣诞面包的旧记录。</p></li>
</ul>
