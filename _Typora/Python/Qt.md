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

```python
    def initUI(self):

        text_edit = QTextEdit()
        self.setCentralWidget(text_edit)

        # QAction可以操作菜单栏，工具栏和自定义键盘快捷键
        exit_action = QAction(QIcon('..\\img\\icon.png'), 'Exit', self)
        exit_action.setShortcut('Ctrl+Q')
        exit_action.setStatusTip('Exit this application')  # 鼠标悬停提示
        exit_action.triggered.connect(self.close)  #

        self.statusBar()

        menubar = self.menuBar()
        file_menu = menubar.addMenu('&File')
        file_menu.addAction(exit_action)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(exit_action)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()

```



## 事件和信号

### 事件和信号槽

所有的GUI程序都是事件驱动的。事件主要由用户触发，但也可能有其他触发方式：例如网络连接、window manager或定时器。当我们调用QApplication的exec_()方法时会使程序进入主循环。主循环会获取并发事件。

在事件模型中，有三个参与者：

- 事件源
- 事件对象
- 事件接收者

事件源是状态发生变化的对象。它会生成事件。事件(对象)封装了事件源中状态的变动。事件接收者是要通知的对象。事件源对象将事件处理的工作交给事件接收者。

PyQt5有一个独特的signal&slot(信号槽)机制来处理事件。信号槽用于对象间的通信。signal在某一特定事件发生时被触发，slot可以是任何callable对象。当signal触发时会调用与之相连的slot。

```python
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)  # LCD数字
        sld = QSlider(Qt.Horizontal, self)  # 滑块

        v_box = QVBoxLayout()  # 垂直布局
        v_box.addWidget(lcd)  # 添加LCD数字
        v_box.addWidget(sld)  # 添加滑块

        self.setLayout(v_box)  # 设置布局方式
        sld.valueChanged.connect(lcd.display)  # 将滑块的valueChanged信号连接到lcd的display插槽

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Signal and slot')
        self.show()
```

### 重新实现事件处理器

通过重新实现事件处理器来处理事件

```python
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event Handler')
        self.show()

    def keyPressEvent(self, e):  # 重写KetPressEvent 事件处理器

        if e.key() == Qt.Key_Escape:  # K大写
            self.close()  # 按下Esc后程序退出

```

### 事件发送者

sender()方法让我们知道事件是哪个控件发送的

```python
class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton("Button1", self)
        btn1.move(30, 50)

        btn2 = QPushButton("Button2", self)
        btn2.move(150, 50)

        # 创建了两个按钮并且连接到了同一个插槽
        btn1.clicked.connect(self.buttonClicked)
        btn2.clicked.connect(self.buttonClicked)

        self.statusBar()

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("Event Sender")
        self.show()

    def buttonClicked(self):
        # 通过调用sender方法判断信号源
        sender = self.sender()
        # 输出判断结果
        self.statusBar().showMessage(sender.text() + ' was pressed')
```

### 发出信号



```python
class Communicate(QObject):
    closeApp = pyqtSignal()  # 创建了一个closeApp信号
    # 这个信号会在按下鼠标的时候触发
    # 它连接着QMainWindow的close()插槽


class Example(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.comm = Communicate()
        self.comm.closeApp.connect(self.close)
        self.setGeometry(300, 300, 290, 150)
        self.show()

    def mousePressEvent(self, event):
        # 在窗体上点击鼠标时会触发closeApp信号，使程序退出
        self.comm.closeApp.emit()

```


## 控件

### QCheckBox

```python

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()  #
        cb.stateChanged.connect(self.changeTitle)  # 状态改变连接到changeTitle

        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('CheckBox')
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:  # 选中状态
            self.setWindowTitle('QCheckBox')  # 更改窗口标题
        else:
            self.setWindowTitle('')
```



### 开关按钮

```python
    def initUI(self):
        self.col = QColor(0, 0, 0)  # 初始颜色为黑色

        redb = QPushButton('Red', self)
        redb.setCheckable(True)
        redb.move(10, 10)
        redb.clicked[bool].connect(self.setColor)

        blueb = QPushButton('Blue', self)
        blueb.setCheckable(True)
        blueb.move(10, 60)
        blueb.clicked[bool].connect(self.setColor)

        greenb = QPushButton('Green', self)
        greenb.setCheckable(True)
        greenb.move(10, 110)
        greenb.clicked[bool].connect(self.setColor)

        self.square = QFrame(self)
        self.square.setGeometry(150, 20, 100, 100)
        self.square.setStyleSheet("QWidget{background-color:%s}" %
                                  self.col.name())

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Toggle button')
        self.show()

    def setColor(self, pressed):
        source = self.sender()

        if pressed:
            val = 255
        else:
            val = 0

        if source.text() == "Red":
            self.col.setRed(val)
        elif source.text() == "Green":
            self.col.setGreen(val)
        else:
            self.col.setBlue(val)

        self.square.setStyleSheet("QFrame{background-color:%s}" %
                                  self.col.name())

```



### 滑动条

```python
    def initUI(self):
        sld = QSlider(Qt.Horizontal, self)  # 创建一个水平滑块
        sld.setFocusPolicy(Qt.NoFocus)  # 如果不加上这一句，那么用户可以通过tab键选中这个滑块
        sld.setGeometry(30, 40, 200, 30)  # 滑块的位置，大小

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Slider')
        self.show()

```


### 进度条

```python
    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doSome)

        self.timer = QBasicTimer() # 定时器的构造方法
        self.step = 0

        self.setGeometry(300, 300, 200, 170)
        self.setWindowTitle('QProgressBar')
        self.show()

    def timerEvent(self, e):

        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doSome(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')
```



### 日历控件

```python
    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.move(20, 20)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())
        self.lbl.move(130, 260)

        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Calendar')
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())
```




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