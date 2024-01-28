---
type: DeBug
skill: ElementUI
create_date: 2022-01-31
---

#前端/组件库 #前端/Vue

### 表单验证Validator的callback中一直拿不到value

有以下几种可能：

- `<el-form-item>`中的prop必须等于`<el-input中v-model="form.input1">`的input。
-  rules中的规则名称也需要和form中属性定义的名称相同
-   `<el-form-item>`上的prop名称不对，应当与rules中的名称一致；
-   绑定的属性没有在data中声明；
-   没有在`<el-form>`上指定model。
