# 图像傅里叶变换的MATLAB实现

> 本文基于《MATLAB图像处理实例详解》[杨丹，赵海滨，龙哲]2013年版

## 图像的二维离散傅里叶变换

图像的二维离散傅立叶变换，代码如下

```matlab
% 读入图片
I = imread("img/test1.png");

% 变换之后为 complex double类型
J = fft2(I);

% double类型
K = abs(J/256);

figure;
subplot(121); imshow(I); % 显示图像
subplot(122); imshow(uint8(K)); % 显示频谱图
```

<img src=".\傅立叶变换的matlab实现.imgs\image-20210117084412451.png" alt="image-20210117084412451" style="zoom: 50%;" />

> **为什么要除以256 ？**
>
> 
>
> 首先将图片数据转化为实数类型。这一步将0-255的像素值转化为0.0-1.0范围内的实数。大多数图像处理API支持整数和实数类型的输入。如果输入是整数类型，这些API会在内部将输入转化为实数后处理，再将输出转化为整数。如果有多个处理步骤，在整数和实数之间的反复转化将导致精度损失，因此推荐在图像处理前将其转化为实数类型

> `imshow(uint8(K));` **为什么要将图片转化为uint8形式？**
>
> 
>
> matlab中，常使用imshow()函数来显示图像，而此时的图像矩阵可能经过了某种运算。
>
> 在matlab中，为了保证精度，经过了运算的图像矩阵I其数据类型会从unit8型变成double型。
>
> 如果直接运行imshow(I)，我们会发现显示的是一个白色的图像。这是因为imshow()显示图像时对double型是认为在0~1范围内，即大于1时都是显示为白色，而imshow显示uint8型时是0 ~ 255范围。
>
> 而经过运算的范围在0-255之间的double型数据就被不正常得显示为白色图像了。

## 傅里叶变换后平移

```matlab
% 读入图片
I = imread("img/test1.png");
% 傅里叶变换
J = fft2(I);
% 类型转换
K = abs(J/255);
% 对原图像进行平移
K = fftshift(K); 
figure;
subplot(121); imshow(I); title('原图像');
subplot(122); imshow(uint8(K)); title('傅里叶变换平移之后的图像');
```

<img src=".\傅立叶变换的matlab实现.imgs\image-20210117085909118.png" alt="image-20210117085909118" style="zoom:50%;" />

## 变亮后进行傅里叶变换

```matlab
% 读取图像
R = imread("img/test2.png");
% 将图片变为灰度图像
I = rgb2gray(R);
% 将图像变亮，因为I为uint8类型，所以不用担心超出255的范围。
I1 = I * exp(1);
% 进行傅里叶变换
J1 = fft2(I); % 原图
J2 = fft2(I1); % 变亮后
% 转换
K1 = abs(J1/255);% 原图
K2 = abs(J2/255);% 变亮后
% 图像平移
K1 = fftshift(K1); % 原图
K2 = fftshift(K2); % 变亮后
figure;
subplot(221); imshow(R); title('原图像');
subplot(222); imshow(I); title('灰度图像');
subplot(223); imshow(uint8(K1)); title('傅里叶变换平移之后的图像');
subplot(224); imshow(uint8(K2)); title('变亮之后的图像');
```

<img src=".\傅立叶变换的matlab实现.imgs\image-20210117091428422.png" alt="image-20210117091428422" style="zoom:50%;" />

## 旋转后进行傅里叶变换

```matlab
% 读取图像
R = imread("img/test2.png");
% 将图片变为灰度图像
I = rgb2gray(R);
% 将图像逆时针45度旋转
I1 = imrotate(I, 45, 'bilinear');
% 进行傅里叶变换
J1 = fft2(I); % 原图
J2 = fft2(I1); % 平移后
% 转换
K1 = abs(J1/255);% 原图
K2 = abs(J2/255);% 平移后
% 图像平移
K1 = fftshift(K1); % 原图
K2 = fftshift(K2); % 平移后
figure;
subplot(221); imshow(R); title('原图像');
subplot(222); imshow(I); title('灰度图像');
subplot(223); imshow(uint8(K1)); title('傅里叶变换平移之后的图像');
subplot(224); imshow(uint8(K2)); title('平移之后的图像');
```

<img src=".\傅立叶变换的matlab实现.imgs\image-20210117093043746.png" alt="image-20210117093043746" style="zoom: 50%;" />

## 添加高斯噪声

```matlab
% 读取图像
R = imread("img/test2.png");
P1 = R; % 原彩色图像
% 将图片变为灰度图像
I = rgb2gray(R);
P3 = I;
% 添加高斯噪声
I1 = imnoise(I, 'gaussian', 0, 0.03);
P2 = imnoise(R, 'gaussian', 0, 0.03);
P4 = I1;
% 进行傅里叶变换
J1 = fft2(I); % 原图
J2 = fft2(I1); % 添加后
% 转换
K1 = abs(J1/255);% 原图
K2 = abs(J2/255);% 添加后
% 图像平移
K1 = fftshift(K1); % 原图
K2 = fftshift(K2); % 添加后
figure;
subplot(321); imshow(P1); title('原图像');
subplot(322); imshow(P2); title('高斯噪声');
subplot(323); imshow(P3); title('原图像');
subplot(324); imshow(P4); title('高斯噪声');
subplot(325); imshow(uint8(K1)); title('原图像');
subplot(326); imshow(uint8(K2)); title('高斯噪声');
```

<img src=".\傅立叶变换的matlab实现.imgs\image-20210117093858958.png" alt="image-20210117093858958" style="zoom: 67%;" />

## 傅里叶反变换

```matlab
% 读取图像
R = imread("img/test2.png");
% 将图片变为灰度图像
I = rgb2gray(R);
% 进行傅里叶变换
J = fft2(I);
% 图像平移
L = fftshift(J);
% 平移回来
M = ifftshift(L);
% 傅里叶反变换
M = ifft2(M);

figure;
subplot(121); imshow(I); title('原图');
subplot(122); imshow(uint8(M)); title('反变换');
```

<img src=".\傅立叶变换的matlab实现.imgs\image-20210117181718776.png" alt="image-20210117181718776" style="zoom:67%;" />