# 安装与配置zsh

转载请注明原文链接：[安装与配置zsh](https://www.wangt.cc//2021/11/%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AEzsh/)


## apt安装zsh

### 查看是否安装有zsh

> cat /etc/shells

### 安装zsh

> sudo apt install zsh

### 切换shell为zsh

> chsh -s %(which zsh)

### 查看当前shell

> echo $SHELL

## 源码安装zsh

### 下载zsh

```
wget https://nchc.dl.sourceforge.net/project/zsh/zsh/5.8/zsh-5.8.tar.xz
```

### 解压并安装

```
解压
tar xvf zsh-5.8.tar.xz
安装
cd zsh-5.8
./configure --prefix=$HOME/.local
make && make install
```

### 配置环境变量

```
vim .bashrc
添加
export PATH=$PATH:$HOME/.local/bin	# 设置环境变量
export SHELL=`which zsh`      		# 设置$SHELL为zsh
exec `which zsh` -l           		# 设置登录为zsh
```

## 配置zsh

### 安装oh-my-zsh

-   从github安装

```
 wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
 zsh install.sh
```

-   从gitee安装
    
    ```
    1.下载安装文件
    wget https://gitee.com/mirrors/oh-my-zsh/raw/master/tools/install.sh
    2.修改install.sh文件内容
    找到以下内容
    ----------------------------------------------------------------
    # Default settings
    ZSH=${ZSH:-~/.oh-my-zsh}
    REPO=${REPO:-ohmyzsh/ohmyzsh}
    REMOTE=${REMOTE:-https://github.com/${REPO}.git}
    BRANCH=${BRANCH:-master}
    ----------------------------------------------------------------
    将其中的第3，4行替换为以下内容
    ----------------------------------------------------------------
    REPO=${REPO:-mirrors/oh-my-zsh}
    REMOTE=${REMOTE:-https://gitee.com/${REPO}.git}
    ----------------------------------------------------------------
    3.保存文件，赋予执行权限
    4.执行
    5.修改仓库地址
    cd ~/.oh-my-zsh
    git remote set-url origin https://gitee.com/mirrors/oh-my-zsh.git
    git pull
    6.结束
    ```

### 修改主题为ys主题

> vim ~/.zshrc  
> 修改:ZSH_THEME="ys"

### 修改ys主题（可选）

> vim ~/.oh-my-zsh/themes/ys.zsh-theme  
> 修改49行以下内容，去掉主机名  
> ![[../Python/assets/Pasted image 20220604230305.png]]

极简模式：

```shell
PROMPT="%{$terminfo[bold]$fg[red]%}$ %{$reset_color%}"
```

Geek模式：

```shell
PROMPT="%{$fg[cyan]%}[$PWD] %{$fg[magenta]%}No %{$fg[yellow]%}Coding, %{$fg[magenta]%}No %{$fg[green]%}Life% \

%{$terminfo[bold]$fg[green]%}$ %{$reset_color%}"
```


### 安装插件

-   autojump
-   autosuggestioins
-   syntax-highlighting

### 安装autjump

```bash
#.下载插件autojump到/.oh-my-zsh/custom目录中 
git clone https://gitee.com/haha-web/autojump.git $ZSH_CUSTOM/plugins/autojump 
#.到目录autojump中 
cd $ZSH_CUSTOM/plugins/autojump 
#执行install.py 
./install.py
```

在Gitee上直接搜一个就可以了

install完之后会提示在zshrc上添加一段(会提示的)

```bash
[[ -s /home/jancoyan/.autojump/etc/profile.d/autojump.sh ]] && source /home/jancoyan/.autojump/etc/profile.d/autojump.sh

autoload -U compinit && compinit -u  
```



### 安装autosuggestioins

```bash
git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

```bash
git clone https://gitee.com/phpxxo/zsh-autosuggestions.git ${ZSH_CUSTOM}/plugins/zsh-autosuggestions
```

### 安装syntax-highlighting

```bash
github
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
gitee
git clone https://gitee.com/wxzxingtian/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
```

### 加载插件

```
$ vim ~/.zshrc
修改以下内容
plugins=(git)为
plugins=(git extract zsh-autosuggestions zsh-syntax-highlighting)

$ source~/.zshrc
```