# Java_Swing_Awt

## 布局管理

```java
    public static void main(String[] args) {
        // 1.创建顶层容器
        JFrame jf = new JFrame("Test Windows"); //创建顶层窗口
        jf.setSize(250, 250); //设置窗口大小
        jf.setLocationRelativeTo(null); //把窗口放到屏幕中心

        jf.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE); //当点击窗口的关闭按钮时退出程序
        // 没有这一句，程序不会退出

        //2. 创建中间容器
        JPanel panel = new JPanel(); //创建面板容器

        //3.创建一个基本组件（按钮），并添加到面板容器中
        JButton btn = new JButton("TEST");
        panel.add(btn);

        //4. 把面板容器作为窗口的内容面板设置到窗口
        jf.setContentPane(panel);

        //5. 显示窗口，前面创建的信息都再内存中，要通过这一句话把内存中的窗口显示到屏幕上
        jf.setVisible(true);
    }
```

### 1.1: FlowLayout（流式布局）

FlowLayout，流式布局管理器。按水平方向依次排列放置组件，排满一行，换下一行继续排列。排列方向（左到右 或 右到左）取决于容器的componentOrientation属性（该属性属于Component），它可能的值如下:

- ComponentOrientation.LEFT_TO_RIGHT（默认）
- ComponentOrientation.RIGHT_TO_LEFT

同一行（水平方向）的组件的对齐方式由 FlowLayout 的align属性确定，它可能的值如下:

- FlowLayout.LEFT : 左对齐
- FlowLayout.CENTER : 居中对齐（默认）
- FlowLayout.RIGHT : 右对齐
- FlowLayout.LEADING : 与容器方向的开始边对齐，例如，对于从左到右的方向，则与左边对齐
- FlowLayout.TRAILING : 与容器方向的结束边对齐，例如，对于从左到右的方向，则与右边对齐。

FlowLayout的 构造方法:
```java
// 默认 居中对齐的，水平和垂直间隙是 5 个单位
FlowLayout()

// 指定对齐方式，默认的水平和垂直间隙是 5 个单位
FlowLayout(int align)

// 指定对其方式，水平 和 竖直 间隙
FlowLayout(int align, int hgap, int vgap)
```

测试：

```java
    public static void main(String[] args) {
        JFrame jf = new JFrame("Test");
        jf.setSize(250, 250);
        jf.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        jf.setLocationRelativeTo(null);

        //JPanel jp = new JPanel(new FlowLayout()); 默认对齐方式

        FlowLayout fl = new FlowLayout();
        fl.setAlignment(FlowLayout.RIGHT); // 设置对齐方式
        JPanel jp = new JPanel(fl); //在容器这里将排版参数传进去。

        JButton btn1 = new JButton("Btn1");
        JButton btn2 = new JButton("Btn2");
        JButton btn3 = new JButton("Btn3");
        JButton btn4 = new JButton("Btn4");
        jp.add(btn1);
        jp.add(btn2);
        jp.add(btn3);
        jp.add(btn4);

        jf.setContentPane(jp);
        jf.setVisible(true);
    }
```

### 1.2: GridLayout（网格布局）

GridLayout，网格布局管理器。它以矩形网格形式对容器的组件进行布置，把容器按行列分成大小相等的矩形网格，一个网格中放置一个组件，**组件宽高自动撑满网格**。

以行数和总数优先: 通过构造方法或 setRows 和 setColumns 方法将行数和列数都设置为非零值时，指定的列数将被忽略。列数通过指定的行数和布局中的组件总数来确定。

因此，例如，如果指定了三行和两列，在布局中添加了九个组件，则它们将显示为三行三列。仅当将行数设置为零时，指定列数才对布局有效。

GridLayout构造方法:
```java
// 默认构造, 每个组件占据一行一列
GridLayout()

// 指定 行数 和 列数 的网格布局
GridLayout(int rows, int cols)

// 指定 行数 和 列数 的网格布局, 并指定 水平 和 竖直 网格间隙
GridLayout(int rows, int cols, int hgap, int vgap)
```

例子

