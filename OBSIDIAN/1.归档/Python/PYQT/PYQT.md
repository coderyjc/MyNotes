

## 信号与槽

### 一个信号一个槽

- 信号clicked：点击

```python

class Demo(QWidget):  # 继承QWidget
    def __init__(self):
        super(Demo, self).__init__()

        self.button = QPushButton('Start', self)  # 因为是继承于QWidget，所以self不能忘了
        # （相当于告诉了程序这个QPushButton是放在QWidget这个房子中的）
        self.button.clicked.connect(self.change_text)  # 连接信号与槽函数
        # self.button 是一个控件，clicked（按钮被点击）是一个信号，connect()是连接，括号中是槽函数

    def change_text(self):
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)  # 信号与槽解绑，如果把这一行注释掉，则每一次点击都会输出一次change text

```

### 多个信号一个槽

- 信号 pressed：当鼠标在button上并单击左键的时候触发信号
- 信号 released：当鼠标左键被释放的时候触发信号

```python
class Demo(QWidget):  # 继承QWidget
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        self.button.pressed.connect(self.change_text)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')
```

### 信号与信号连接

```python
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Start', self)
        #  将pressed信号和released信号连接起来，而released信号则与槽函数连接。
        #  这样当点击不放时，pressed信号发出，released信号也会发出，从而启动槽函数。
        #  释放鼠标则发出released信号，再次启动槽函数。所以程序运行效果跟2.2小节其实是一样的。
        self.button.pressed.connect(self.button.released)
        self.button.released.connect(self.change_text)

    def change_text(self):
        if self.button.text() == 'Start':
            self.button.setText('Stop')
        else:
            self.button.setText('Start')
```

### 一个信号多个槽


```python
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 300)  # 初始化窗口的大小
        self.setWindowTitle('demo')  # 设置窗口名称
        self.button = QPushButton('Start', self)
        # 连接三个槽函数
        self.button.clicked.connect(self.change_text)
        self.button.clicked.connect(self.change_window_size)  # 3
        self.button.clicked.connect(self.change_window_title)  # 4

    def change_text(self):
        print('change text')
        self.button.setText('Stop')
        self.button.clicked.disconnect(self.change_text)

    def change_window_size(self):  # 5
        print('change window size')
        self.resize(500, 500)
        self.button.clicked.disconnect(self.change_window_size)

    def change_window_title(self):  # 6
        print('change window title')
        self.setWindowTitle('window title changed')
        self.button.clicked.disconnect(self.change_window_title)

```

## 第三章 布局管理

### 垂直布局管理

```python
"""
垂直布局管理
"""

class Demo(QWidget):

	def __init__(self):
		super(Demo(),  self)
		self.user_label = QLabel('Username:',  self)
		self.pwd_label = QLabel('Password:',  self)  # 两个文本标签

		self.v_layout = QVBoxLayout()  # 实例化一个垂直布局管理器
		self.v_layout.addWidget(self.user_label)
		self.v_layout.addWidget(self.pwd_label)  # 添加两个文本标签

		self.setLayout(self.v_layout)  # 将self.v_layout设置为整个窗口的最终布局方式

```

### 水平布局管理
```python

"""
水平布局管理
"""

class Demo(QWidget):

	def __init__(self):
		super(Demo, self).__init__()
		self.uer_label = QLabel('Username',  self)
		self.user_line = QLineEdit(self)  # 单行输入文本

		self.h_layout = QHBoxLayout()  # 实例化一个水平布局管理器
		self.h_layout.addWidget(self.user_label)
		self.h_layout.addWidget(self.user_line)  # 添加刚才的两个widget
		# 先添加的出现在左边

		self.setLayout(self.h_layout)  # 将self.h_layout 设置为整个个窗口的最终布局方式

```

### 水平垂直混合使用

