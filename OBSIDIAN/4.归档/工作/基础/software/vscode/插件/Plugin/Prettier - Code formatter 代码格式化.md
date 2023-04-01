---
type: 代码格式化
name: Prettier - Code formatter 代码格式化
ootb: 0
recommendation: 8
create_date: 2022-01-27
---

![[assets/Pasted image 20220127143548.png]]

# Prettier - Code formatter 代码格式化

插件：https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode

官网：https://www.prettier.cn/docs

## 配置

### 配置文件

==创建配置文件==

-   `package.json` 中的 `"prettier"` 关键字 
-   使用json或者yaml写的 `.prettierrc` 文件
-    `.prettierrc.json`, `.prettierrc.yml`, `.prettierrc.yaml`, 或者 `.prettierrc.json5` 文件
-   A `.prettierrc.js`, `.prettierrc.cjs`, `prettier.config.js`, 或者 `prettier.config.cjs` 文件，需要通过导出 `module.exports` 配置.
-   `.prettierrc.toml` 文件.

==基本配置==

json

```json
{
  "trailingComma": "es5",
  "tabWidth": 4,
  "semi": false,
  "singleQuote": true
}
```

JS:

```js
// prettier.config.js or .prettierrc.js
module.exports = {
  trailingComma: "es5",
  tabWidth: 4,
  semi: false,
  singleQuote: true,
};
```

YAML:

```yaml
# .prettierrc or .prettierrc.yaml
trailingComma: "es5"
tabWidth: 4
semi: false
singleQuote: true
```

TOML:

```toml
# .prettierrc.toml
trailingComma = "es5"
tabWidth = 4
semi = false
singleQuote = true
```

### 配置字段

**打印宽度**

```json
printWidth: 80
```

**tab宽度**

```json
tabWidth: 2
```

**分号**

行末的分号

```json
semi: true
```

**引号**

单引号还是双引号

```json
singleQuote: false
```

**大括号内空格**

-   `true` - Example: `{ foo: bar }`.
-   `false` - Example: `{foo: bar}`.

```json
bracketSpacing: true
```

**括号换行**

```html
<button
  onClick={this.handleClick}>
  true
</button>

<button
  onClick={this.handleClick}
>
  false
</button>
```

```json
bracketSameLine: false
```

**箭头函数的参数括号**

```json
arrowParens: "always" // or avoid
```

更多参考 [官方文档](https://www.prettier.cn/docs/options.html)