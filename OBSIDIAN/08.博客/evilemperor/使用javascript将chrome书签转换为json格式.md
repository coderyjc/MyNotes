## chrome书签转化为json格式

json文件的格式

> 需要安装 jsdom依赖

> 目前有个小bug, 只能转换文件夹下面的, 在根目录的不可以转换

```js
const jsdom = require("jsdom");
const fs = require('fs')
var JSDOM = jsdom.JSDOM;

function main() {
    // 文件目录
  fs.readFile('./bookmarks_2022_8_1.html', 'utf-8', (err, res) => {
    // 内容转成dom对象
    let doms = parseToDOM(res);
    for (const dom of doms) {
        // 从dom对象中获取DL标签
        if (dom.tagName == 'DL') {
          let result = textHandle(dom, null);
            //写入文件（会覆盖之前的内容）（文件不存在就创建）  utf8参数可以省略 
            fs.writeFile('rst.json',JSON.stringify(result.children),'utf8',function(error){
              console.log('写文件成功');
            })
        }
    }
  })
}

function textHandle(dl, temp) {
    let dts = getDts(dl);
    if (dts.length > 0) {
        for (var i in dts) {
            let dt = dts[i], hdl = getTag(dt, "DL");
            if (hdl != null) {
                let h = getTag(dt, "H3");
                let returns = textHandle(hdl, {name: h.textContent, children: [], web: []})
                if (temp == null) {
                    temp = returns;
                } else {
                    temp.children.push(returns);
                }
            } else {
                var a = getTag(dt, "A");
                temp.web.push({
                    url: a.href,
                    title: a.textContent,
                })
            }
        }
    }
    return temp;
}

function getTag(dt, tagname) {
    let dtcs = dt.children, obj = null;
    if (dtcs.length < 1) {
        return obj
    }
    for (let dtc of dtcs) {
        if ((dtc.tagName.toUpperCase()) == tagname) {
            obj = dtc;
            break;
        }
    }
    return obj;
}

function getDts(dl) {
    let dlcs = dl.children, arr = [];
    if (dlcs.length < 1) {
        return arr;
    }
    for (let dlc of dlcs) {
        if ((dlc.tagName.toUpperCase()) == 'DT') {
            arr.push(dlc)
        }
    }
    return arr;
}

function parseToDOM(str) {
    var document = new JSDOM().window.document;
    let div = document.createElement("div");
    if (typeof str == "string") {
        div.innerHTML = str;
    }
    return div.childNodes;
}

main()

```