```python
"""
混合使用水平bu'ju
"""

class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()

        # 初始化按钮、文本行、标签等
        self.user_label = QLabel('Username', self)
        self.pwd_label = QLabel('Password', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.label_v_layout = QVBoxLayout()  # 用来管理label
        self.line_v_layout = QVBoxLayout()  # 用来管理line
        self.button_h_layout = QHBoxLayout()  # 用来管理button

        # 将self.label_v_layout垂直布局和self.line_vlayout垂直布局这两个布局管理器从左到右依次水平摆放
        self.label_line_h_layout = QHBoxLayout()
        # 将self.label_line_h_layout和self.button_h_layout垂直从上到下摆放
        self.all_v_layout = QVBoxLayout()
        # 以上两个布局管理器用来管理1 - 3中的布局，我们应该通过addLayout()向其中添加布局管理器

        self.label_v_layout.addWidget(self.user_label)
        self.label_v_layout.addWidget(self.pwd_label)
        self.line_v_layout.addWidget(self.user_line)

        self.line_v_layout.addWidget(self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)

        self.label_line_h_layout.addLayout(self.label_v_layout)
        self.label_line_h_layout.addLayout(self.line_v_layout)
        self.all_v_layout.addLayout(self.label_line_h_layout)
        self.all_v_layout.addLayout(self.button_h_layout)
        # 添加控件用addWidght()，添加布局用addLayout()

        self.setLayout(self.all_v_layout)

# 上面的代码是将两个QLabel用垂直布局方式摆放，将两个QLineEdit也用垂直布局方式摆放，最后用一个水平布局管理来摆放着两个垂直布局管理器。那换种思路，可以把QLabel和QLineEdit用水平布局方式摆放

# 自己实现上述过程。

```

### 表单布局

```python
"""
表单布局 QFormLayout
"""

# 表单布局可以将控件以两列的形式进行排布，左列控件为文本标签，右列为输入型的控件，如QLineEdit。

class Demo(QWidget):

	def __init__(self):
		super(Demo, self).__init__()

		self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

        self.f_layout = QFormLayout()  # 实例化一个QFormLayout控件

        self.button_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        # 调用addRow()方法传入QLabel和QLineEdit控件
        self.f_layout.addRow(self.user_label, self.user_line)  
        self.f_layout.addRow(self.pwd_label, self.pwd_line)
        self.button_h_layout.addWidget(self.login_button)
        self.button_h_layout.addWidget(self.signin_button)

        self.all_v_layout.addLayout(self.f_layout)  # 将表单布局添加到总布局中
        self.all_v_layout.addLayout(self.button_h_layout)

        self.setLayout()

```

### 网格布局

```python
"""
网格布局 QGridLayout
"""

# 相当于坐标式布局

class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.user_label = QLabel('Username:', self)
        self.pwd_label = QLabel('Password:', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.login_button = QPushButton('Log in', self)
        self.signin_button = QPushButton('Sign in', self)

		self.grid_layout = QGridLayout()  # 实例化一个QGridLayout布局管理器
		self.h_layout = QHBoxLayout()
		self.v_layout = QVBoxLayout()

		self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
		self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
		self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
		self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
		# QGridLayout的addWidget()方法遵循如下语法形式：
		# addWidget(widget, row, column, rowSpan, columnSpan)
		# 在第几行，在第几列， 占几行， 占几列

		self.h_layout.addWidget(self.login_button)
		self.h_layout.addWidget(self.signin_button)

		self.v_layout.addWidget(self.grid_layout)
		self.v_layout.addWidget(self.h_layout)
		# 最后，程序用垂直布局管理器将一个网格布局和一个水平布局添加进去。

		self.setLayout(self.v_layout)

```



## 第四章 QMessageBox消息框

### 信息框

```python
class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Information', self)  # 实例化一个按钮
        self.button.clicked.connect(self.show_messageBox)  # 将按钮的点击状态与show_message连接

    def show_messageBox(self):
        QMessageBox.information(self, 'Title', 'Hello',
                                QMessageBox.Yes | QMessageBox.No)
    # 创建一个信息框
    # information(QWidget父类（self）, 信息框标题，信息框显示文本，信息框按钮（用 | 连接）)
```

按钮类型：

- QMessageBox.Ok
- QMessageBox.Yes
- QMessageBox.No
- QMessageBox.Close
- QMessageBox.Open
- QMessageBox.Cancel
- QMessageBox.Save

