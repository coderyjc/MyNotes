
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

## 自己写的这个ac了

```c
#include<iostream>  
#include<algorithm>  
#include<string.h>  
#include<deque>  
#include<map>  
  
using namespace std;  
  
int main(){  
  
    int n;  
    cin >> n;  
    char cmd[3], msg[11];  
    deque<pair<string,int>> v;  
    int priority, sortFlag = 0;  
  
    for (int i = 0; i < n; ++i) {  
        scanf("%s", cmd);  
        if(cmd[0] == 'P'){  
            scanf("%s %d", msg, &priority);  
            v.push_back((pair<string, int>)make_pair(msg, priority));  
            sortFlag = 0;  
        } else {  
            if(!sortFlag){  
                sort(v.begin(), v.end(), [](const pair<string, int> &p1, const pair<string, int> &p2){  
                    return p1.second < p2.second;  
                });  
                sortFlag = 1;  
            }  
            if(v.size() != 0){  
                cout << v[0].first << endl;  
                v.pop_front();  
            } else {  
                printf("EMPTY QUEUE!");  
            }  
        }  
    }  
  
    return 0;  
}
```