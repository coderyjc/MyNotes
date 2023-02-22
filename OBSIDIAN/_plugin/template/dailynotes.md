---
creation date: <% tp.file.creation_date() %>
modification date: <%+ tp.file.last_modified_date("dddd Do MMMM YYYY HH:mm:ss") %>
tags: DailyNote
banner: "_plugin/banners/daily-note-banner.gif"
banner_y: 0.5536
banner_x: 0.50168
cssclass: noyaml
banner_icon: 💌
week: <% tp.date.now("YYYY-WW") %>
---

# <% tp.file.title %>

<< [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>]] | [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>]]>>



- [ ] 




上午：
- C + DS
- LeetCode

下午：
- OS
- CN
- CO
- DB
- 软件工程

晚上：
- 毕设