信息框类型：

- information
- question
- warning
- critical
- about

### 与信息框交互



```python
class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.show_message)

    def show_message(self):
        choice = QMessageBox.question(self, 'Change Text?', 'Would you like to change the button text?',
                                      QMessageBox.Yes | QMessageBox.No)
        # 点击了某个按钮之后会返回这个按钮，将返回的按钮保存在了choice中

        if choice == QMessageBox.Yes:
            self.button.setText('Changed!')
        elif QMessageBox == QMessageBox.No:
            pass  # 什么也不做

```

### 第五章 登录框小程序

突破瓶颈：

- 我们所写下的代码，都是分成了模块的（函数、类）
- 所以程序界面在初始化的时候，是“初始化了这些界面”并且<font color=red>将这些属性赋予了某个控件</font>
- 所以我们没有必要纠结于代码是不是顺序执行的，我们只知道我们赋予了这个控件哪些属性就可以了
- 因为当这个控件的这些属性被触发的时候，我们<font color=red>程序的调用也是模块化的</font>

```python
import sys
from PyQt5.QtWidgets import *

USER_PWD = {
    'Jancoyan': '123'
}


class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.resize(300, 100)

        # 在init函数中初始化控件并调用布局初始化等函数
        self.user_label = QLabel('UserName', self)
        self.pwd_label = QLabel('Password', self)
        self.user_line = QLineEdit(self)
        self.pwd_line = QLineEdit(self)
        self.log_in_button = QPushButton('Log in', self)
        self.sign_in_button = QPushButton('sign in', self)

        self.grid_layout = QGridLayout()
        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.line_edit_init()  # 行输入初始化
        self.push_button_init()  # 按钮初始化
        self.layout_init()  # 布局初始化
        self.sign_in_page = Sign_in_page()  # 注册页面

    def layout_init(self):
        # 初始化标签、输入等控件
        self.grid_layout.addWidget(self.user_label, 0, 0, 1, 1)
        self.grid_layout.addWidget(self.user_line, 0, 1, 1, 1)
        self.grid_layout.addWidget(self.pwd_label, 1, 0, 1, 1)
        self.grid_layout.addWidget(self.pwd_line, 1, 1, 1, 1)
        self.h_layout.addWidget(self.log_in_button)
        self.h_layout.addWidget(self.sign_in_button)
        self.v_layout.addLayout(self.grid_layout)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def line_edit_init(self):

        self.user_line.setPlaceholderText('Please enter your username')
        # 在用户没有输入任何文本的时候显示灰色默认文本
        self.pwd_line.setPlaceholderText('Please enter your password')
        self.pwd_line.setEchoMode(QLineEdit.Password)  # 让输入的密码显示黑色圆圈（保密）
        # 只有当上面下面两个框框都有文字的时候，登录按钮才可以点击
        self.user_line.textChanged.connect(self.check_input_func)
        self.pwd_line.textChanged.connect(self.check_input_func)

    def push_button_init(self):
        self.log_in_button.setEnabled(False)
        self.log_in_button.clicked.connect(self.check_login_func)  # 点击登录按钮
        self.sign_in_button.clicked.connect(self.show_sign_in_page_func)  # 点击注册按钮

    def check_login_func(self):
        if USER_PWD.get(self.user_line.text()) == self.pwd_line.text():
            # 在用户字典中查找账号和密码，并输出相应的信息
            QMessageBox.information(self, 'Information', 'Log in Successfully!')
        else:
            QMessageBox.critical(self, 'Wrong', 'Wrong Username or Password!')

        self.user_line.clear()
        self.pwd_line.clear()
        # 登录完成后清除相关的信息

    def show_sign_in_page_func(self):
        self.sign_in_page.exec_()

    def check_input_func(self):
        # 判断此时 LineEdit控件中是否存在文本
        if self.user_line.text() and self.pwd_line.text():
            self.log_in_button.setEnabled(True)  # 都有文本则可以使用登录按钮
        else:
            self.log_in_button.setEnabled(False)  # 否则，登录按钮不可用


class Sign_in_page(QDialog):
    def __init__(self):
        super(Sign_in_page, self).__init__()
        self.sign_in_user_label = QLabel('Username:', self)
        self.sign_in_pwd_label = QLabel('Password:', self)
        self.sign_in_pwd2_label = QLabel('Password:', self)
        self.sign_in_user_line = QLineEdit(self)
        self.sign_in_pwd_line = QLineEdit(self)
        self.sign_in_pwd2_line = QLineEdit(self)
        self.sign_in_button = QPushButton('Sign in', self)

        self.user_h_layout = QHBoxLayout()
        self.pwd_h_layout = QHBoxLayout()
        self.pwd2_h_layout = QHBoxLayout()
        self.all_v_layout = QVBoxLayout()

        self.lineedit_init()
        self.pushbutton_init()
        self.layout_init()

    def layout_init(self):
        self.user_h_layout.addWidget(self.sign_in_user_label)
        self.user_h_layout.addWidget(self.sign_in_user_line)
        self.pwd_h_layout.addWidget(self.sign_in_pwd_label)
        self.pwd_h_layout.addWidget(self.sign_in_pwd_line)
        self.pwd2_h_layout.addWidget(self.sign_in_pwd2_label)
        self.pwd2_h_layout.addWidget(self.sign_in_pwd2_line)

        self.all_v_layout.addLayout(self.user_h_layout)
        self.all_v_layout.addLayout(self.pwd_h_layout)
        self.all_v_layout.addLayout(self.pwd2_h_layout)
        self.all_v_layout.addWidget(self.sign_in_button)

        self.setLayout(self.all_v_layout)

    def lineedit_init(self):
        self.sign_in_pwd_line.setEchoMode(QLineEdit.Password)  # 输入后隐藏密码
        self.sign_in_pwd2_line.setEchoMode(QLineEdit.Password)

        # 将三个消息框与槽函数连接
        # 只有当三个文本框中都有内容的时候才能点击题交按钮
        self.sign_in_user_line.textChanged.connect(self.check_input_func)
        self.sign_in_pwd_line.textChanged.connect(self.check_input_func)
        self.sign_in_pwd2_line.textChanged.connect(self.check_input_func)

    def pushbutton_init(self):
        self.sign_in_button.setEnabled(False)  # 先把注册按钮关闭
        self.sign_in_button.clicked.connect(self.check_sign_in_func)

    def check_input_func(self):  # 三个条件同时满足才能完成注册
        if self.sign_in_user_line.text() and self.sign_in_pwd_line.text() and self.sign_in_pwd2_line.text():
            self.sign_in_button.setEnabled(True)
        else:
            self.sign_in_button.setEnabled(False)

    def check_sign_in_func(self):
        if self.sign_in_pwd_line.text() != self.sign_in_pwd2_line.text():
            QMessageBox.critical(self, 'Wrong', 'Two Passwords Typed Are Not Same!')
        elif self.sign_in_user_line.text() not in USER_PWD:  # 不在字典中
            USER_PWD[self.sign_in_user_line.text()] = self.sign_in_pwd_line.text()  # 向用户字典中添加这个用户
            QMessageBox.information(self, 'Information', 'Register Successfully')
            self.close()
        else:
            QMessageBox.critical(self, 'Wrong', 'This Username Has Been Registered!')

        self.sign_in_user_line.clear()
        self.sign_in_pwd_line.clear()
        self.sign_in_pwd2_line.clear()  # 注册完成后清空三个框框

```

