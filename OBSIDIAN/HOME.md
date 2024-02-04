```dataviewjs
var i = [dv.pages().length,
		 dv.pages(`"4.归档"`).length,
		 dv.pages(`"5.专题研究"`).length,
		 dv.pages(`"4.归档/学习/读书/微信读书同步"`).length,
		 dv.pages().file.etags.distinct().length,
		 dv.pages().file.tasks.length]
var diary = dv.pages(`"2.等待处理/Diary"`).length
dv.paragraph(`总共有 **${i[0]}** 篇文档，共计 **780,585** 字，图片 **1405** 张`)
dv.paragraph(`==已归档笔记== **${i[1]}** 篇
			 ==正在进行的笔记== **${i[2]}** 篇
			 ==读书笔记== **${i[3]}** 篇
			 ==日记== **${diary}**篇`)
dv.paragraph(`==已完成任务== **${i[5]}** 个
			 ==标签==  **${i[4]}** 个`)
```

| 文件类型 | 数量 | 大小 |
|----------|-------|------|
| png | 1438 | 177.01 MB |
| js | 47 | 77.65 MB |
| ttf | 4 | 48.20 MB |
| mp4 | 9 | 27.81 MB |
| gif | 5 | 16.59 MB |
| css | 80 | 5.77 MB |
| pdf | 1 | 5.65 MB |
| md | 974 | 3.12 MB |
| scss | 82 | 2.24 MB |
| xmind | 4 | 0.43 MB |
| json | 94 | 0.24 MB |
| ts | 9 | 0.06 MB |
| map | 2 | 0.05 MB |
| drawio | 2 | 0.04 MB |
| license | 2 | 0.03 MB |
| jpg | 2 | 0.03 MB |
| xlsx | 2 | 0.02 MB |
| webp | 1 | 0.02 MB |
| jpeg | 1 | 0.02 MB |
| mdenc | 1 | 0.01 MB |
| workspace | 1 | 0.00 MB |
| gitignore | 2 | 0.00 MB |
| yml | 2 | 0.00 MB |
| bkp | 1 | 0.00 MB |

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


```dataview
task 
from "2.等待处理"
where !completed
```

