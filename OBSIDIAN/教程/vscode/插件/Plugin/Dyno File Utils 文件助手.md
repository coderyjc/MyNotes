---
type: 项目管理
name: Dyno File Utils 文件助手
ootb: 1
recommendation: 8
create_date: 2022-01-26
---

![[Pasted image 20220126201706.png]]

# Dyno File Utils 文件助手

https://marketplace.visualstudio.com/items?itemName=dyno-nguyen.vscode-dynofileutils

## 特点

- 创建/删除一个或者多个文件/文件夹
- 创建级联的一个/多个文件/文件夹
- 重命名、duplicate
- 用模板创建项目


## 使用

命令行打开 输入 FileUtil 然后可以输入命令进行使用

### 创建多个文件/文件夹

```
input.html, style.css, script.js, public/styles/scss/index.scss, public/lib/js/, public/lib/css/
```

生成以下文件

```bash
/demo
├── public
│   ├── lib
│   ├── styles
|   |---|-- scss
|   |-------|-- index.scss
│   └── js
│   └── css
├── index.cpp
├── index.scss
└── index.ts
```

### 大括号扩展

> 大括号扩展是一种可以生成任意字符串的机制。

示例文件名输入 (separator = "," & expandSeparator = "|")

```
tmp/a/{index|script|style-1|style-2}{js|css}
```

```
/tmp
├── a
│   ├── index.js
│   ├── script.js
│   └── style-1.css
│   └── style-2.css
```

### 重命名和删除

直接FileUtil 输入到命令行

### 创建模板

提前在配置文件中写好命令，然后直接FileUtil，选择template

## 配置

-   `dynoFileUtils.confirmDelete - boolean`：控制文件工具在删除文件时是否应要求确认。
-   `dynoFileUtils.folderExclude - [String]`：配置 glob 以在搜索时排除文件夹。
-   `dynoFileUtils.separator - string`: 创建多个文件/文件夹时的分隔符。
-   `dynoFileUtils.expandSeparator - string`: 使用大括号扩展创建多个文件/文件夹时的分隔符。`Note`它必须不同于`separator`.
-   `dynoFileUtils.openFile - boolean`: 完成后应该打开文件。
-   `dynoFileUtils.templates [Object]`: 2种方式快速创建文件夹模板
    -   folderPath (isPattern: false)：在此处复制您的模板文件夹路径。
    -   pattern (isPattern: true): 创建模板的模式。

以下是示例
![[Pasted image 20220126204526.png]]