## 第六章 文本编辑和浏览

左边为QTextEdit控件，右边为QTextBrowser控件。在左边输入文字时，右边会同步显示。

```python
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.edit_label = QLabel('TextEdit', self)
        self.browser_label = QLabel('QTextBrowser', self)
        self.text_edit = QTextEdit(self)  # 文本编辑框
        self.text_browser = QTextBrowser(self)  # 文本展示框

        self.edit_v_layout = QVBoxLayout()
        self.browser_v_layout = QVBoxLayout()
        self.all_h_layout = QHBoxLayout()

        self.layout_init()
        self.text_edit_init()

    def layout_init(self):
        self.edit_v_layout.addWidget(self.edit_label)
        self.edit_v_layout.addWidget(self.text_edit)

        self.browser_v_layout.addWidget(self.browser_label)
        self.browser_v_layout.addWidget(self.text_browser)

        self.all_h_layout.addLayout(self.edit_v_layout)
        self.all_h_layout.addLayout(self.browser_v_layout)

        self.setLayout(self.all_h_layout)

    def text_edit_init(self):
        self.text_edit.textChanged.connect(self.show_text_func)  # 文本发生改变的时候就会发出信号，调用show_text_func函数

    def show_text_func(self):
        self.text_browser.setText(self.text_edit.toPlainText())  # setText用来设置文本，toPlainText用来获取文本

```