```java
    public static void main(String[] args) {
        JFrame jf = new JFrame("GridTest");
        jf.setSize(300, 300);
        jf.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        jf.setLocationRelativeTo(null);

        JPanel jp = new JPanel(new GridLayout(3, 3)); //初始化一个三行三列的容器

        JButton[] btn = new JButton[9]; //创建了9个按钮
        String text = "Button";
        for(int i = 0; i < 9; i++){
            btn[i] = new JButton(text + i);
            jp.add(btn[i]); //添加进容器
        }
        jf.setContentPane(jp);
        jf.setVisible(true);
    }
```



### 1.9: null（绝对布局）

## JavaSwing相关特性

### 5.3：事件处理

动作监听器 ActionListener

```java

final String COMMAND_OK = "OK";
final String COMMAND_CANCEL = "Cancel";

JButton okBtn = new JButton("OK");
okBtn.setActionCommand(COMMAND_OK);             // 按钮绑定动作命令

JButton cancelBtn = new JButton("Cancel");
cancelBtn.setActionCommand(COMMAND_CANCEL);     // 按钮绑定动作命令

// 创建一个动作监听器实例
ActionListener listener = new ActionListener() {
    @Override
    public void actionPerformed(ActionEvent e) {
        // 获取事件源，即触发事件的组件（按钮）本身
        // e.getSource();
    
        // 获取动作命令
        String command = e.getActionCommand();
        
        // 根据动作命令区分被点击的按钮
        if (COMMAND_OK.equals(command)) {
            System.out.println("OK 按钮被点击");
            
        } else if (COMMAND_CANCEL.equals(command)) {
            System.out.println("Cancel 按钮被点击");
        }
    }
};

// 设置两个按钮的动作监听器（使用同一个监听器实例）
okBtn.addActionListener(listener);
cancelBtn.addActionListener(listener);

```

焦点监听器

```java
JButton btn = new JButton("OK");
btn.addFocusListener(new FocusListener() {
    @Override
    public void focusGained(FocusEvent e) {
        System.out.println("获得焦点: " + e.getSource());
    }
    @Override
    public void focusLost(FocusEvent e) {
        System.out.println("失去焦点: " + e.getSource());
    }
});

JTextField textField = new JTextField(10);
textField.addFocusListener(new FocusListener() {
    @Override
    public void focusGained(FocusEvent e) {
        System.out.println("获得焦点: " + e.getSource());
    }
    @Override
    public void focusLost(FocusEvent e) {
        System.out.println("失去焦点: " + e.getSource());
    }
});
```

鼠标监听器

```java
JPanel panel = new JPanel();

panel.addMouseListener(new MouseListener() {
    @Override
    public void mouseEntered(MouseEvent e) {
        System.out.println("鼠标进入组件区域");
    }

    @Override
    public void mouseExited(MouseEvent e) {
        System.out.println("鼠标离开组建区域");
    }

    @Override
    public void mousePressed(MouseEvent e) {
        // 获取按下的坐标（相对于组件）
        e.getPoint();
        e.getX();
        e.getY();

        // 获取按下的坐标（相对于屏幕）
        e.getLocationOnScreen();
        e.getXOnScreen();
        e.getYOnScreen();

        // 判断按下的是否是鼠标右键
        e.isMetaDown();

        System.out.println("鼠标按下");
    }

    @Override
    public void mouseReleased(MouseEvent e) {
        System.out.println("鼠标释放");
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        // 鼠标在组件区域内按下并释放（中间没有移动光标）才识别为被点击
        System.out.println("鼠标点击");
    }
});

```

键盘监听器

```java
JFrame jf = new JFrame();

jf.addKeyListener(new KeyListener() {
    @Override
    public void keyPressed(KeyEvent e) {
        // 获取键值，和 KeyEvent.VK_XXXX 常量比较确定所按下的按键
        int keyCode = e.getKeyCode();
        System.out.println("按下: " + e.getKeyCode());
    }
    
    @Override
    public void keyTyped(KeyEvent e) {
        // e.getKeyChar() 获取键入的字符
        System.out.println("键入: " + e.getKeyChar());
    }
    
    @Override
    public void keyReleased(KeyEvent e) {
        System.out.println("释放: " + e.getKeyCode());
    }
});

```