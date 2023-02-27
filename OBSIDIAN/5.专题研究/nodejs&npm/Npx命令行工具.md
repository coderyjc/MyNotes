npx是npm5.2之后自带的一个命令。
npx的作用非常多，但是比较常见的是使用它来调用项目中的某个模块的指令。

我们以webpack为例：
全局安装的是webpack5.1.3
项目安装的是webpack3.6.0

如果我在终端执行 webpack --version使用的是哪一个命令呢？
显示结果会是 webpack 5.1.3，事实上使用的是全局的，为什么呢？
原因非常简单，在当前目录下找不到webpack时，就会去全局找，并且执行命令；

如何解决这个问题呢？

那么如何使用项目（局部）的webpack，常见的是两种方式：

- 方式一：明确查找到node_module下面的webpack
- 方式二：在 scripts定义脚本，来执行webpack；

◼ 方式一：在终端中使用如下命令（在项目根目录下）
```bash
./node_modules/.bin/webpack --version
```
◼ 方式二：修改package.json中的scripts
```json
"scripts": {
"webpack": "webpack --version"
}
```


方式三：==使用npx==
```bash
npx webpack --version
```

npx的原理非常简单，它会到当前目录的node_modules/.bin目录下查找对应的命令；
