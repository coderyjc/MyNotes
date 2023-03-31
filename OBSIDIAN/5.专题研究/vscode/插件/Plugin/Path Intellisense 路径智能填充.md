---
type: 代码生成
name: Path Intellisense 路径智能填充
ootb: 0
recommendation: 7
create_date: 2022-01-27
---

![[assets/Pasted image 20220127104839.png]]

# Path Intellisense 路径智能填充

https://marketplace.visualstudio.com/items?itemName=christian-kohler.path-intellisense

## 特点

更强大的自动填充路径

## 安装

要使用PathIntellisense而不是vscode自带的，需要在设置中添加以下内容

```javascript
{ "typescript.suggest.paths": false }
{ "javascript.suggest.paths": false }
```

## 配置

### 导入语句中的文件扩展名

如果语句是导入语句，则 Path Intellisense 会默认删除文件扩展名。要启用文件扩展名，请将以下设置设置为 true：

```javascript
{
	"path-intellisense.extensionOnImport": true,
}
```

### 显示隐藏文件

默认情况下，不显示隐藏文件。将此设置为 true 以显示隐藏文件。

```javascript
{
	"path-intellisense.showHiddenFiles": true,
}
```

如果设置为 false，PathIntellisense 也会忽略默认的“files.exclude”：

```javascript
{
	"files.exclude": {
		"**/*.map.js": true
	}
}
```

### 导航到文件夹时自动斜线

默认情况下，自动完成不会在目录后添加斜杠。

```javascript
{
	"path-intellisense.autoSlashAfterDirectory": false,
}
```

### 自动触发下一个建议

选择建议后，将自动弹出下一个建议。

此设置将覆盖该`autoSlashAfterDirectory`设置。

```javascript
{
	"path-intellisense.autoTriggerNextSuggestion": false,
}
```

### 绝对路径

默认情况下，绝对路径在当前工作区根路径中解析。将其设置为 false 以将绝对路径解析为磁盘根路径。

```javascript
{
	"path-intellisense.absolutePathToWorkspace": true,
}
```

### 映射

定义可用于使用绝对路径或与 webpack 解析选项结合使用的自定义映射。

```javascript
{
	"path-intellisense.mappings": {
		"/": "${workspaceFolder}",
		"lib": "${workspaceFolder}/lib",
		"global": "/Users/dummy/globalLibs"
	},
}
```

当路径应该相对于当前项目的当前根目录时，使用 ${workspaceFolder}。V2.2.1 及更低版本使用 ${workspaceRoot}。较新的版本支持这两个占位符。