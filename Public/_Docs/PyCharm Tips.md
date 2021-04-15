## PyCharm使用技巧



| 快捷键                  | 作用         |
| ----------------------- | ------------ |
| Ctrl + O （大写字母 O） | 重写父类方法 |
|Ctrl + I （字母 I）|  重写父类接口|
|Ctrl + Shift + U   | 代码大小写转换|
|Ctrl + - | 折叠代码块 |
|Ctrl + + | 展开代码块 |
|Ctrl + Shift + - | 折叠所有代码块|
|Ctrl + Shift + + | 展开所有代码块|
|Ctrl + X | 删除一行 |
|Ctrl + Shift + V|调出Pycharm内置剪贴板|



## PyCharm Plugins

1. Key Promoter X

比如我使用鼠标点开 Find in Path，它就会在右下角弹窗提示你该用哪个快捷键。

2. Vim in PyCharm

在大多数场景之下，使用鼠标的效率和精准度，是远不如键盘快捷键的（前提是你已经相当熟练的掌握了快捷键），这个你得承认吧。

Vi 可以满足你对文本操作的所有需求，比可视化界面更加效率，更加 geek。如果你和我一样，是忠实的 vim 粉。在安装完 Pycharm 完后，肯定会第一时间将 ideaVim 这个插件也装上，它可以让我们在 Pycharm 中 使用 vim 来编辑代码。

安装方法如下，安装完后需要重启 Pycharm 生效。

3. Markdown in PyCharm

富文本排版文档是一件非常痛苦的事情 ，对于程序员写文档，最佳的推荐是使用 Markdown ，我所有的博客日记都是使用 Markdown 写出来的。

从 Github下载的代码一般也都会带有README.md文件，该文件是一个Markdown格式的文件。

PyCharm是默认没有安装Markdown插件的，所以不能按照Markdown格式显示文本，显示的是原始文本。

因此，如果要在 PyCharm 中阅读 Markdown 文档，可以装一下 Markdown support 这个插件。


5. Regex Tester in PyCharm

Regex Tester是PyCharm的第三方插件，可以测试正则表达式。

按照下图入口，安装 Regex Tester 插件：


安装完成后，无需重启 PyCharm ，点击  PyCharm  界面左下方的小矩形按钮，就能找到 Regex Tester 选项。

6. Use Bash in Windows

在 Windows 上的 cmd 命令和 Linux 命令有不少的差异，比如要列出当前目录下的所有文件，Windows 上是用 dir ，而 Linux 上则是用 ls -l 。

对于像我这样熟悉 Linux 的开发者来说，Windows 的 那些 CMD 命令带来的糟糕体验是无法忍受的。

在弹出的 Bash 窗口，你可以敲入你想使用的 Linux 命令，是不是舒服多了。

7. Auto PEP8 in PyCharm

pep8 是Python 语言的一个代码编写规范。如若你是新手，目前只想快速掌握基础，而不想过多去注重代码的的编写风格（虽然这很重要），那你可以尝试一下这个工具 - autopep8

首先在全局环境中（不要在虚拟环境中安装），安装一下这个工具。

$ sudo pip install autopep8
然后在 PyCharm 导入这个工具，具体设置如下图

Name: AutoPep8
Description: autopep8 your code
Program: autopep8
Arguments: --in-place --aggressive --aggressive $FilePath$
Working directory: $ProjectFileDir$
Output filters: $FILE_PATH$\:$LINE$\:$COLUMN$\:.*

8. Test RESTful Web Service

PyCharm 的 Test RESTful Web Service工具提供了RESTful接口测试界面，如下图所示，提供了get、post，put等http方法，其中的Request子界面headers，Parameters，Body等功能，Response子界面用于显示返回值，Response Headers用于显示返回的消息头。

10. CodeGlance

如果你曾使用过 Sublime Text，切换到其他代码编辑器，或多或少会有些不习惯，因为很少有编辑器会像 Sublime 那样自带一个预览功能的滚动条。

在 PyCharm 中，就没有解决不了的问题，如果有，那么就装个插件。

要想在 PyCharm 中使用这个预览滚动条，只要装上 CodeGlance 这个插件。使用效果如下

13. 12. Profile in PyCharm

