---
type: 功能增强
name: Import Cost 显示包大小
ootb: 
recommendation: 6
create_date: 2022-01-26
---

![[assets/Pasted image 20220126213304.png]]

# Import Cost 显示包大小

https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost

## 特点

计算进口量和需求量。目前支持：

-   默认导入： `import Func from 'utils';`
-   全部内容导入： `import * as Utils from 'utils';`
-   选择性导入： `import {Func} from 'utils';`
-   使用别名选择性导入： `import {orig as alias} from 'utils';`
-   子模块导入： `import Func from 'utils/Func';`
-   要求： `const Func = require('utils').Func;`

同时支持`Javascript`和`Typescript`


## 配置

以下属性是可配置的：

```javascript
  // 小包大小，单位KB
  "importCost.smallPackageSize": 50,

  // 中包大小，单位KB，大于这个大小就是大包
  "importCost.mediumPackageSize": 100,

  // 小包颜色
  "importCost.smallPackageColor": "#7cc36e",

  // 中包颜色
  "importCost.mediumPackageColor": "#7cc36e",

  // 大包颜色
  "importCost.largePackageColor": "#d44e40",

  // File extensions to be parsed by the Typescript parser
  "importCost.typescriptExtensions": [
    "\\.tsx?$"
  ],

  // File extensions to be parsed by the Javascript parser
  "importCost.javascriptExtensions": [
    "\\.jsx?$"
  ],

  // Which bundle size to display
  "importCost.bundleSizeDecoration": "both",

  // Display the 'calculating' decoration
  "importCost.showCalculatingDecoration": true,

  // Print debug messages in output channel
  "importCost.debug": false
```

任何超过 mediumPackageSize 限制的包大小都将被视为大包。