---
type: 代码格式化
name: "Auto Rename 自动重命名标签"
ootb: 1
recommendation: 8
create_date: 2022-01-25
---

![[Pasted image 20220126192521.png]]

# Auto Rename Tag 自动重命名标签

https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag

## 特点

-   当您重命名一个 HTML/XML 标签时，会自动重命名配对的 HTML/XML 标签

## 配置

设置对那些语言启用，默认是`*` 也就是对所有语言适用

```json
{
  "auto-rename-tag.activationOnLanguage": ["html", "xml", "php", "javascript"]
}
```