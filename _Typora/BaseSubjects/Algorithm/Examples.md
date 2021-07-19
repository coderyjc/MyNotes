## 蛇形填数

蛇形填数。在n×n方阵里填入1，2，…，n×n，要求填成蛇形。例如，n＝4时方阵为：
10 11 12 1
9 16 13 2
8 15 14 3
7 6 5 4
上面的方阵中，多余的空格只是为了便于观察规律，不必严格输出。n≤8。

### 解析

从1开始依次填写。设“笔”的坐标为（x,y），则一开始x=0，y=n-1，即第0行，第n-1列（行列的范围是0～n-1，没有第n列）。“笔”的移动轨迹是：下，下，下，左，左，左，上，上，上，右，右，下，下，左，上。总之，先是下，到不能填为止，然后是左，接着是上，最后是右。“不能填”是指再走就出界（例如4→5），或者再走就要走到以前填过的格子（例如12→13）。如果把所有格子初始化为0，就能很方便地加以判断。


```c++
#include<iostream>
using namespace std;

const int maxn = 20;
int a[maxn][maxn];

int main(){
	int n, x, y, tot = 0;
	cin >> n;
	tot = a[x = 0][y = n - 1] = 1;
	while(tot < n * n){
		while(x + 1 < n && !a[x + 1][y]) a[++x][y] = ++tot;
		while(y - 1 >= 0 && !a[x][y - 1]) a[x][--y] = ++tot;
		while(x - 1 >= 0 && !a[x - 1][y]) a[--x][y] = ++tot;
		while(y + 1 < n && !a[x][y + 1]) a[x][++y] = ++tot;
	}
	for(x = 0; x < n; x++){
		for (y = 0; y < n; y++)
			cout << a[x][y];
		cout << endl;
	}
	return 0;
}
```



## 竖式输出

文本处理在计算机应用中占有重要地位。本书到现在为止还没有正式讨论过字符串（尽
管曾经使用过），因为在C语言中，字符串其实就是字符数组——可以像处理普通数组一样
处理字符串，只需要注意输入输出和字符串函数的使用。
竖式问题。找出所有形如abc*de（三位数乘以两位数）的算式，使得在完整的竖式中，
所有数字都属于一个特定的数字集合。输入数字集合（相邻数字之间没有空格），输出所有
竖式。每个竖式前应有编号，之后应有一个空行。最后输出解的总数。具体格式见样例输出
（为了便于观察，竖式中的空格改用小数点显示，但所写程序中应该输出空格，而非小数
点）。
样例输入：
2357
样例输出：
 ![P3-4](D:\Algorithm\img\P3-4.jpg)



```c++
#include<cstdio>
#include<cstring>
using namespace std;
int main()
{
	int count = 0;
	char s[20], buf[99];
	scanf("%s", s);
	for(int abc = 111; abc <= 999; abc++)
		for(int de = 11; de <= 99; de++){
			int x = abc*(de%10), y = abc*(de/10), z = abc*de;
			sprintf(buf, "%d%d%d%d%d", abc, de, x, y, z);  
            // output to a string
			int ok = 1;
			for(int i = 0; i < strlen(buf); i++)
				if (strchr(s, buf[i]) == NULL) 
                    // strchr() -> find buf[i] in s, return its position
					ok = 0;
			if(ok){
				printf("<%d>\n", ++count);
				printf("%5d\nX%4d\n----\n%5d\n%4d\n-----\n%5d\n\n", abc, de, x, y, z);
				break;
			}
		}
	printf("The number of solutions = %d\n", count);
	return 0;
}
```



## 生成元

如果x加上x的各个数字之和得到y，就说x是y的生成元。给出n（1≤n≤100000），求最小
生成元。无解输出0。例如，n=216，121，2005时的解分别为198，0，1979。

### 解析

本题看起来是个数学题，实则不然。假设所求生成元为m。不难发现m<n。换句话说，只需枚举所有的m<n，看看有没有哪个数是n的生成元。可惜这样做的效率并不高，因为每次计算一个n的生成元都需要枚举n-1个数。有没有更快的方法？聪明的读者也许已经想到了：只需一次性枚举100000内的所有正整数m，标记“m加上m的各个数字之和得到的数有一个生成元是m”，最后查表即可。

```c++
#include<iostream>
using namespace std;
int main()
{
	const int maxn = 100000 + 5;
	int num[maxn];
	for(int i = 0; i < maxn; i++) num[i] = 0;
	for(int i = 0; i < maxn; i++){
		int x = i, y = i;
		while(x > 0){
			y += x % 10;
			x /= 10;
	}
		if(num[y] == 0 || i < num[y])
			num[y] = i;
	}
	int n;
	cin >> n;
	cout << num[n] << endl;
	return 0;
}
```



## 分子量

给出一种物质的分子式（不带括号），求分子量。本题中的分子式只包含4种原子，分
别为C, H, O, N，原子量分别为12.01, 1.008, 16.00, 14.01（单位：g/mol）。例如，C6H5OH的
分子量为94.108g/mol。

