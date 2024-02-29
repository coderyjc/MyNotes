## C语言-程序流程结构

### 概述

C语言支持最基本的三种程序运行结构：顺序结构、选择结构、循环结构。

- 顺序结构：程序按顺序执行，不发生跳转。

- 选择结构：依据是否满足条件，有选择的执行相应功能。

- 循环结构：依据条件是否满足，循环多次执行某段代码。

### 选择结构

#### if语句

![[clip_image002-1600565899951.png]]

```c
#include <stdio.h>

int main()
{
	int a = 1;
	int b = 2;

	if (a > b)
	{
		printf("%d\n", a);
	}

	return 0;
} 
```

#### if…else语句

![[clip_image002-1600565955370.png]]

```c
#include <stdio.h>
int main()
{
	int a = 1;
	int b = 2;

	if (a > b)
	{
		printf("%d\n", a);
	}
	else
	{
		printf("%d\n", b);
	}
	return 0;
}

```

#### if…else if…else语句

![[clip_image002-1600565985028.png]]

```c
#include <stdio.h>

int main()
{
	unsigned int a;
	scanf("%u", &a);

	if (a < 10)
	{
		printf("个位\n");
	}
	else if (a < 100)
	{
		printf("十位\n");
	}
	else if (a < 1000)
	{
		printf("百位\n");
	}
	else
	{
		printf("很大\n");
	}

	return 0;
}
```

#### 三目运算符

![[2-1Q11512525J14.gif]]

```c
#include <stdio.h>

int main()
{
	int a = 10;
	int b = 20;
	int c;

	if (a > b)
	{
		c = a;
	}
	else
	{
		c = b;
	}
	printf("c1 = %d\n", c);

	a = 1;
	b = 2;
	c = ( a > b ? a : b );
	printf("c2 = %d\n", c);

	return 0;
}

```

#### switch语句

```c
#include <stdio.h>

int main()
{
	char c;
	c = getchar();

	switch (c) //参数只能是整型变量
	{
	case '1':
		printf("OK\n");
		break;//switch遇到break就中断了
	case '2':
		printf("not OK\n");
		break;
	default://如果上面的条件都不满足，那么执行default
		printf("are u ok?\n");
	}
	return 0;
}
```

输出结果：

```bash
tao@Taoc:~/Desktop/C/4$ ./4.2.5 
t
are u ok?
```

### 循环语句

#### while语句

![[clip_image002-1600566360348.png]]

```c
#include <stdio.h>

int main()
{
	int a = 20;
	while (a > 10)
	{
		scanf("%d", &a);
		printf("a = %d\n", a);
	}

	return 0;
}
```

#### do…while语句

![[clip_image002-1600566398556.png]]

```c
#include <stdio.h>

int main()
{
	int a = 1;
	do
	{
		a++;
		printf("a = %d\n", a);
	} while (a < 10);

	return 0;
}

```

#### for 语句

```c
#include <stdio.h>

int main()
{
	int i;
	int sum = 0;
	for (i = 0; i <= 100; i++)
	{
		sum += i;

	}

	printf("sum = %d\n", sum);

	return 0;
}
```

#### 嵌套循环

```c
#include <stdio.h>

int main()
{
	int num = 0;
	int i, j, k;
	for (i = 0; i < 10; i++)
	{
		for (j = 0; j < 10; j++)
		{
			for (k = 0; k < 10; k++)
			{
				printf("hello world\n");
				num++;
			}
		}
	}

	printf("num = %d\n", num);

	return 0;
}

```

### 跳转语句break、continue、goto

#### break 语句

在switch条件语句和循环语句中都可以使用`break`语句：

- 当它出现在`switch`条件语句中时，作用是终止某个`case`并跳出`switch`结构。
- 当它出现在循环语句中，作用是跳出当前内循环语句，执行后面的代码。
- 当它出现在嵌套循环语句中，跳出最近的内循环语句，执行后面的代码

```bash
#include <stdio.h>

int main()
{
	int i = 0;
	while (1)
	{
		i++;
		printf("i = %d\n", i);

		if (i == 10)
		{
			break; //跳出while循环
		}
	}

	int flag = 0;
	int m = 0;
	int n = 0;

	for (m = 0; m < 10; m++)
	{
		for (n = 0; n < 10; n++)
		{
			if (n == 5)
			{
				flag = 1;
				break; //跳出for (n = 0; n < 10; n++)
			}
		}

		if (flag == 1)
		{
			break; //跳出for (m = 0; m < 10; m++)
		}
	}

	return 0;
}
```

输出结果：

```bash
tao@Taoc:~/Desktop/C/4$ ./4.3.1
i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
i = 7
i = 8
i = 9
i = 10
```

#### continue语句

在循环语句中，如果希望立即终止本次循环，并执行下一次循环，此时就需要使用`continue`语句

```c
#include<stdio.h>

int main()
{
	int sum = 0;           //定义变量sum

	for (int i = 1; i <= 100; i++)
	{
		if (i % 2 == 0)   //如果i是一个偶数，执行if语句中的代码
		{
			continue;      //结束本次循环
		}
		sum += i;          //实现sum和i的累加
	}

	printf("sum = %d\n", sum);

	return 0;
}
```

```bash
tao@Taoc:~/Desktop/C/4$ ./4.4.2
sum = 2500
```

#### goto语句(无条件跳转，尽量少用)

```c
#include <stdio.h>

int main()
{
	goto End; //无条件跳转到End的标识
	printf("aaaaaaaaa\n");

End:
	printf("bbbbbbbb\n");

	return 0;
}
```

输出结果：

```c
tao@Taoc:~/Desktop/C/4$ ./4.4.3 
bbbbbbbb
```
