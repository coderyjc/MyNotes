---
type: 代码补全
name: Path Autocomplete 路径填充
ootb: 1
recommendation: 7
create_date: 2022-01-26
---

![[assets/Pasted image 20220126220142.png]]


# Path Autocomplete 路径填充

https://marketplace.visualstudio.com/items?itemName=ionutvmi.path-autocomplete

## 特点

-   它支持相对路径（以 ./ 开头）
-   它支持工作区的绝对路径（以 / 开头）
-   它支持文件系统的绝对路径（以：C : 开头）
-   它支持相对于用户文件夹的路径（以 ~ 开头）
-   它支持部分路径（./tmp/fol 识别为 ./tmp/folder1 如果存在）
-   `path-autocomplete.excludedItems`它通过选项支持项目排除
-   它支持 npm 包（以 az 开头，与磁盘无关）
-   支持选择文件夹后自动建议
-   `path-autocomplete.pathMappings`它通过选项支持自定义映射
-   它支持通过自定义转换插入的文本`path-autocomplete.transformations`
-   它支持 Windows 路径`path-autocomplete.useBackslash`

## 配置

-   `path-autocomplete.extensionOnImport` - boolean 如果为 true，则在`import`或`require`语句上插入文件名时也会附加扩展名。
    
-   `path-autocomplete.includeExtension`- boolean 如果为 true，则在插入文件名时也会附加扩展名。
    
-   `path-autocomplete.excludedItems` 排除某些文件
    
    ```
    "path-autocomplete.excludedItems": {
        "**/*.js": { "when": "**/*.ts" }, // ignore js files if i'm inside a ts file
        "**/*.map": { "when": "**" }, // always ignore *.map files
        "**/{.git,node_modules}": { "when": "**" }, // always ignore .git and node_modules folders
        "**": { "when": "**", "isDir": true }, // always ignore `folder` suggestions
        "**/*.ts": { "when": "**", "context": "import.*" }, // ignore .ts file suggestions in all files when the current line matches the regex from the `context`
    }
    ```
    
-   `path-autocomplete.pathMappings` 用于定义绝对或相对路径的别名。
    
    ```
    "path-autocomplete.pathMappings": {
        "/test": "${folder}/src/Actions/test", // alias for /test
        "/": "${folder}/src", // the absolute root folder is now /src,
        "$root": ${folder}/src // the relative root folder is now /src
        // or multiple folders for one mapping
        "$root": ["${folder}/p1/src", "${folder}/p2/src"] // the root is now relative to both p1/src and p2/src
    }
    ```
    
-   `path-autocomplete.pathSeparators`- string 列出用于在字符串外使用时提取插入路径的分隔符。默认值为：`\t({[`
    
-   `path-autocomplete.transformations` 应用于插入文本的自定义转换列表。示例：`_`选择 SCSS 部分文件时替换为空字符串。
    
    ```
    "path-autocomplete.transformations": [{
        "type": "replace",
        "parameters": ["^_", ""],
        "when": {
            "fileName": "\\.scss$"
        }
    }],
    ```
    
    支持的转换：
    
    -   `replace`- 对选定的项目文本执行字符串替换。参数：
        -   `regex` - 正则表达式模式
        -   `replaceString` - 替换字符串
-   `path-autocomplete.triggerOutsideStrings` boolean - 如果为真，它将触发引号之外的自动完成
    
-   `path-autocomplete.enableFolderTrailingSlash` boolean - 如果为 true，它将在插入将触发自动完成的文件夹路径后添加一个斜杠。
    
-   `path-autocomplete.disableUpOneFolder` boolean - 禁用完成列表中的上一个文件夹 (..) 元素。
    
-   `path-autocomplete.useBackslash`boolean - 如果为 true，它将`\\`在插入路径时使用。
    
-   `path-autocomplete.ignoredFilesPattern`- 字符串 - 用于在指定文件类型中禁用路径完成的 Glob 模式。示例：“* _/_ .{css,scss}”
    
-   `path-autocomplete.ignoredPrefixes`数组 - 忽略前缀列表，以禁用对某些前面的单词/字符的建议。例子：
    
    ```js
        "path-autocomplete.ignoredPrefixes": [
            "//" // type double slash and no suggesstions will be displayed
        ]
    ```
    

### 配置 VSCode 以识别路径别名

VSCode 不会自动识别路径别名，因此您无法通过 alt+click 来打开文件。要解决此问题，您需要创建项目`jsconfig.json`的`tsconfig.json`根目录并定义别名。一个示例配置：

```
{
  "compilerOptions": {
    "target": "esnext", // define to your liking
    "baseUrl": "./",
    "paths": {
      "test/*": ["src/actions/test"],
      "assets/*": ["src/assets"]
    }
  },
  "exclude": ["node_modules"] // Optional
}
```

### tips

-   如果你想在 markdown 或简单的文本文件中使用它，你需要启用`path-autocomplete.triggerOutsideStrings`
    
-   `./`对于相对路径
    
    > 如果`./`不能正常工作，请将其添加到`keybindings.json`: `{ "key": ".", "command": "" }`。
    
-   当我使用别名时，我无法在 Ctrl + Click 上跳转到导入的文件
    
    > 这由 jsconfig.json 中的编译器选项控制。您可以在项目根目录中创建 JSON 文件并为别名添加路径。jsconfig.json 参考 
    
-   如果您对重复建议有疑问，请使用该`path-autocomplete.ignoredFilesPattern`选项在某些文件类型中禁用路径自动完成
    
-   如果您需要更细粒度的控制来处理重复项目，您可以使用`path-autocomplete.excludedItems`如下选项：
    

```
// disable all suggestions in HTML files, when the current line contains the href or src attributes
"path-autocomplete.excludedItems": {
        "**": {
            "when": "**/*.html",
            "context": "(src|href)=.*"
        }
},

// for js and typescript you can disable the vscode suggestions using the following options
"javascript.suggest.paths": false,
"typescript.suggest.paths": false
```