```c++
#include<iostream>
#include<ctype.h>
using namespace std;
const int MAXN = 10000 + 5;
int main(){
	double ele[126];
	ele['C'] = 12.01;
	ele['H'] = 1.008;
	ele['N'] = 14.01;
	ele['O'] = 16.00;
	char str[MAXN];
	double rst = 0;
	cin >> str;
	double tempm = 0, num = 0;
	for(int i = 0; str[i]; i++){
		if(isalpha(str[i])){
			tempm = ele[str[i]];
			if(isdigit(str[i + 1]) && isdigit(str[i + 2]))
				num = (str[i + 1] - '0') * 10 + str[i + 2] - '0';
			else if(isdigit(str[i + 1]))
				num = str[i + 1] - '0';
			else num = 1;
			rst += tempm * num;
			tempm = 0;
			num = 0;
		}	
	}
	cout << rst;
	return 0;
}
```



## 周期串

如果一个字符串可以由某个长度为k的字符串重复多次得到，则称该串以k为周期。例如，abcabcabcabc以3为周期（注意，它也以6和12为周期）。输入一个长度不超过80的字符串，输出其最小周期。

```c++
#include<iostream> 
#include <string>
using namespace std;
int main()
{
    string str;
    cin >> str;
    int rst;
    for(rst = 1; rst < str.length(); rst++)
    {
    	if(str.length() % rst) continue; //不能整除，不能切割
    	int flag = 1;
    	for(int i = 1; i < str.length()/rst; i++){
    		if( str.substr(0, rst) != str.substr(rst * i, rst)) //切割比对
    			flag = 0;
			if(flag == 0) break;
		}
		if(flag == 1) break;
	} 
	cout << rst;
    return 0;
}
```

## 素数判定

```c++
int is_prime(int n)
{
	if(n <= 1) return 0;
	int m = floor(sqrt(n) + 0.5);
	for(int i = 2; i <= m; i++)
	if(n % i == 0) return 0;
	return 1;
}
```

## 刽子手游戏

刽子手游戏其实是一款猜单词游戏，游戏规则是这样的：计算机想一个单词让你猜，你每次可以猜一个字母。如果单词里有那个字母，所有该字母会显示出来；如果没有那个字母，则计算机会在一幅“刽子手”画上填一笔。这幅画一共需要7笔就能完成，因此你最多只能错6次。注意，猜一个已经猜过的字母也算错。
在本题中，你的任务是编写一个“裁判”程序，输入单词和玩家的猜测，判断玩家赢了（You win.）、输了（You lose.）还是放弃了（You chickened out.）。每组数据包含3行，第1行是游戏编号（-1为输入结束标记），第2行是计算机想的单词，第3行是玩家的猜测。后两行保证只含小写字母。

样例输入

1
cheese
chese
2
cheese
acdefg
3
cheese
abcdefgij

样例输出

Round 1
You win.
Round2
You chickened out.
Round 3
You lose.

```C++
#include<iostream>
using namespace std;

string s, s2;
int win, lose;
int rest, chance;

int main() {
	int rnd = 1;
	while (1) {
		cin >> rnd >> s >> s2;
		if(rnd == -1) return 0;
		cout << "Round " << rnd << endl;
		win = lose = 0;
		rest = s.length();
		chance = 7;
		for (int i = 0; i < s2.length(); i++) {
			int bad = 1;
			for (int j = 0; j < s.length(); i++)
				if (s[j] == s2[i]) {
					rest--;
					s[j] = ' ';
					bad = 0;
				}
			if (bad) --chance;
			if (!chance) lose = 1;
			if (!rest) win = 1;
			if (win || lose) break;
		}
		if (win) cout << "You win." << endl;
		else if (lose) cout << "You lose." << endl;
		else cout << "You chickened out" << endl;
	}
	return 0;
}
```

## 救济金发放

n(n<20)个人站成一圈，逆时针编号为1～n。有两个官员，A从1开始逆时针数，B从n开
始顺时针数。在每一轮中，官员A数k个就停下来，官员B数m个就停下来（注意有可能两个
官员停在同一个人上）。接下来被官员选中的人（1个或者2个）离开队伍。
输入n，k，m输出每轮里被选中的人的编号（如果有两个人，先输出被A选中的）。例
如，n=10，k=4，m=3，输出为4 8, 9 5, 3 1, 2 6, 10, 7。注意：输出的每个数应当恰好占3列。


```c++
#include<cstdio>
#define maxn 25
using namespace std;

int n, k, m, a[maxn];

int go(int p, int d, int t){
	while(t--){
		do{
			p = (p + d + n - 1) % n + 1;  
			printf("p = %d\n", p);
		}while(a[p] == 0);
	}
	printf("\n");
	return p;
}

int main(){
	while(scanf("%d%d%d", &n, &k, &m) == 3 && n){
		for(int i = 1; i <= n; i++) a[i] = i;
		int rest = n;
		int p1 = n, p2 = 1;
		while(rest){
			p1 = go(p1, 1, k);
			p2 = go(p2, -1, m);
			printf("%3d", p1); rest--;
			if(p2 != p1) {printf("%3d", p2); rest--;}
			a[p1] = a[p2] = 0;
			if(rest) printf(",");
		}
		printf("\n");
	}
	return 0;
}
```