## 第九章 滑动条和表盘



### 滑动条

```python

class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()
        self.slider_1 = QSlider(Qt.Horizontal, self)  # 传入Horizontal创建一个水平滑动条
        self.slider_1.setRange(0, 100)  # 可以用setRange设置滑块的范围

        # 如果不用lambda表达式，就不能传进去参数 self.slider_1 和 self.slider_2
        self.slider_1.valueChanged.connect(lambda: self.on_change_func(self.slider_1))

        self.slider_2 = QSlider(Qt.Vertical, self)
        self.slider_2.setMinimum(0)
        self.slider_2.setMaximum(100)  # 可以使用设置最大值和最小值的函数设置滑块的范围
        # slider数值改变触发函数
        self.slider_2.valueChanged.connect(lambda: self.on_change_func(self.slider_2))

        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))

        self.h_layout = QHBoxLayout()
        self.v_layout = QVBoxLayout()

        self.h_layout.addWidget(self.slider_2)
        self.h_layout.addStretch(1)
        self.h_layout.addWidget(self.label)
        self.h_layout.addStretch(1)
        # 两个addStretch确保数字显示在最中间

        self.v_layout.addWidget(self.slider_1)
        self.v_layout.addLayout(self.h_layout)

        self.setLayout(self.v_layout)

    def on_change_func(self, slider):
        # 对数值的变化做出反应
        if slider == self.slider_1:
            self.slider_2.setValue(self.slider_1.value())
            self.label.setText(str(self.slider_1.value()))
        else:
            self.slider_1.setValue(self.slider_2.value())
            self.label.setText(str(self.slider_2.value()))
```

### 表盘

```python
class Demo(QWidget):

    def __init__(self):
        super(Demo, self).__init__()

        self.dial = QDial(self)
        self.dial.setFixedSize(300, 300)  # 设置表盘的大小
        self.dial.setRange(0, 100)  # 表盘的范围
        self.dial.valueChanged.connect(self.on_change_func)  # 数值改变进行连接
        self.dial.setNotchesVisible(True)  # 显示刻度
        self.label = QLabel('0', self)
        self.label.setFont(QFont('Arial Black', 20))
        self.v_layout = QVBoxLayout()
        self.v_layout.addWidget(self.dial)
        self.v_layout.addWidget(self.label)
        self.setLayout(self.v_layout)

    def on_change_func(self):
        self.label.setText(str(self.dial.value()))
```



## 第十九章 列表控件、树形控件、表格控件

### 列表控件

