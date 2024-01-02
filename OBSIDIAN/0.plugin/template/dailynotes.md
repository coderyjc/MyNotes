---
creation date: <% tp.file.creation_date() %>
tags: DailyNote
cssclass: noyaml
week: <% tp.date.now("YYYY-WW") %>
---

# <% tp.file.title %>

<< [[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "YYYY-MM-DD") %>]] | [[<% tp.date.now("YYYY-MM-DD", 1, tp.file.title, "YYYY-MM-DD") %>]]>>

