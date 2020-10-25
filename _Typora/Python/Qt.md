## 基本功能

### 空白窗口

```python
"""显示一个空白窗口"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)  # 每一PyQt5应用程序必须创建一个应用程序对象。sys.argv参数是一个列表，从命令行输入参数。
    window = QWidget()  # QWidget部件是PyQt5所有用户界面对象的基类。他为QWidget提供默认构造函数
    window.resize(300, 300)  # 调整窗口的大小
    window.move(300, 300)  # 移动窗口在屏幕上的位置
    window.setWindowTitle("This is test window")  # 设置窗口的标题
    window.show()  # 显示
    sys.exit(app.exec_())  # 系统exit()方法确保应用程序干净的退出的exec_()方法有下划线。因为它是一个Python关键词。
```

### 小图标


```python
"""面向对象编程，添加一个程序图标"""
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):  # 继承QWidget父类
    def __init__(self):  # 构造方法
        super().__init__()  # 初始化父类属性
        self.InitUI()  # 绘制界面(调用这个函数)

    def InitUI(self):
        self.setGeometry(600, 600, 600, 300)  # 设置窗口的位置和大小
        self.setWindowTitle("Test2")
        self.setWindowIcon(QIcon('..\\img\\icon.png'))  # 设置窗口的图标
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序
    e = Example()  # 创建对象
    sys.exit(app.exec())

```

### 关闭窗口按钮和提示语


```python
"""显示提示语 和 关闭窗口"""

import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))  
        # QToolTip 是一个用来显示消息的静态方法，这句话的目的是设置字体，第一个参数是字体名字，第二个是大小
        
        q_btn = QPushButton('Quit', self)  # 设置按钮，第一个参数是按钮显示的名字，第二个是"按钮为谁设置"
        q_btn.setToolTip('You will <font color=red><b>close</b></font> the window')  
        # 文字中可以有html元素
        
        q_btn.resize(q_btn.sizeHint())  # 重新设置按钮大小，sizeHint() 表示默认大小
        q_btn.move(50, 50)  # 按钮位置
        q_btn.clicked.connect(QCoreApplication.instance().quit)  # 点击按钮之后退出程序

        self.setGeometry(300, 300, 300, 200)  # 窗口大小和位置
        self.setWindowTitle('Tooltips')  # 窗口名字
        self.show()  # 显示窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

### 窗口居中和消息框


```python
"""消息框 和 让窗口显示在屏幕中间"""
import sys

from PyQt5.QtWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):

        self.resize(600, 600)
        self.center()  # 调用‘将窗口显示到屏幕中央’函数
        self.setWindowTitle('MessageBox')  # 窗口名字
        self.show()  # 显示窗口

    """
    在我们关闭窗口的时候会触发 QCloseEvent ，所以我们需要重写这个事件处理程序
    所有的函数的第一个参数必须都是self
    随后的几个参数分别是 yes的结构，no的结果，和默认的结果
    """

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Quit',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        # 获得窗口
        window = self.frameGeometry()
        # 获得屏幕中心点
        center_point = QDesktopWidget().availableGeometry().center()
        # 显示到屏幕中心点
        window.moveCenter(center_point)
        self.move(window.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```


## 布局管理


### 框布局 Boxlayout

```python
import sys

from PyQt5.QtWidgets import *


# 使用QHBoxLayout和QVBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):

        ok_button = QPushButton("OK")
        cancel_button = QPushButton("Cancel")

        h_box = QHBoxLayout()  # 创建垂直布局
        h_box.addStretch(1)  # 在前面添加一个伸展因子
        h_box.addWidget(ok_button)  # 添加ok按钮
        h_box.addWidget(cancel_button)  # 添加cancel按钮

        v_box = QVBoxLayout()  # 创建水平布局
        v_box.addStretch(1)  # 在水平布局前面添加一个伸展因子
        v_box.addLayout(h_box)

        self.setLayout(v_box) 

        self.setGeometry(500, 500, 300, 300)
        self.setWindowTitle('Buttons')  # 窗口名字
        self.show()  # 显示窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
```



### 表格布局QGridLayout

QGridLayout支持在其中嵌套其他的布局管理器称为其管理对象

```python
import sys

from PyQt5.QtWidgets import *


# 表格布局将空间划分为行和列，使用QGridLayout 创建一个网格布局

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.InitUI()

    def InitUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        names = ['Cls', 'Bck', '', 'Close',
                 '7', '8', '9', '/',
                 '4', '5', '6', '*',
                 '1', '2', '3', '-',
                 '0', '.', '=', '+']

        positions = [(i, j) for i in range(5) for j in range(4)]
    
        for position, name in zip(positions, names):
            # zip 函数将传入其中的两个参数组成一个元组返回
            if name == '':
                continue
            button = QPushButton(name)
            grid.addWidget(button, *position)

        self.setGeometry(500, 500, 300, 300)
        self.setWindowTitle('Buttons')  # 窗口名字
        self.show()  # 显示窗口


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

```

### 例子 : 评论

```python
import sys
from PyQt5.QtWidgets import *


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')

        title_edit = QLineEdit()  # 行编辑
        author_edit = QLineEdit()
        review_edit = QTextEdit()  # 文本编辑

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(title, 1, 0)
        grid.addWidget(title_edit, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(author_edit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(review_edit, 3, 1, 5, 1)
        # 四个数值参数分别为 所在行，所在列，所占行数，所占列数

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())
```




## 菜单和工具栏

### 状态栏

QMainWindow 类提供了一个主要的应用程序窗口。你用它可以让应用程序添加状态栏,工具栏和菜单栏。

```python
    def initUI(self):
        self.statusBar().showMessage('Ready')
        # QMainWindow类第一次调用statusBar()方法创建一个状态栏。
        # 后续调用返回的状态栏对象。showMessage()状态栏上显示一条消息。

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('StatusBar')
        self.show()
```

### 菜单栏

```python

class Example(QMainWindow):

    def initUI(self):

        exit_action = QAction(QIcon('..\\img\\icon.png'), '&Exit', self)
        exit_action.setShortcut('Ctrl+Q')  # 创建快捷方式
        # 注意！！加号前后不能有空格 ! ! !

        exit_action.setStatusTip('Exit application')
        exit_action.triggered.connect(qApp.quit)  # 创建鼠标指针悬停的提示

        self.statusBar()

        menubar = self.menuBar()  # 创建一个菜单栏
        file_menu = menubar.addMenu('&File')  # 添加菜单
        file_menu.addAction(exit_action)  # 添加事件

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')
        self.show()
```



### 工具栏

```python
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exit_action = QAction(QIcon('../img/icon.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Toolbar')
        self.show()

```


### 放在一起





## 事件和信号

### 事件和信号槽



### 重新实现事件处理器



### 事件发送者



### 发出信号




## 控件



### QCheckBox



### 开关按钮



### 滑动条


### 进度条



### 日历控件


### QPixmap



### 文本框



### QSplitter



### 下拉列表





## 拖拽


### 简单拖拽



### 拖拽一个按钮




## 绘图



### 绘制文本



### 画点



### 颜色



### QPen（画笔）


### QBrush（笔刷）