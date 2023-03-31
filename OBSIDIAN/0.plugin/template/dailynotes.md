---
creation date: <% tp.file.creation_date() %>
tags: DailyNote
banner: "0.plugin/banners/daily-note-banner.gif"
banner_y: 0.5536
banner_x: 0.50168
cssclass: noyaml
banner_icon: 💌
week: <% tp.date.now("YYYY-WW") %>
---

# <% tp.file.title %>

<< [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>]] | [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>]]>>


> [!info]+ 一句话描述你要做、在做、准备做的事情
> 


- [ ] 毕设