```python
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.pic_label = QLabel(self)  # 用于显示图片
        self.pic_label.setPixmap(QPixmap('..\\img\\arrow.png'))

        self.list_widget_1 = QListWidget(self)  # list_widget_1放在左边用于显示可选的内容
        self.list_widget_2 = QListWidget(self)  # list_widget_2放在右边用于显示被双击的项

        self.list_widget_1.doubleClicked.connect(lambda: self.change_func(self.list_widget_1))  # doubleClicked 双击
        self.list_widget_2.doubleClicked.connect(lambda: self.change_func(self.list_widget_2))
        # 然后将这两个QListWidget控件的doubleClicked信号和自定义的槽函数连接起来，每当双击QListWidget中的某项时，就会触发该槽函数。

        for i in range(6):  # 循环创建六个QListWidgetItem，并通过调用addItem(QListWidgetItem)将其添加到list_widget_1中；
            text = 'Item {}'.format(i)
            self.item = QListWidgetItem(text)
            self.list_widget_1.addItem(self.item)

        self.item_6 = QListWidgetItem('Item 6', self.list_widget_1)  # 可以通过实例化时直接指定父类进行添加

        self.list_widget_1.addItem('Item 7')  # 也可以直接调用addItem添加内容
        str_list = ['Item 9', 'Item 10']
        self.list_widget_1.addItems(str_list)  # 也通过添加列表来添加内容

        self.item_8 = QListWidgetItem('Item 8')
        self.list_widget_1.insertItem(8, self.item_8)  # 通过 insertItem(row, QListWidget) 在指定行中加入一项内容
        # self.list_widget_1.insertItem(8, 'Item 8')

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.list_widget_1)
        self.h_layout.addWidget(self.pic_label)
        self.h_layout.addWidget(self.list_widget_2)
        self.setLayout(self.h_layout)

    def change_func(self, list_widget):  # 判断信号是哪一个QListWidget发出的
        if list_widget == self.list_widget_1:  # 如果时list_widget_1
            item = QListWidgetItem(self.list_widget_1.currentItem())  # 先用currentItem获取到当前项，实例化为QListWidgetItem
            self.list_widget_2.addItem(item)  # 再通过addItem(QListWidgetItem)方法加入list_widget_2中
            # print(self.list_widget_2.count()) 可以打印一下当前项目的数量
        else:  # 信号是list_widget_2发出的
            self.list_widget_2.takeItem(self.list_widget_2.currentRow())  # 将当前被双击项的行数传给takeItem(int)方法来进行删除
            print(self.list_widget_2.count())


"""
    注意:
    currentItem()的返回值是QListWidgetItem，照理来说应该是可以直接被添加的，也就是说下方这种写法应该也是可以的，但是却没有用：
    self.list_widget_2.addItem(self.list_widget_1.currentItem())
"""

```


### 树形控件

```python
class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.setGeometry(200, 200, 600, 400)
        self.label = QLabel('No Click')  # 用于显示每个QTreeWidgetItem文本

        self.tree = QTreeWidget(self)  # 树形控件
        self.tree.setColumnCount(2)  # 将树形控件的列数设置为 2（默认是 1）
        self.tree.setHeaderLabels(['Install Components', 'Test'])  # 设置每一列的标题（可以传入一个列表,也可以构造一个列表）
        # 如果只有一列的话，应该通过 setHeaderLabel(str) 设置
        self.tree.itemClicked.connect(self.change_func)  # 将 itemClicked信号连接到自定义槽函数
        # 每当点击QTreeWidget 中的任意一项的时候，都会触发这个信号

        self.preview = QTreeWidgetItem(self.tree)  # 实例化一个QTreeWidgetItem将其父类设置为 self.tree,表示其为最顶层项
        self.preview.setText(0, 'Preview')  # 通过setText() 设置文本，0表示第一列

        # self.preview = QTreeWidgetItem()
        # self.preview.setText(0, 'Preview')
        # self.tree.addTopLevelItem(self.preview)  # 使用这个方法可以设置最顶的层

        self.qt5112 = QTreeWidgetItem()
        self.qt5112.setText(0, 'Qt 5.11.2 snapshot')
        self.qt5112.setCheckState(0, Qt.Unchecked)  # 让这个项以复选框的形式呈现出来
        self.preview.addChild(self.qt5112)  # 为preview添加子项

        choice_list = ['macOS', 'Android x86', 'Android ARMv7', 'Sources', 'iOS']
        self.item_list = []
        for i, c in enumerate(choice_list):  # enumerate 返回枚举对象(1,'macOS')...
            item = QTreeWidgetItem(self.qt5112)
            item.setText(0, c)
            item.setCheckState(0, Qt.Unchecked)
            self.item_list.append(item)

        self.test_item = QTreeWidgetItem(self.qt5112)  # 构造函数的参数是其上一级
        self.test_item.setText(0, 'test1')  # 测试文本：在第一列显示test1
        self.test_item.setText(1, 'test2')  # 测试文本：在第二列显示test1

        self.tree.expandAll()  # 让QTreeWidget所有的项都是以打开状态显示的
        # 注意：要在所有项都已经实例化好之后再调用这个方法，如果一开始就调用则没有效果

        self.h_layout = QHBoxLayout()
        self.h_layout.addWidget(self.tree)
        self.h_layout.addWidget(self.label)
        self.setLayout(self.h_layout)

    def change_func(self, item, column):
        self.label.setText(item.text(column))  # 在槽函数中，self.label显示对应项的文本，item就是被点击的项
        # 调用text(int) 传入列数，获得文本

        # print(item.text(column))
        # print(column)

        if item == self.qt5112:  # 如果被点击的项目为 item，则我们判断它是否被选中
            # 如果是，将它的所有子项都设为选中状态，如果不是，就都设为未被选中状态

            if self.qt5112.checkState(0) == Qt.Checked:
                [x.setCheckState(0, Qt.Checked) for x in self.item_list]
            else:
                [x.setCheckState(0, Qt.Unchecked) for x in self.item_list]
        else:
            # 如果被点击的是qt5112的子项，我们判断有多少个子项被选中了
            # 若数量为5，则设置qt5112为选中状态，若为0-5之间，则设为半选中状态，若等于0，则设为无选中状态。
            check_count = 0
            for x in self.item_list:
                if x.checkState(0) == Qt.Checked:
                    check_count += 1

            if check_count == 5:
                self.qt5112.setCheckState(0, Qt.Checked)
            elif 0 < check_count < 5:
                self.qt5112.setCheckState(0, Qt.PartiallyChecked)
            else:
                self.qt5112.setCheckState(0, Qt.Unchecked)

```