在 Python 中有许多模块可以帮助你分析并找出你的项目中哪里出现了性能问题。

比如，常用的模块有 cProfile，在某些框架中，也内置了中间件帮助你进行性能分析，比如 Django ，WSGI。

做为Python 的第一 IDE， PyCharm 本身就支持了这项功能。而且使用非常方便，小白。

假设现在要分析如下这段代码的性能损耗情况，找出到底哪个函数耗时最多

import time

def fun1():
    time.sleep(1)

def fun2():
    time.sleep(1)

def fun3():
    time.sleep(2)

def fun4():
    time.sleep(1)

def fun5():
    time.sleep(1)
    fun4()

fun1()
fun2()
fun3()
fun5()
点击 Run -> Profile '程序' ，即可进行性能分析。


运行完毕后，会自动跳出一个性能统计界面。


性能统计界面由Name、Call Count、Time(ms)、Own Time(ms) ，4列组成一个表格，见下图。

表头Name显示被调用的模块或者函数；Call Count显示被调用的次数；Time(ms)显示运行时间和时间百分比，时间单位为毫秒（ms）。
点击表头上的小三角可以升序或降序排列表格。
在Name这一个列中双击某一行可以跳转到对应的代码。
以fun4这一行举例：fun4被调用了一次，运行时间为1000ms，占整个运行时间的16.7%
点击 Call Graph（调用关系图）界面直观展示了各函数直接的调用关系、运行时间和时间百分比，见下图。


右上角的4个按钮表示放大、缩小、真实大小、合适大小；

箭头表示调用关系，由调用者指向被调用者；
矩形的左上角显示模块或者函数的名称，右上角显示被调用的次数；
矩形中间显示运行时间和时间百分比；
矩形的颜色表示运行时间或者时间百分比大小的趋势：红色 > 黄绿色 > 绿色，由图可以看出fun3的矩形为黄绿色，fun1为绿色，所有fun3运行时间比fun1长。
从图中可以看出Test.py直接调用了fun3、fun1、fun2和fun5函数；fun5函数直接调用了fun4函数；fun1、fun2、fun3、fun4和fun5都直接调用了print以及sleep函数；整个测试代码运行的总时间为6006ms，其中fun3的运行时间为1999ms，所占的时间百分比为33.3%，也就是 1999ms /  6006ms = 33.3%。
13. Json Parse in PyCharm

在开发过程中，经常会把校验一串 JSON 字符串是否合法，在以前我的做法都是打开 https://tool.lu/json/ 这个在线网站，直接美化来校验，只有 JSON 格式都正确无误合法的，才能够美化。

img
img
直到后来发现在 PyCharm 有一个插件专门来做这个事，那就是 JSON Parser，在插件市场安装后，重启 PyCharm ，就能在右侧边栏中看到它。

img
img


14. Inspect Code in PyCharm

对于编译型的语言，如 Java，需要将代码编译成机器可识别的语言才可运行，在编译过程中，就可以通过分析或检查源程序的语法、结构、过程、接口等来检查程序的正确性，找出代码隐藏的错误和缺陷。这个过程叫做静态代码分析检查。

那对于 Python 这种解释型的语言来说，代码是边运行边翻译的，不需要经过编译这个过程。很多肉眼无法一下子看出的错误，通常都是跑一下（反正跑一下这么方便）才能发现。

由于Python 运行是如此的方便，以至于我们都不太需要关注静态分析工具。

但也不是说，静态分析工具完全没有用武之地，我认为还是有。

如果你的编码能力还没有很成熟，代码中可以有许许多多的隐藏bug，由于 Python 是运行到的时候才解释，导致一次运行只能发现一个错误，要发现100个bug，要运行100次，数字有点夸大，其实就是想说，如果这么多的错误都能通过一次静态检查发现就立马修改，开发调试的效率就可以有所提升。当然啦，并不是说所有的错误静态分析都能提前发现，这点希望你不要误解。

做为 Python 最强 IDE，PyCharm本身内置了这个功能，不需要你安装任何插件。

你只需要像下面这样点击项目文件夹，然后右键，选择 Inspect Code，就可以开启静态检查。

图片
我对开源组件 nova 的静态检查发现，其有不规范的地方有数千处。

