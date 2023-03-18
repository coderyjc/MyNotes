---
banner: "0.plugin/banners/rainy-day-bird.gif"
banner_y: 0.176
banner_x: 0.5759
---

```dataviewjs
var i = [dv.pages().length,
		 dv.pages(`"4.归档"`).length,
		 dv.pages(`"5.专题研究"`).length,
		 dv.pages(`"1.收集箱/wechat_notes"`).length,
		 dv.pages().file.etags.distinct().length]

dv.paragraph(`总共有 **${i[0]}** 篇文档`)
dv.paragraph(`其中==已归档笔记== **${i[1]}** 篇，==正在进行的笔记== **${i[2]}** 篇，==读书笔记== **${i[3]}** 篇，==标签==  **${i[4]}**个`)

```


```dataviewjs
let setting = {};
//在和风天气中创建的 Api key
setting.key = "dc0f31ac6f37484f88e3e7d45b84e403";
setting.city = "";//城市名 为空自动定位
setting.icon = false;//是否显示图标true false
setting.days = 3 ;//天气预报天数1-7
setting.headerLevel = 3;//添加标题的等级
setting.addDesc = true;//是否添加描述true false
setting.onlyToday = false;//是否只在当天显示
setting.anotherCity = "梁山";//添加另外一个城市
//脚本文件 weatherView.js 所在路径
dv.view("0.plugin/dataviewjs/dv_weatherView",setting)
```

````ad-flex
<div>

### 最近编辑
```dataview
table WITHOUT ID file.link AS "标题",file.mtime as "时间"
from !"模板" and !"kanban"
sort file.mtime desc
limit 5
```
</div>

<div>

### 三天内创建的笔记
```dataview
table file.ctime as 创建时间
from ""
where date(today) - file.ctime <=dur(3 days)
sort file.ctime desc
limit 5
```
</div>
````
