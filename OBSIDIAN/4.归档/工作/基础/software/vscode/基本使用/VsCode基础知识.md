# VsCode基础知识

#VsCode #教程 #VsCode配置  

### 基本设置

#### 隐藏行号

```
设置 > 用户设置 > Line Numbers
```

#### 导航设置

```
设置 > 工作台 > 导航路径 > (Breadcrumbs: Enabled & Breadcrumbs: File Path)
```

#### 滚动缩放

```
文本编辑器 > Editor: Mouse Wheel Zoom
```


### 编码优化

#### 代码格式

代码美化主要我使用的是 [[../插件/Plugin/Prettier - Code formatter 代码格式化]] ，并需要在项目目录创建配置文件`.prettierrc`基本内容如下

```
{
  "eslintIntegration": true,
  "stylelintIntegration": true,
  "printWidth": 2000,
  "tabWidth": 2,
  "singleQuote": true,
  "semi": false
}
```

#### 代码片段

> 代码片段快捷生成： https://snippet-generator.app/

Vscode提供了`User Snippet` 用户代码片段，让用户可以自定义快捷键来输入内容。

- prefix      :这个参数是使用代码段的快捷入口,比如这里的log在使用时输入log会有智能感知.
- body        :这个是代码段的主体.需要设置的代码放在这里,字符串间换行的话使用\r\n换行符隔开.注意如果值里包含特殊字符需要进行转义.多行语句的以,隔开
- $1          :这个为光标的所在位置.
- $2          :使用这个参数后会光标的下一位置将会另起一行,按tab键可进行快速切换,还可以有$3,$4,$5.....
- description :代码段描述,在使用智能感知时的描述

```ad-note
title: 如何在代码片段中插入 $ 和｛ 符号
`\\$`
`\\{`
```


#### 代码智能提示

推荐 [[../插件/Plugin/Tabnine AI 代码智能提示]]

#### SASS/LESS 编译

推荐 [[../插件/Plugin/Live Sass Compiler SASS自动翻译]]

#### 字体

在vscode配置中搜索`Editor: Font Family` 并设置以下值。

```
'JetBrains Mono','Fira Code',Menlo,Monaco, 'Courier New', monospace
```

需要在配置中将连字打开（设置中搜索`fontLigatures`关键词）

```
"editor.fontFamily": "'Fira Code','JetBrains Mono'",
"editor.fontLigatures": true,
```


> 禁止突出显示歧义字符

![](assets/Pasted%20image%2020220904125954.png)

![](assets/Pasted%20image%2020220904130023.png)

禁止突出显示歧义字符

![](assets/Pasted%20image%2020220904130034.png)

![](assets/Pasted%20image%2020220904130048.png)

