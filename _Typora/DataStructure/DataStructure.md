## 线性表

### 线性表的顺序实现

#### Header.h

```C
#pragma once

#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<time.h>

#define TRUE 1
#define FALSE 0
#define OK 1
#define ERROR 0
#define INFEASIBLE -1
#define OVERFLOW -2

typedef int Status;

typedef int ElemType;
```

###  main.h

```c
#include"Header.h"

// 线性表的顺序实现

#define MAXSIZE 100 //顺序表能达到的最大长度

typedef struct  {
	ElemType* elem;
	int length;
}SqList;


Status InitList(SqList& L) {
	//构造一个空的线性表
	L.length = 0;
	L.elem = (ElemType*)calloc(MAXSIZE, sizeof(SqList));
	// L.elem = new ElemType[100];
	return OK;
}

//---------------------以下所有操作的前提是线性表已存在

Status DestoryList(SqList& L) {
	//销毁线性表
	if (L.elem != NULL) free(L.elem);
	L.length = 0;
	return OK;
}


Status ClearList(SqList& L) {
	//将 L 重置为空表
	if (L.elem == NULL) return ERROR;
	L.length = 0;
	return OK;
}

bool ListEmpty(SqList& L) {
	//判断是否为空，空为1
	if (L.elem == NULL) return ERROR;
	return L.length ? false : true;
}

Status ListLength(SqList& L) {
	if (L.elem == NULL) return ERROR;
	//返回线性表的长度
	return L.length;
}

Status GetElem(SqList& L, int i, ElemType& e) {
	//用 e 返回第i个元素, 下标从 1 开始
	if (L.elem == NULL || i > L.length || i <= 0) return ERROR;
	e = L.elem[i - 1];
	return OK;
}

int LocateElem(SqList& L, ElemType e) {
	//返回第一个与e相等的元素的[序号]
	if (L.elem == NULL) return ERROR;
	for (int i = 0; i < L.length; i++) {
		if (L.elem[i] == e) {
			return i;
		}
	}
	return -1;
}

Status PriorElem(SqList& L, ElemType cur_e, ElemType& pre_e) {
	//若cur-e是L的数据元素且不是第一个元素，返回其前驱
	int pos = 0;
	for (pos = 0; pos < L.length; pos++) {
		if (L.elem[pos] == cur_e)
			break;
	}
	if (pos == 0) return ERROR;
	pre_e = L.elem[pos - 1];
	return OK;
}

Status NextElem(SqList& L, ElemType cur_e, ElemType& next_e) {
	//若cur-e不是L的数据元素且不是第一个元素，返回其后继
	int pos = 0;
	for (pos = 0; pos < L.length; pos++) {
		if (L.elem[pos] == cur_e)
			break;
	}
	if (pos == L.length - 1) return ERROR;
	next_e = L.elem[pos + 1];
	return OK;
}

Status ListInsert(SqList& L, int i, ElemType e) {
	//插入元素
	if (L.length + 1 >= 100) return ERROR;
	for (int j = L.length; j >= i; j--) {
		L.elem[j] = L.elem[j - 1];
	}
	L.elem[i - 1] = e;
	L.length++;
	return OK;
}

Status ListDelete(SqList& L, int i, ElemType& e) {
	//删除第i个元素并用e返回其值
	if (i <= 0 || i >= L.length) return ERROR;
	e = L.elem[i - 1];
	for (int j = i; j < L.length; j++)
		L.elem[j - 1] = L.elem[j];
	L.length--;
	return OK;
}

//---------------------------以上为基本操作

void showInfo(SqList &L) {
	printf("\nSqList：\n length : %d \n ", ListLength(L)); //长度
	if (L.length == 0) printf("无元素");
	int e;
	for (int i = 0; i < L.length; i++) {
		GetElem(L, i + 1, e); //获取元素
		printf("%d ", e);
	}
	printf("\n");
}


int main() {

	SqList L;

	InitList(L); //初始化
	showInfo(L);

	printf("是否为空： %d\n", ListEmpty(L)); //判空

	for (int i = 0; i < 10; i++) {
		ListInsert(L, 1, i);
		if (i == 5)
			DestoryList(L); //销毁线性表
		if (i == 6)
			ClearList(L); //清空线性表
	}
	showInfo(L); //插入
	
	printf("是否为空： %d\n", ListEmpty(L));

	int e1 = 0;
	ListDelete(L, 1, e1); //删除
	printf("删除第一个元素 %d 后：", e1);
	showInfo(L);

	int pre = 0;
	PriorElem(L, 7, pre);
	printf("7 pre : %d\n", pre);
	pre = 0;
	PriorElem(L, 8, pre);
	printf("8 pre : %d\n", pre);

	int suc = 0;
	NextElem(L, 7, suc);
	printf("7 suc : %d\n", suc);
	suc = 0;
	NextElem(L, 8, suc);
	printf("8 suc : %d\n", suc);

	printf("第一个与7相等的元素的序号: %d\n", LocateElem(L, 7));
	printf("第一个与9相等的元素的序号: %d\n", LocateElem(L, 9));

	return 0;
}
```




## 栈与队列



