---
type: 代码可视化
name: SCSS Formatter 格式化
ootb: 1
recommendation: 7
create_date: 2022-01-27
---

![[assets/Pasted image 20220127110905.png]]

# SCSS Formatter 格式化

https://marketplace.visualstudio.com/items?itemName=sibiraj-s.vscode-scss-formatter

## 特点

可以通过命令行中的 `Format Document` 命令进行格式化

格式化文档命令的默认键盘快捷键：

-   MacOS：⇧⌥F或Shift+Option+F
-   Linux：Ctrl+Shift+I
-   Windows：Shift+Alt+F

## 配置

-   `scssFormatter.printWidth`：格式化程序将换行的行长。
-   `scssFormatter.singleQuote`: 使用单引号而不是双引号。
-   `scssFormatter.trailingComma`: 多行时尽可能打印尾随逗号。

注意

-   `formatOnPaste`不支持，因为[Prettier](https://github.com/prettier/prettier)不支持为 css/scss 格式化选择或文本范围。