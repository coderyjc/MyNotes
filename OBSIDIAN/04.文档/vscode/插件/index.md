## 代码生成
```dataview
table type as 类型, recommendation as 个人评分, ootb=1 as 开箱即用
from "教程/vscode/插件/Plugin"
where type="代码生成"
sort recommendation desc
```

## 主题图标
```dataview
table type as 类型, recommendation as 个人评分, ootb=1 as 开箱即用
from "教程/vscode/插件/Plugin"
where contains(type, "主题") or contains(type, "图标")
sort recommendation desc
```

## 功能扩展
```dataview
table type as 类型, recommendation as 个人评分, ootb=1 as 开箱即用
from "教程/vscode/插件/Plugin"
where contains(type, "功能")
sort recommendation desc
```

## 语言扩展
```dataview
table type as 类型, recommendation as 个人评分, ootb=1 as 开箱即用
from "教程/vscode/插件/Plugin"
where contains(type, "语言")
sort recommendation desc
```

## 代码提示
```dataview
table type as 类型, recommendation as 个人评分, ootb=1 as 开箱即用
from "教程/vscode/插件/Plugin"
where contains(type, "可视化") or contains(type, "提示")
sort recommendation desc
```



## 所有
```dataview
list from "教程/vscode/插件/Plugin"
sort file.name desc
```

