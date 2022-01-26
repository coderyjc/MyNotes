---
plugin-platform: vscode
type: 代码格式化
name: "Auto Close Tag 自动关闭标签"
create_date: 2022-01-25
---


# Auto Close Tag 自动关闭标签

https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-close-tag

![[Pasted image 20220125170258.png]]

## 特点
-   键入开始标签的右括号时自动添加结束标签
-   插入结束标签后，光标在开始和结束标签之间
-   设置不自动关闭的标签列表
-   自动关闭自关闭标签
-   支持 Sublime Text 3 的自动关闭标签
-   使用键盘快捷键或命令面板手动添加关闭标签

Sublime Text 3 模式

要在键入时自动添加关闭标签`</`（与 Sublime Text 3 相同），请将以下配置设置为`true`：

```json
{
    "auto-close-tag.SublimeText3Mode": true
}
```

该设置是`false`默认设置。

## 配置

用于`auto-close-tag.enableAutoCloseTag`设置是否自动插入关闭标签（默认为`true`）：

```json
{
    "auto-close-tag.enableAutoCloseTag": true
}
```

设置是否自动关闭自关闭标签（例如键入 `<br`，然后敲 `/`，将自动添加`>`）（默认情况下`true`）：

```json
{
    "auto-close-tag.enableAutoCloseSelfClosingTag": true
}
```

是否在自闭合标签的正斜杠前插入空格（`false`默认为）：

```json
{
    "auto-close-tag.insertSpaceBeforeSelfClosingTag": false
}
```

添加条目`auto-close-tag.activationOnLanguage`以设置将激活扩展程序的语言。用`["*"]`激活所有语言。以下是默认设置：

```json
{
    "auto-close-tag.activationOnLanguage": [
        "xml",
        "php",
        "blade",
        "ejs",
        "jinja",
        "javascript",
        "javascriptreact",
        "typescript",
        "typescriptreact",
        "plaintext",
        "markdown",
        "vue",
        "liquid",
        "erb",
        "lang-cfml",
        "cfml",
        "HTML (Eex)"
    ]
}
```

注意：该设置应使用[VS Code](https://github.com/Microsoft/vscode/tree/master/extensions)中定义的语言 id 进行设置。

以[javascript 定义](https://github.com/Microsoft/vscode/blob/master/extensions/javascript/package.json)为例，我们需要使用`javascript`for`.js`和`.es6`，使用`javascriptreact`for `.jsx`。所以，如果你想在`.js`文件上启用这个扩展，你需要在 settings.json 中添加`javascript`。

或者，您也可以排除您不希望激活扩展的语言。下面是一个例子：

```json
{
    "auto-close-tag.disableOnLanguage": [
        "php",
        "python"
    ]
}
```
