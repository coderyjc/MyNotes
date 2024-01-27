由于一些特殊的原因，某些情况下我们没办法很好的从 https://registry.npmjs.org 下载下来一些需要的包

查看npm镜像：

```bash
npm config get registry # npm config get registry
```

我们可以直接设置npm的镜像：

```bash
npm config set registry https://registry.npm.taobao.org
```

但是对于大多数人来说（比如我），并不希望将npm镜像修改了：
第一，不太希望随意修改npm原本从官方下来包的渠道；
第二，担心某天淘宝的镜像挂了或者不维护了，又要改来改去；

这个时候，我们可以使用cnpm，并且将cnpm设置为淘宝的镜像：

```bash
npm install -g cnpm --registry=https://registry.npm.taobao.org
cnpm config get registry # https://r.npm.taobao.org/
```

