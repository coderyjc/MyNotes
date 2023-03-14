
参考： https://blog.csdn.net/ATCG7/article/details/106963196

题解使用优先级队列+scanf/printf函数IO

---

```cpp
#include<iostream>
#include<cstdio>
#include<algorithm>
#include<queue>

using namespace std;

struct news
{
	char name[20];
	int pri;
	friend bool operator <(news a,news b) {
		return a.pri >b.pri ;
  }
}win[100005];

int main() {
	int n, cnt = 0;
	scanf("%d", &n); getchar();

	char action[10];
	priority_queue<news> w;
	
  for(int i = 0; i < n; i++) {
		scanf("%s", action);
		if(action[0] == 'P') {
			scanf("%s %d", win[cnt].name, &win[cnt].pri);
			w.push(win[cnt]); 
			cnt++;
		}
		else if(action[0] == 'G') {
			if(w.empty()) {
				printf("EMPTY QUEUE!\n");
			}
			else {
				printf("%s\n", w.top().name);
				w.pop();
			}
		}
	}
	return 0;
}
```

### 自己写的这个最后一个点过不去

应该是数量上来了就过不去了。

### 我把所有IO都改成了scanf和printf，还是超时

```cpp
/**
* Author: Yan Jingcun
* Date: 2023-03-13
* Descption: 
*/ 

#include<iostream>
#include<vector>
#include<algorithm>
#include<string.h>
#include<queue>

using namespace std;

int main(){

  int isorderd = 0;
  int n;
  cin >> n;
  int pri;

  char op[3];
  char* v[100001];
  int a[100001];
  memset(a, 0, 100001 * sizeof(int));

  for (int i = 0; i < n; i++) {
    scanf("%s",op);
    if(op[0] == 'P' && op[1] == 'U' && op[2] == 'T'){
      char* msg = new char[11];
      scanf("%s %d", msg, &pri);
      v[pri] = msg;
      a[pri] = 1;
    }else if(op[0] == 'G' && op[1] == 'E' && op[2] == 'T'){
      int flag = 0;
      for (int i = 0; i < 100001; i++) {
        if(a[i] != 0) {
          printf("%s\n", v[i]);
          a[i] = 0;
          flag = 1;
          break;
        }
      }
      if(!flag) printf("EMPTY QUEUE!");
    }
  }

  return 0;
}
```