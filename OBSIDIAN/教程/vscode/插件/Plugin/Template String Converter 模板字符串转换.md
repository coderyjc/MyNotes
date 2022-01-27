---
type: 
name: Template String Converter 模板字符串转换
ootb: 1
recommendation: 7
create_date: 2022-01-27
---


![[Pasted image 20220127115803.png]]

# Template String Converter 模板字符串转换

https://marketplace.visualstudio.com/items?itemName=meganrogge.template-string-converter

## 特点

当在js或者ts中打出了`${` 的时候， 自动将字符串转换为模板字符串

## 配置项

`template-string-converter.enable` 扩展的开和关

`template-string-converter.validLanguages` 应用的语言

`template-string-converter.quoteType` single (`''`), double (`""`), or both

`template-string-converter.convertOutermostQuotes` 在嵌套引号的情况下，将最外面的引号转换为反引号

`template-string-converter.autoRemoveTemplateString` 当`$`或者`{`被删除时，用引号替换反引号键入美元符号并打开大括号会将引号转换为反引号。 删除 $ 符号会导致反引号替换为引号

`template-string-converter.convertWithinTemplateString` 在模板字符串中，在`${`键入时将字符串转换为模板字符串

`template-string-converter.addBracketsToProps` 为 JSX 属性的模板字符串添加括号 键入一个美元符号然后打开花括号并将 addBracketsToProps 设置为 true 将引号转换为反引号并在属性周围添加括号
