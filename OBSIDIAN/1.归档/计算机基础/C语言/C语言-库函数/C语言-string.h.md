> https://www.runoob.com/cprogramming/c-standard-library-string-h.html

## string.h总结

### mem开头

`void *memset(void *str, int c, size_t n)`复制字符c（一个无符号字符）到参数str所指向的字符串的前n个字符。

`void memchr(const void *str, int c, size_t n)` 在参数str所指向的字符串的前n个字节中搜索第一次出现字符c（一个无符号字符）的位置。

`int memcmp(const void *str1, const void *str2, size_t n)`把str1和str2的前n个字节进行比较。

`void *memcpy(void *dest, const void *src, size_t n)`从src复制n个字符到dest。

`void *memmove(void *dest, const void *src, size_t n)`另一个用于从src复制n个字符到dest的函数。

### str开头

`size_t strlen(const char *str)`计算字符串str的长度，直到空结束字符，但不包括空结束字符。

`char *strcat(char *dest, const char *src)`把src所指向的字符串追加到dest所指向的字符串的结尾。

`char *strncat(char *dest, const char *src, size_t n)`把src所指向的字符串追加到dest所指向的字符串的结尾，直到n字符长度为止。

`char *strchr(const char *str, int c)`在参数str所指向的字符串中搜索第一次出现字符c（一个无符号字符）的位置。

`int strcmp(const char *str1, const char *str2)`把str1所指向的字符串和str2所指向的字符串进行比较。

`int strncmp(const char *str1, const char *str2, size_t n)`把str1和str2进行比较，最多比较前n个字节。

### 数值转换

- atoi(str); int
- atof(str); double
- atol(str); long

```c
char str[] = "2371.32";

printf("%d\n", atoi(str)); // 转换到int整型。2371

printf("%lf\n", atof(str)); // 转换为double类型，2371.320000

printf("%ld\n", atol(str)); // 转换为long长整型。2371
```