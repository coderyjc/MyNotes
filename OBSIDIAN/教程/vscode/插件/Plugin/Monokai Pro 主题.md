---
type: 主题
name: Monokai Pro 主题
ootb: 1
recommendation: 9
create_date: 2022-01-26
---


# Monokai Pro 主题

## 特点



## 激活

### 方式一

1. 输入Monokai Pro: enter license，回车  ，输入：`id@chinapyg.com`  
2. 输入lincese key 回车  输入：`d055c-36b72-151ce-350f4-a8f69`

### 方式二

找到 `C:\Users\用户名\.vscode\extensions\monokai.theme-monokai-pro-vscode-1.1.18\js`

2、打开app.js，搜索`key: "isValidLicense"`，找到如下地方，注释掉原来的代码，保存即可。  

修改方式如下：

```js
    key: "isValidLicense",
    value: function()
    {
        var e = arguments.length > 0 && void 0 !== arguments[0] ? arguments[0] : "",
            t = arguments.length > 1 && void 0 !== arguments[1] ? arguments[1] : "";
        //if (!e || !t) return !1; 注释掉原来的代码
        if (!e || !t) return 1;
        var o = s()("".concat(i.APP.UUID).concat(e)),
            r = o.match(/.{1,5}/g),
            n = r.slice(0, 5).join("-");
        //return t === n  注释掉原来的代码
        return 1
    }
```

