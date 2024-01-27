---
type: DeBug
skill: ElementUI
create_date: 2022-01-31
---

#前端/组件库 #前端/Vue

# ElemetUI


### 表单验证Validator的callback中一直拿不到value

有以下几种可能：

- `<el-form-item>`中的prop必须等于`<el-input中v-model="form.input1">`的input。
-  rules中的规则名称也需要和form中属性定义的名称相同
-   `<el-form-item>`上的prop名称不对，应当与rules中的名称一致；
-   绑定的属性没有在data中声明；
-   没有在`<el-form>`上指定model。

### ColorPicker 的颜色格式问题

这个组件颜色格式

color-format 表示写入 v-model的时候的颜色格式

**在滑动小圆点的时候只是改变了预览颜色的值， 并没有写入v-model， 这个时候是以默认的rgb表示的。因此，如果想让其生效，就必须点击“确定”按钮让颜色的数据生效**
![[../Vue.js/assets/Pasted image 20220506190509.png]]
![[../Vue.js/assets/Pasted image 20220506190604.png]]