### 表格控件



```python
class Demo(QTableWidget):  # 直接继承 QTableWidget
    def __init__(self):
        super(Demo, self).__init__()

        self.setRowCount(6)  # 设置表格的行数
        self.setColumnCount(6)  # 设置表格的列数

        # self.table = QTableWidget(6, 6, self)  也可以在实例化的时候直接指定列数

        print(self.rowCount())  # 获取行数
        print(self.columnCount())  # 获取列数

        self.setColumnWidth(0, 30)  # 设置列宽，setColumnWidth(列序号，宽度值)
        self.setRowHeight(0, 30)  # 设置行高 (行号，高度值)

        self.setHorizontalHeaderLabels(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])  # 行标题
        self.setVerticalHeaderLabels(['t1', 't2', 't3', 't4', 't5', 't6'])  # 列标题

        # self.setShowGrid(False)  # 是否显示网格线

        self.item_1 = QTableWidgetItem('Hi')
        self.setItem(0, 0, self.item_1)

        self.item_2 = QTableWidgetItem('Bye')
        self.item_2.setTextAlignment(Qt.AlignCenter)  # 文本对齐方式
        self.setItem(2, 2, self.item_2)

        self.setSpan(2, 2, 2, 2)   # 合并单元格，setSpan(行序号，列序号，合并的行数，合并的列数)

        print(self.findItems('Hi', Qt.MatchExactly))  # 查找，精确匹配
        print(self.findItems('B', Qt.MatchContains))  # 查找，包含匹配

```

## 第二十章 列表视图、树形视图、表格视图

### 列表视图





### 属性视图





### 表格视图





## 第二十四章 更多控件

### 拆分窗口

