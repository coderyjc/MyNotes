---
type: 文档
name: CSS Peek css 查看
ootb: 1
recommendation: 8
create_date: 2022-01-26
---

![[Pasted image 20220126195513.png]]

# CSS Peek css查看

https://marketplace.visualstudio.com/items?itemName=pranaygp.vscode-css-peek

## 特点

支持HTML中的CSS代码“跳转到定义”和“跳转到符号”

支持HTML - CSS/SCSS/LESS 的跳转

扩展支持符号定义跟踪的所有正常功能，适用于 css 选择器（类、ID 和 HTML 标记）。这包括：

-   Peek：内联加载 css 文件并在此处进行快速编辑。( `Ctrl+Shift+F12`)
-   转到：直接跳转到 css 文件或在新编辑器中打开它 ( `F12`)
-   悬停：悬停在符号 ( `Ctrl+hover`)上显示定义

此外，它还支持符号提供程序，因此如果已经知道类或 ID 名称，则可以快速跳转到正确的 CSS/SCSS/LESS 代码


## 配置

-   `cssPeek.supportTags`- 除了类名和 ID 之外，还可以从 HTML 标记中peek。React 组件被忽略了，但在使用 Angular 时禁用此功能是个好主意
-   `cssPeek.peekFromLanguages` - 使用扩展的 vscode 语言名称列表
-   `cssPeek.peekToExclude`- 过滤掉不查找的样式文件的文件 glob 列表。默认情况下，`node_modules` 和 `bower_components` 是被忽略的