起初是想实现 vim的自动补全功能的, 但是无意间发现了这个管理vim中插件的方法

> vim https://github.com/vim/vim.git
> vim插件管理软件  vim-plug https://github.com/junegunn/vim-plug
> 下载完管理插件的之后 从这里下载插件 https://vimawesome.com/

## Vim8.1 的安装

### 卸载旧版本Vim8.0

1. 查看所有与 vim 有关的包

`dpkg -l | grep vim`

```bash
➜  ~ dpkg -l | grep vim
ii  vim                                    2:8.0.1453-1ubuntu1.8               amd64        Vi IMproved - enhanced vi editor
ii  vim-common                             2:8.0.1453-1ubuntu1.8               all          Vi IMproved - Common files
rc  vim-nox                                2:8.0.1453-1ubuntu1.8               amd64        Vi IMproved - enhanced vi editor - with scripting languages support
ii  vim-runtime                            2:8.0.1453-1ubuntu1.8               all          Vi IMproved - Runtime files
rc  vim-tiny                               2:8.0.1453-1ubuntu1.8               amd64        Vi IMproved - enhanced vi editor - compact version
```

2. 删除所有的相关包

`sudo apt-get remove vim vim-runtime vim-common`

### 安装vim8.1


```bash
git clone https://github.com/vim/vim.git

cd vim

./configure

sudo make

sudo make install
```


## vim-plug的安装

> 简单翻译一下这个repo的readme.md

### 安装

下载 `plug.vim` 到vim目录, 我的是`/usr/share/vim/vim80/autoload`, 直接从[github的plug.vim](https://github.com/junegunn/vim-plug/blob/master/plug.vim)中复制然后编辑文件也可以.

如果没有这个文件夹, 就从用户文件夹中创建`.vimrc/autoload` 在这个文件夹中进行操作 

### 使用

在`~/.vimrc`中添加vim插件的片段

例子如下: 

```bash
call plug#begin()

Plug 'junegunn/vim-easy-align'

Plug 'SirVer/ultisnips' | Plug 'honza/vim-snippets'

Plug 'rdnetto/YCM-Generator', { 'branch': 'stable' }

Plug 'nsf/gocode', { 'tag': 'v.20150303', 'rtp': 'vim' }

Plug 'junegunn/fzf', { 'dir': '~/.fzf', 'do': './install --all' }

Plug '~/my-prototype-plugin'

call plug#end()
```

### 举例 -- 安装 Nerd Tree 插件

打开 https://vimawesome.com/plugin/nerdtree-red 

![[Pasted image 20220619130124.png]]

在 `.vimrc` 中加入 `Plug 'scrooloose/nerdtree'`

然后在vim编辑器中运行命令 

`:source %`
`:PlugInstall`

如图

![[Pasted image 20220619130325.png]]

输入PlugInstall命令之后显示, 成功

![[Pasted image 20220619130412.png]]

在`/vimrc` 中添加 `autocmd VimEnter * NERDTree` 设置自启动

### 卸载插件

先删除vimrc 中的Plug命令, 再在vim中执行命令 `:PlugClean`