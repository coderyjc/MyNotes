

---
cssClasses: cards cards-align-bottom cards-2-3 table-100
banner: "_plugin/banners/book-banner.gif"
banner_x: 0.5
banner_y: undefined
banner_icon: 
---**


```dataviewjs
const groups =  dv.pages('#读书').groupBy(p => p.category?.split('-')[0])
for (let group of groups) {
	dv.header(3, group.key);
	dv.table(["Name","author", "NoteCount"],
		group.rows
			.sort(k => k.noteCount, 'desc')
			.map(k => [k.file.link,k.author, k.noteCount]))
}

```



> [!cards|banner] ## 视图看板
>```dataview
table without id ("![](" + cover + ")") as Cover,file.link as Name, author as Author,noteCount as NoteCount
from #读书
where !contains(file.folder, "_plugin") 
sort noteCount desc
>```
