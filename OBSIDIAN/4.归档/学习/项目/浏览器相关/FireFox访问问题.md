## 火狐浏览器访问github提示：未连接：有潜在的安全问题

火狐浏览器访问github，提示：

```text
未连接：有潜在的安全问题；
Firefox 检测到潜在的安全威胁，并因 github.com 要求安全连接而没有继续。
```

如果这种情况是因为使用DevSidecar而引起的，可以使用以下方式解决：

在地址栏输入：about:config

在搜索框输入：security.enterprise_roots.enabled  将值切换为true即可。

