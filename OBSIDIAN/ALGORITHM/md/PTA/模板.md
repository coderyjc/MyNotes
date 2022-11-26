### 判断素数

```c++
int isPrime(int n) {
	if (n < 2) return 0;
	for (int i = 2; i <= sqrt(n); i++) {
		if (0 == n % i) return 0;
	}
	return 1;
}
```


### algorithm::sort 排序规则

```c++
bool cmp(int a, int b){
	return a < b; // 默认。升序排列。
}

```

