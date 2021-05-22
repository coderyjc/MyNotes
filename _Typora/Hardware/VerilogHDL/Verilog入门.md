# Verilog入门


## 1  概述

用于数字逻辑电路设计的描述语言；

用Verilog HDL描述的电路设计就是该电路的verilog HDL模型。

Verilog HDL 既是一种行为描述的语言也是一种结构描述的语言。

一个复杂电路的完整Verilog HDL模型是由若干个Verilog HDL 模块构成的，每一个模块又可以由若干个子模块构成。

Verilog模型可以是实际电路的不同级别的抽象。这些抽象的级别和它们对应的模型类型共有以下五种：

- 系统级(system)
- 算法级(algorithmic) 
- 寄存器级(Register Transfer Level)
- 门级(gate-level) 
- 开关级(switch-level)

## 2  Verilog HDL基本结构

Verilog的基本设计单元是“模块 (block) ” 。

Verilog 模块的结构由在module和endmodule关键词之间的4个主要部分组成：

```verilog
module block1(a,b,c,d )； // 端口定义
  input a,b,c； // IO说明
  output d；
  wire x； // 信号类型说明
  assign d = a | x；  // 功能描述
  assign x = ( b & ~c )；
endmodule
```



数据类型：

- 输入口（input）可以由寄存器或网络连接驱动，但它本身只能驱动网络连接。

- 输出口 (output)可以由寄存器或网络连接驱动，但它本身只能驱动网络连接。

- 输入/输出口(inout)只可以由网络连接驱动，但它本身只能驱动网络连接。

**例化**

```verilog
...
	< module_name > < instance_name > (<port_list>);        // 模块元件例化
    <gate_type_keyword> < instance_name > (<port_list>); // 门元件例化
endmodule // 例化元件名可以省略
```

在一个模块中引用另一个模块，对其端口进行相关连接，叫做模块例化。模块例化建立了描述的层次。信号端口可以通过位置或名称关联，端口连接也必须遵循一些规则。

## 3  常量、变量



## 4  运算符及表达式



## 5  语句



## 6  赋值语句和块语句



## 7  条件语句



## 8  循环语句



## 9  结构说明语句



## 10 编译预处理语句



## 11 语句的顺序执行与并行执行



## 12 不同抽象级别的Verilog HDL模型

