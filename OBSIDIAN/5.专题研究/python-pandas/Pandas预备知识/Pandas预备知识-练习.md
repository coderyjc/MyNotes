## 利用列表推导式写矩阵乘法



## 更新矩阵



## 卡方统计量


设矩阵 \(A_{m\times n}\) ，记 \(B_{ij} = \frac{(\sum_{i=p}^mA_{pj})\times (\sum_{q=1}^nA_{iq})}{\sum_{p=1}^m\sum_{q=1}^nA_{pq}}\) ，定义卡方值如下：
\[\chi^2 = \sum_{i=1}^m\sum_{j=1}^n\frac{(A_{ij}-B_{ij})^2}{B_{ij}}\]
请利用 `Numpy` 对给定的矩阵 \(A\) 计算 \(\chi^2\) 。

## 改进矩阵计算的性能



## 连续整数的最大长度