---
type: DeBug
skill: Gradle
create_date: 2022-05-08
---

### Could not install Gradle distribution from 'https://services.gradle.

没有设置代理服务器加速，这个加速不能在初始化的时候设置，应该在设置里手动添加

这里这样设置

![[assets/Pasted image 20220310185259.png]]

```text
mirrors.neusoft.edu.cn
```