```python
class Demo(QSplitter):  # 继承QSplitter

    def __init__(self):
        super(Demo, self).__init__()

        self.dir_model = QDirModel(self)  # 实例化 QDirMode 模型

        self.list_view = QListView(self)  # 分别实例化三个模型
        self.tree_view = QTreeView(self)
        self.table_view = QTableView(self)

        self.list_view.setModel(self.dir_model)  # 将这三个视图的模型设置为 dir_model
        self.tree_view.setModel(self.dir_model)
        self.table_view.setModel(self.dir_model)

        self.tree_view.doubleClicked.connect(self.show_func)  # 将双击的信号与show_func连接起来
        # 当被双击时，被双击项的索引会保存在index中，而这个参数会传给槽函数

        # 拆分窗口默认时水平的，我们可以用下面这句话将其编程垂直的。
        # self.setOrientation(Qt.Vertical)
        self.addWidget(self.list_view)
        self.addWidget(self.tree_view)

        self.insertWidget(0, self.table_view)  # 插入控件，insertWidget(int,widget)第一个是要插入的索引位置，第二个是控件
        self.setSizes([300, 200, 200])  # 设置各个子控件的宽度（垂直就是高度）
        # print(self.count())  # 拆分窗口中控件的数量

    def show_func(self, index):
        # 在槽函数中我们调用setRootIndex()并传入index值，
        # 也就是说，每当我们双击QTreeView中的某项时，
        # QListView和QTableView就会将该项的索引设为自身的根索引，并显示相应的目录结构；
        self.list_view.setRootIndex(index)
        self.table_view.setRootIndex(index)
```

### 标签页窗口

```python
class Demo(QTabWidget):  # 继承QTabWidget

    def __init__(self):
        super(Demo, self).__init__()

        self.tab1 = QWidget()
        self.tab2 = QWidget()  # 前两个为QWidget
        self.tab3 = QTextEdit()  # 第三个控件为TextEdit

        self.tab1_init()  # 向 self.tab1 中添加控件，完成布局
        self.tab2_init()  # 向 self.tab1 中添加控件，完成布局

        self.addTab(self.tab1, 'Basic Info')  # addTab(widget对象, 标题)
        self.addTab(self.tab2, 'Contact Info')
        self.addTab(self.tab3, 'More Info')
        # self.addTab(self.tab1, QIcon('icon.ico'), 'More info')  # 也可以设置标签的图标

        # self.currentChanged.connect(lambda: print(self.currentIndex()))
        # 用户点击tab标签的时候，打印输出用户点击的标签的索引

    def tab1_init(self):
        name_label = QLabel('Name:', self.tab1)
        gender_label = QLabel('Gender', self.tab1)
        bd_label = QLabel('Birth Date', self.tab1)

        name_line = QLineEdit(self.tab1)
        items = ['Please choose your gender', 'Female', 'Male']
        gender_combo = QComboBox(self.tab1)
        gender_combo.addItems(items)
        bd_date_edit = QDateEdit(self.tab1)

        g_layout = QGridLayout()
        g_layout.addWidget(name_label, 0, 0, 1, 1)
        g_layout.addWidget(name_line, 0, 1, 1, 1)
        g_layout.addWidget(gender_label, 2, 0, 1, 1)
        g_layout.addWidget(gender_combo, 2, 1, 1, 1)
        g_layout.addWidget(bd_label, 3, 0, 1, 1)
        g_layout.addWidget(bd_date_edit, 3, 1, 1, 1)

        self.tab1.setLayout(g_layout)

    def tab2_init(self):
        tel_label = QLabel('Tel:', self.tab2)
        mobile_label = QLabel('Mobile:', self.tab2)
        add_label = QLabel('Address:', self.tab2)

        tel_line = QLineEdit(self.tab2)
        mobile_line = QLineEdit(self.tab2)
        add_line = QLineEdit(self.tab2)

        g_layout = QGridLayout()
        g_layout.addWidget(tel_label, 0, 0, 1, 1)
        g_layout.addWidget(tel_line, 0, 1, 1, 1)
        g_layout.addWidget(mobile_label, 1, 0, 1, 1)
        g_layout.addWidget(mobile_line, 1, 1, 1, 1)
        g_layout.addWidget(add_label, 2, 0, 1, 1)
        g_layout.addWidget(add_line, 2, 1, 1, 1)

        self.tab2.setLayout(g_layout)
```

### 堆叠窗口

QStackedWidget用法跟QTabWdidget用法思想相似，只是界面样式不同。我们经常将QStackedWidget和QListWidget或者QListView搭配使用

```python

```

### 停靠窗口

```python

```

### 多文档界面

```python

```





# Qt



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