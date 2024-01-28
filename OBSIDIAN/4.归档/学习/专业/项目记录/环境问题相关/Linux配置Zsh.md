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
> ![[../../../../4/assets/Pasted image 20220604230305.png]]

极简模式：

```shell
PROMPT="%{$terminfo[bold]$fg[red]%}$ %{$reset_color%}"
```

Geek模式：

```shell
PROMPT="%{$fg[cyan]%}[$PWD] %{$fg[magenta]%}No %{$fg[yellow]%}Coding, %{$fg[magenta]%}No %{$fg[green]%}Life% \

%{$terminfo[bold]$fg[green]%}$ %{$reset_color%}"
```

花里胡哨的模式：

```shell
PROMPT="%{$fg[cyan]%}[%2C] %{$fg[green]%}No Coding, No Life %{$fg[red]%}(ง •_•)ง \

%{$terminfo[bold]$fg[green]%}$ %{$reset_color%}"
```

![[assets/Pasted image 20230511115020.png]]

其他配置项

```bash
%%  一个'%'
#%) 一个')'
%y  当前的tty名
%l  当前的tty名，如 pts/1
%M  完整主机名
%m  主机名（在第一个句号之前截断）
%n  当前用户名
%. %c %C 前两个显示相对路径的当前文件夹名，最后一个是绝对路径（也就是说，前两个在家目录下显示'~'，最后那个显示你的用户名），'%'后的数字表示显示几层路径
%N  zsh 正在执行的脚本/函数名。如果'%'后跟了数字，似乎还有其他作用
%L  当前shell的层数
%j  当前正在进行的工作数量
%i  与%!类似：The line number currently being executed in the script, sourced file,<br>         or shell function given by %N. This is most useful for debugging as part of $PS4.
%!  显示当前历史事件号码（也就是打开shell后第几条命令）
%/ %d   显示当前工作路径（$pwd）。如果'％'后面是一个整数，它指定显示路径的元件的数量;没有数字就显示整个路径。一个负整数就是指定主目录，即％-1d代表第一部分
%~  目前的工作目录相对于～的相对路径
%?  返回最后命令的执行结果的代码
%#  用户组，#（普通用户）/%（超级用户）
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