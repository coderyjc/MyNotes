---
type: 知识总结
skill: npm
create_date: 2022-01-31
---

#前端/NPM #前端/包管理工具

# NPM 知识总结

### **npm install moduleName 命令**

1.  安装模块到项目node_modules目录下。
2.  不会将模块依赖写入devDependencies或dependencies 节点。
3.  运行 npm install 初始化项目时不会下载模块。

### **npm install -g moduleName 命令**

1.  安装模块到全局，不会在项目node_modules目录中保存模块包。
2.  不会将模块依赖写入devDependencies或dependencies 节点。
3.  运行 npm install 初始化项目时不会下载模块。

### **npm install -save moduleName 命令**

1.  安装模块到项目node_modules目录下。
2.  会将模块依赖写入dependencies 节点。
3.  运行 npm install 初始化项目时，会将模块下载到项目目录下。
4.  运行npm install --production或者注明NODE_ENV变量值为production时，**会**自动下载模块到node_modules目录中。

### **npm install -save-dev moduleName 命令**

1.  安装模块到项目node_modules目录下。
2.  会将模块依赖写入devDependencies 节点。
3.  运行 npm install 初始化项目时，会将模块下载到项目目录下。
4.  运行npm install --production或者注明NODE_ENV变量值为production时，**不会**自动下载模块到node_modules目录中。