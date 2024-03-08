![[assets/Pasted image 20240303144016.png]]

```c
#include <stdio.h>  
#include <math.h>  
  
int main(){  
    double sum = 0, sign = 1.0;  
    int n = 1, count = 0;  
    double term = 1.0; // 用来保存【当前】最后一项的值，这个值是非常有必要的，用于判断循环是否结束。  
  
    // 如果直接使用 1/n 来判断是否结束的话，由于在循环体内已经加了2，因此判断的时候是当前项的下一项的值，而不是当前项的值。  
    while(fabs(term) >= 1e-4){  
        term = sign / n;  
        sum += term;  
        count++;  
        sign = -sign;  
        n += 2;  
    }  
  
    printf("count = %d\n", count);  
    printf("result = %lf", sum * 4);  
    return 0;  
}
```

