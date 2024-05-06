---
annotation-target: d2l-pytorch.pdf
---


>%%
>```annotation-json
>{"created":"2024-04-25T01:56:22.674Z","updated":"2024-04-25T01:56:22.674Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":92798,"end":92846},{"type":"TextQuoteSelector","exact":"对于任意具有相同形状的张量，常见的标准算术运算符（+、-、*、/和**）都可以被升级为按元素运算","prefix":"数升级为按元素向量运算来生成向量值F : Rd, Rd →Rd。","suffix":"。我们可以在同一形状的任意两个张量上调用按元素操作。在下面的例子"}]}]}
>```
>%%
>*%%PREFIX%%数升级为按元素向量运算来生成向量值F : Rd, Rd →Rd。%%HIGHLIGHT%% ==对于任意具有相同形状的张量，常见的标准算术运算符（+、-、*、/和**）都可以被升级为按元素运算== %%POSTFIX%%。我们可以在同一形状的任意两个张量上调用按元素操作。在下面的例子*
>%%LINK%%[[#^v84f6jl701c|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^v84f6jl701c


>%%
>```annotation-json
>{"created":"2024-04-25T01:57:26.411Z","text":"> Z[:] = X + Y 和 Z = X + Y 有什么区别？\n\n在编程语言中，尤其是在像Python这样支持数组操作的语言中，`Z[:] = X + Y`和`Z = X + Y`两种赋值方式有着明显的区别，这些差异主要体现在内存使用和对象引用上。\n\n1. `Z = X + Y`\n\n这种赋值方式中，`Z`被赋予`X + Y`的结果，这是一种新的数组或对象。这意味着`Z`将引用一个全新的内存地址，即`X + Y`操作生成的新数组或对象的内存位置。如果之前`Z`已经引用了某个数组或对象，那么这个引用将被更新为新的内存地址。\n\n- **内存分配**：这会分配新的内存来存储`X + Y`的结果。\n- **引用更改**：如果之前`Z`已经引用了其他对象，这个操作会改变其引用到新对象。\n\n2. `Z[:] = X + Y`\n\n在这种赋值方式中，使用`Z[:]`实际上是在说“更新`Z`现有的所有元素”。这不会创建`Z`的新实例，而是直接在`Z`当前指向的内存地址中修改数据。这种方法常用于需要保留原有数组或对象`Z`的引用不变的情况下，只更新其内容。\n\n- **原地更新**：`X + Y`的结果将被用来替换`Z`中现有的元素，这不会分配新的内存空间给`Z`，而是修改现有的内容。\n- **引用保持**：`Z`的引用地址不变，只是内容发生了改变。\n\n应用场景的区别\n\n- 当你不想改变`Z`的引用，只想更新其值时，应该使用`Z[:] = X + Y`。这对于当其他变量或数据结构也持有对`Z`的引用时尤其有用，因为这些引用所见的`Z`内容会同步更新。\n- 当你不关心`Z`原来的引用，或者需要`Z`指向一个全新对象时，应该使用`Z = X + Y`。\n\n总的来说，选择哪种方法取决于你是否需要保留原对象的引用以及是否需要避免额外的内存分配。这两种方法在功能上可能看起来相似，但在内存管理和对象引用方面的差异会对程序的性能和行为产生重大影响。","updated":"2024-04-25T01:57:26.411Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":95769,"end":95781},{"type":"TextQuoteSelector","exact":"Z[:] = X + Y","prefix":"os_like(Y)print('id(Z):', id(Z))","suffix":"print('id(Z):', id(Z))id(Z): 140"}]}]}
>```
>%%
>*%%PREFIX%%os_like(Y)print('id(Z):', id(Z))%%HIGHLIGHT%% ==Z[:] = X + Y== %%POSTFIX%%print('id(Z):', id(Z))id(Z): 140*
>%%LINK%%[[#^cim9opz0ae5|show annotation]]
>%%COMMENT%%
>> Z[:] = X + Y 和 Z = X + Y 有什么区别？
>
>在编程语言中，尤其是在像Python这样支持数组操作的语言中，`Z[:] = X + Y`和`Z = X + Y`两种赋值方式有着明显的区别，这些差异主要体现在内存使用和对象引用上。
>
>1. `Z = X + Y`
>
>这种赋值方式中，`Z`被赋予`X + Y`的结果，这是一种新的数组或对象。这意味着`Z`将引用一个全新的内存地址，即`X + Y`操作生成的新数组或对象的内存位置。如果之前`Z`已经引用了某个数组或对象，那么这个引用将被更新为新的内存地址。
>
>- **内存分配**：这会分配新的内存来存储`X + Y`的结果。
>- **引用更改**：如果之前`Z`已经引用了其他对象，这个操作会改变其引用到新对象。
>
>2. `Z[:] = X + Y`
>
>在这种赋值方式中，使用`Z[:]`实际上是在说“更新`Z`现有的所有元素”。这不会创建`Z`的新实例，而是直接在`Z`当前指向的内存地址中修改数据。这种方法常用于需要保留原有数组或对象`Z`的引用不变的情况下，只更新其内容。
>
>- **原地更新**：`X + Y`的结果将被用来替换`Z`中现有的元素，这不会分配新的内存空间给`Z`，而是修改现有的内容。
>- **引用保持**：`Z`的引用地址不变，只是内容发生了改变。
>
>应用场景的区别
>
>- 当你不想改变`Z`的引用，只想更新其值时，应该使用`Z[:] = X + Y`。这对于当其他变量或数据结构也持有对`Z`的引用时尤其有用，因为这些引用所见的`Z`内容会同步更新。
>- 当你不关心`Z`原来的引用，或者需要`Z`指向一个全新对象时，应该使用`Z = X + Y`。
>
>总的来说，选择哪种方法取决于你是否需要保留原对象的引用以及是否需要避免额外的内存分配。这两种方法在功能上可能看起来相似，但在内存管理和对象引用方面的差异会对程序的性能和行为产生重大影响。
>%%TAGS%%
>
^cim9opz0ae5


>%%
>```annotation-json
>{"created":"2024-04-25T01:57:59.649Z","updated":"2024-04-25T01:57:59.649Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":96136,"end":96182},{"type":"TextQuoteSelector","exact":"要将大小为1的张量转换为Python标量，我们可以调用item函数或Python的内置函数。","prefix":"(B)(numpy.ndarray, torch.Tensor)","suffix":"a = torch.tensor([3.5])a, a.item"}]}]}
>```
>%%
>*%%PREFIX%%(B)(numpy.ndarray, torch.Tensor)%%HIGHLIGHT%% ==要将大小为1的张量转换为Python标量，我们可以调用item函数或Python的内置函数。== %%POSTFIX%%a = torch.tensor([3.5])a, a.item*
>%%LINK%%[[#^r3k5rxcn7mm|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^r3k5rxcn7mm


>%%
>```annotation-json
>{"created":"2024-04-25T01:58:27.261Z","updated":"2024-04-25T01:58:27.261Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":99809,"end":99836},{"type":"TextQuoteSelector","exact":"量文献认为列向量是向量的默认方向，在本书中也是如此。在","prefix":"个元素。注意，元素xi是一个标量，所以我们在引用它时不会加粗。大","suffix":"数学中，向量x可以写为：x =x1x2...xn"}]}]}
>```
>%%
>*%%PREFIX%%个元素。注意，元素xi是一个标量，所以我们在引用它时不会加粗。大%%HIGHLIGHT%% ==量文献认为列向量是向量的默认方向，在本书中也是如此。在== %%POSTFIX%%数学中，向量x可以写为：x =x1x2...xn*
>%%LINK%%[[#^arg4ro6e50e|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^arg4ro6e50e


>%%
>```annotation-json
>{"created":"2024-04-25T01:58:42.598Z","updated":"2024-04-25T01:58:42.598Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":100300,"end":100376},{"type":"TextQuoteSelector","exact":"向量或轴的维度被用来表示向量或轴的长度，即向量或轴的元素数量。然而，张量的维度用来表示张量具有的轴数。在这个意义上，张量的某个轴的维数就是这个轴的长度。","prefix":"同的含义，这经常会使人感到困惑。为了清楚起见，我们在此明确一下：","suffix":"2.3.3 矩阵正如向量将标量从零阶推广到一阶，矩阵将向量从一阶"}]}]}
>```
>%%
>*%%PREFIX%%同的含义，这经常会使人感到困惑。为了清楚起见，我们在此明确一下：%%HIGHLIGHT%% ==向量或轴的维度被用来表示向量或轴的长度，即向量或轴的元素数量。然而，张量的维度用来表示张量具有的轴数。在这个意义上，张量的某个轴的维数就是这个轴的长度。== %%POSTFIX%%2.3.3 矩阵正如向量将标量从零阶推广到一阶，矩阵将向量从一阶*
>%%LINK%%[[#^xe18bnaxm5p|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^xe18bnaxm5p


>%%
>```annotation-json
>{"created":"2024-04-25T02:04:22.016Z","updated":"2024-04-25T02:04:22.016Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":101850,"end":101888},{"type":"TextQuoteSelector","exact":"量（本小节中的“张量”指代数对象）是描述具有任意数量轴的n维数组的通用方法。","prefix":"推广，矩阵是向量的推广一样，我们可以构建具有更多轴的数据结构。张","suffix":"例如，向量是一阶张量，矩阵是二阶张量。张量用特殊字体的大写字母表"}]}]}
>```
>%%
>*%%PREFIX%%推广，矩阵是向量的推广一样，我们可以构建具有更多轴的数据结构。张%%HIGHLIGHT%% ==量（本小节中的“张量”指代数对象）是描述具有任意数量轴的n维数组的通用方法。== %%POSTFIX%%例如，向量是一阶张量，矩阵是二阶张量。张量用特殊字体的大写字母表*
>%%LINK%%[[#^fvrcx5qfsqk|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^fvrcx5qfsqk


>%%
>```annotation-json
>{"created":"2024-04-25T02:07:09.893Z","updated":"2024-04-25T02:07:09.893Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":102725,"end":102771},{"type":"TextQuoteSelector","exact":"两个矩阵的按元素乘法称为Hadamard积（Hadamard product）（数学符号⊙）","prefix":"0.],[32., 34., 36., 38.]]))具体而言，","suffix":"。对于矩阵B ∈Rm×n，其中第i行和第j列的元素是bij 。矩"}]}]}
>```
>%%
>*%%PREFIX%%0.],[32., 34., 36., 38.]]))具体而言，%%HIGHLIGHT%% ==两个矩阵的按元素乘法称为Hadamard积（Hadamard product）（数学符号⊙）== %%POSTFIX%%。对于矩阵B ∈Rm×n，其中第i行和第j列的元素是bij 。矩*
>%%LINK%%[[#^juelh9qbcd|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^juelh9qbcd


>%%
>```annotation-json
>{"created":"2024-04-25T02:16:00.588Z","text":"- axis=0 指的是沿着行的方向，也就是向下跨越行（行索引变化）。如果你对 A 进行某些操作并指定 axis=0，意味着你要在每一列上进行该操作，处理的是行方向的元素。例如，如果你计算 A.sum(axis=0)，你将得到一个形状为 [4] 的张量，其中包含了 A 每一列元素的和。\n- axis=1 指的是沿着列的方向，也就是向右跨越列（列索引变化）。当你在对 A 指定 axis=1 进行操作时，你将在每一行上执行该操作，处理的是列方向的元素。例如，A.sum(axis=1) 将返回一个形状为 [5] 的张量，其中包含了 A 每一行元素的和。\n\n简而言之，axis=0 和 axis=1 在 PyTorch 的张量操作中分别指向行的变化方向和列的变化方向，这是在进行维度操作时非常基础且重要的概念。","updated":"2024-04-25T02:16:00.588Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":103669,"end":103728},{"type":"TextQuoteSelector","exact":"默认情况下，调用求和函数会沿所有的轴降低张量的维度，使它变为一个标量。我们还可以指定张量沿哪一个轴来通过求和降低维度。","prefix":"orch.Size([5, 4]), tensor(190.))","suffix":"以矩阵为例，为了通过求和所有行的元素来降维（轴0），可以在调用函"}]}]}
>```
>%%
>*%%PREFIX%%orch.Size([5, 4]), tensor(190.))%%HIGHLIGHT%% ==默认情况下，调用求和函数会沿所有的轴降低张量的维度，使它变为一个标量。我们还可以指定张量沿哪一个轴来通过求和降低维度。== %%POSTFIX%%以矩阵为例，为了通过求和所有行的元素来降维（轴0），可以在调用函*
>%%LINK%%[[#^a7swyx669yr|show annotation]]
>%%COMMENT%%
>- axis=0 指的是沿着行的方向，也就是向下跨越行（行索引变化）。如果你对 A 进行某些操作并指定 axis=0，意味着你要在每一列上进行该操作，处理的是行方向的元素。例如，如果你计算 A.sum(axis=0)，你将得到一个形状为 [4] 的张量，其中包含了 A 每一列元素的和。
>- axis=1 指的是沿着列的方向，也就是向右跨越列（列索引变化）。当你在对 A 指定 axis=1 进行操作时，你将在每一行上执行该操作，处理的是列方向的元素。例如，A.sum(axis=1) 将返回一个形状为 [5] 的张量，其中包含了 A 每一行元素的和。
>
>简而言之，axis=0 和 axis=1 在 PyTorch 的张量操作中分别指向行的变化方向和列的变化方向，这是在进行维度操作时非常基础且重要的概念。
>%%TAGS%%
>
^a7swyx669yr


>%%
>```annotation-json
>{"created":"2024-04-25T02:26:17.235Z","updated":"2024-04-25T02:26:17.235Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":104418,"end":104445},{"type":"TextQuoteSelector","exact":"有时在调用函数来计算总和或均值时保持轴数不变会很有用。","prefix":"or([ 8., 9., 10., 11.]))非降维求和但是，","suffix":"sum_A = A.sum(axis=1, keepdims=T"}]}]}
>```
>%%
>*%%PREFIX%%or([ 8., 9., 10., 11.]))非降维求和但是，%%HIGHLIGHT%% ==有时在调用函数来计算总和或均值时保持轴数不变会很有用。== %%POSTFIX%%sum_A = A.sum(axis=1, keepdims=T*
>%%LINK%%[[#^l4d24kde7mi|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^l4d24kde7mi


>%%
>```annotation-json
>{"created":"2024-04-25T02:57:12.172Z","text":"当你尝试将一个 (4, 5) 形状的张量 A 除以一个形状为 [4] 的张量时，PyTorch 需要两个张量的形状能够广播（Broadcast）。广播规则要求从**尾部维度向前匹配**，每个维度的大小要么相同，要么其中一个是 1。在此例中，A 是 (4, 5)，而 A.sum(axis=1) 是 [4]。由于 A.sum(axis=1) 的形状实际上是 [4, 1]（如果进行了正确的维度扩展），则这种除法才有可能正常执行。因为 [4, 1] 可以与 [4, 5] 进行广播，[4] 不能直接与 [4, 5] 进行广播。","updated":"2024-04-25T02:57:12.172Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":109035,"end":109069},{"type":"TextQuoteSelector","exact":"运行A/A.sum(axis=1)，看看会发生什么。请分析一下原因？","prefix":",len(X)是否总是对应于X特定轴的长度?这个轴是什么?6. ","suffix":"7. 考虑一个具有形状(2, 3, 4)的张量，在轴0、1、2上"}]}]}
>```
>%%
>*%%PREFIX%%,len(X)是否总是对应于X特定轴的长度?这个轴是什么?6.%%HIGHLIGHT%% ==运行A/A.sum(axis=1)，看看会发生什么。请分析一下原因？== %%POSTFIX%%7. 考虑一个具有形状(2, 3, 4)的张量，在轴0、1、2上*
>%%LINK%%[[#^juog0b72vlm|show annotation]]
>%%COMMENT%%
>当你尝试将一个 (4, 5) 形状的张量 A 除以一个形状为 [4] 的张量时，PyTorch 需要两个张量的形状能够广播（Broadcast）。广播规则要求从**尾部维度向前匹配**，每个维度的大小要么相同，要么其中一个是 1。在此例中，A 是 (4, 5)，而 A.sum(axis=1) 是 [4]。由于 A.sum(axis=1) 的形状实际上是 [4, 1]（如果进行了正确的维度扩展），则这种除法才有可能正常执行。因为 [4, 1] 可以与 [4, 5] 进行广播，[4] 不能直接与 [4, 5] 进行广播。
>%%TAGS%%
>
^juog0b72vlm


>%%
>```annotation-json
>{"created":"2024-04-25T08:30:28.928Z","updated":"2024-04-25T08:30:28.928Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":117250,"end":117306},{"type":"TextQuoteSelector","exact":"对于任何a，存在某个常量标量k，使得f(a)=k*a，其中k的值取决于输入a，因此可以用d/a验证梯度是否正确。","prefix":"析上面定义的f函数。请注意，它在其输入a中是分段线性的。换言之，","suffix":"72 2. 预备知识a.grad == d / atensor("}]}]}
>```
>%%
>*%%PREFIX%%析上面定义的f函数。请注意，它在其输入a中是分段线性的。换言之，%%HIGHLIGHT%% ==对于任何a，存在某个常量标量k，使得f(a)=k*a，其中k的值取决于输入a，因此可以用d/a验证梯度是否正确。== %%POSTFIX%%72 2. 预备知识a.grad == d / atensor(*
>%%LINK%%[[#^dv5ehga7hkw|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^dv5ehga7hkw


>%%
>```annotation-json
>{"created":"2024-04-25T08:34:20.164Z","text":" .backward() 方法通常要求它所计算梯度的源（即 d）必须是一个标量值。当 a 是一个向量时，通过 f 函数计算得到的 d 也将是一个向量，因此不能直接使用 .backward()。","updated":"2024-04-25T08:34:20.164Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":117477,"end":117521},{"type":"TextQuoteSelector","exact":"在控制流的例子中，我们计算d关于a的导数，如果将变量a更改为随机向量或矩阵，会发生什么？","prefix":" 在运行反向传播函数之后，立即再次运行它，看看会发生什么。3. ","suffix":"4. 重新设计一个求控制流梯度的例子，运行并分析结果。5. 使f"}]}]}
>```
>%%
>*%%PREFIX%%在运行反向传播函数之后，立即再次运行它，看看会发生什么。3.%%HIGHLIGHT%% ==在控制流的例子中，我们计算d关于a的导数，如果将变量a更改为随机向量或矩阵，会发生什么？== %%POSTFIX%%4. 重新设计一个求控制流梯度的例子，运行并分析结果。5. 使f*
>%%LINK%%[[#^r93qmu141tg|show annotation]]
>%%COMMENT%%
> .backward() 方法通常要求它所计算梯度的源（即 d）必须是一个标量值。当 a 是一个向量时，通过 f 函数计算得到的 d 也将是一个向量，因此不能直接使用 .backward()。
>%%TAGS%%
>
^r93qmu141tg


>%%
>```annotation-json
>{"created":"2024-04-25T09:19:18.901Z","text":"\n```python\nx = torch.arange(0, 10, 0.1, requires_grad=True)\nsinx = torch.sin(x)\n\nsinx.sum().backward()  # 使用.sum()使sinx成为标量以调用.backward() \n\ncosx = x.grad\nplot(x.detach().numpy(), [sinx.detach().numpy(), cosx.detach().numpy()], 'sinx', 'cosx')\n```\n\n在 PyTorch 中，.backward() 方法用于计算梯度，但它只能被直接调用在标量（即一个单一数值）张量上。如果对象是非标量张量（即包含多个值的张量），则 .backward() 需要一个与该张量形状相同的参数作为梯度权重，这样才能计算对应的向量-雅可比乘积（Vector-Jacobian product，VJP），从而得到每个元素相对于源张量的梯度。\n\n当你调用 torch.sin(x)，其中 x 是一个包含多个值的张量时，结果同样是一个包含多个值的张量。为了能够使用 .backward() 方法计算梯度，你需要将这个结果张量转换成一个标量。这就是为什么要使用 .sum() 方法的原因。.sum() 方法会计算张量中所有元素的总和，从而将任何形状的张量转换为一个单一的标量值。这样做的好处是：\n\n允许梯度计算：将结果转换为标量后，可以直接调用 .backward() 来计算梯度，而无需额外的权重参数。\n简化计算：使用 .sum() 保证了无论输入张量的大小或维度如何，总能得到一个可以用于梯度计算的标量输出。\n适用性广：这种方法适用于任何需要梯度反向传播的场景，而不仅仅是处理向量或矩阵。\n在具体的代码实现中，例如：\n\nsinx = torch.sin(x)\ntotal = sinx.sum()\ntotal.backward()\n这里，sinx 是 torch.sin(x) 的结果，它是一个向量。通过调用 sinx.sum()，你创建了一个名为 total 的新标量，它是 sinx 中所有元素的和。现在 total 是一个标量，可以直接在其上调用 .backward()，这会触发自动计算梯度的过程，计算出 total 相对于 x 中每个元素的梯度，并将这些梯度存储在 x.grad 属性中。\n\n因此，使用 .sum() 是将结果张量简化为可以进行梯度计算的标量的一种有效方法。","updated":"2024-04-25T09:19:18.901Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":117587,"end":117609},{"type":"TextQuoteSelector","exact":"其中后者不使用f ′(x) = cos(x)","prefix":"x) = sin(x)，绘制f (x)和df(x)dx 的图像，","suffix":"。Discussions412.6 概率简单地说，机器学习就是做"}]}]}
>```
>%%
>*%%PREFIX%%x) = sin(x)，绘制f (x)和df(x)dx 的图像，%%HIGHLIGHT%% ==其中后者不使用f ′(x) = cos(x)== %%POSTFIX%%。Discussions412.6 概率简单地说，机器学习就是做*
>%%LINK%%[[#^klm6g2rzahh|show annotation]]
>%%COMMENT%%
>
>```python
>x = torch.arange(0, 10, 0.1, requires_grad=True)
>sinx = torch.sin(x)
>
>sinx.sum().backward()  # 使用.sum()使sinx成为标量以调用.backward() 
>
>cosx = x.grad
>plot(x.detach().numpy(), [sinx.detach().numpy(), cosx.detach().numpy()], 'sinx', 'cosx')
>```
>
>在 PyTorch 中，.backward() 方法用于计算梯度，但它只能被直接调用在标量（即一个单一数值）张量上。如果对象是非标量张量（即包含多个值的张量），则 .backward() 需要一个与该张量形状相同的参数作为梯度权重，这样才能计算对应的向量-雅可比乘积（Vector-Jacobian product，VJP），从而得到每个元素相对于源张量的梯度。
>
>当你调用 torch.sin(x)，其中 x 是一个包含多个值的张量时，结果同样是一个包含多个值的张量。为了能够使用 .backward() 方法计算梯度，你需要将这个结果张量转换成一个标量。这就是为什么要使用 .sum() 方法的原因。.sum() 方法会计算张量中所有元素的总和，从而将任何形状的张量转换为一个单一的标量值。这样做的好处是：
>
>允许梯度计算：将结果转换为标量后，可以直接调用 .backward() 来计算梯度，而无需额外的权重参数。
>简化计算：使用 .sum() 保证了无论输入张量的大小或维度如何，总能得到一个可以用于梯度计算的标量输出。
>适用性广：这种方法适用于任何需要梯度反向传播的场景，而不仅仅是处理向量或矩阵。
>在具体的代码实现中，例如：
>
>sinx = torch.sin(x)
>total = sinx.sum()
>total.backward()
>这里，sinx 是 torch.sin(x) 的结果，它是一个向量。通过调用 sinx.sum()，你创建了一个名为 total 的新标量，它是 sinx 中所有元素的和。现在 total 是一个标量，可以直接在其上调用 .backward()，这会触发自动计算梯度的过程，计算出 total 相对于 x 中每个元素的梯度，并将这些梯度存储在 x.grad 属性中。
>
>因此，使用 .sum() 是将结果张量简化为可以进行梯度计算的标量的一种有效方法。
>%%TAGS%%
>
^klm6g2rzahh


>%%
>```annotation-json
>{"created":"2024-04-25T23:59:27.021Z","updated":"2024-04-25T23:59:27.021Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":130567,"end":130601},{"type":"TextQuoteSelector","exact":"自变量x和因变量y之间的关系是线性的，即y可以表示为x中元素的加权和","prefix":"准工具中最简单而且最流行。线性回归基于几个简单的假设：首先，假设","suffix":"，这里通常允许包含观测值的一些噪声；其次，我们假设任何噪声都比较"}]}]}
>```
>%%
>*%%PREFIX%%准工具中最简单而且最流行。线性回归基于几个简单的假设：首先，假设%%HIGHLIGHT%% ==自变量x和因变量y之间的关系是线性的，即y可以表示为x中元素的加权和== %%POSTFIX%%，这里通常允许包含观测值的一些噪声；其次，我们假设任何噪声都比较*
>%%LINK%%[[#^j8k8s83b55g|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^j8k8s83b55g


>%%
>```annotation-json
>{"created":"2024-04-26T00:11:33.293Z","updated":"2024-04-26T00:11:33.293Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":133331,"end":133384},{"type":"TextQuoteSelector","exact":"梯度下降最简单的用法是计算损失函数（数据集中所有样本的损失均值）关于模型参数的导数（在这里也可以称为梯度）","prefix":"学习模型。它通过不断地在损失函数递减的方向上更新参数来降低误差。","suffix":"。但实际中的执行可能会非常慢：因为在每一次更新参数之前，我们必须"}]}]}
>```
>%%
>*%%PREFIX%%学习模型。它通过不断地在损失函数递减的方向上更新参数来降低误差。%%HIGHLIGHT%% ==梯度下降最简单的用法是计算损失函数（数据集中所有样本的损失均值）关于模型参数的导数（在这里也可以称为梯度）== %%POSTFIX%%。但实际中的执行可能会非常慢：因为在每一次更新参数之前，我们必须*
>%%LINK%%[[#^qvrhytehm7a|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^qvrhytehm7a


>%%
>```annotation-json
>{"created":"2024-04-26T01:34:52.058Z","text":"yield 关键字使得函数执行可以在每次产生值后暂停并保存状态，等待下次再被激活继续执行。","updated":"2024-04-26T01:34:52.058Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":140974,"end":140979},{"type":"TextQuoteSelector","exact":"yield","prefix":"(i + batch_size, num_examples)])","suffix":" features[batch_indices], labels"}]}]}
>```
>%%
>*%%PREFIX%%(i + batch_size, num_examples)])%%HIGHLIGHT%% ==yield== %%POSTFIX%%features[batch_indices], labels*
>%%LINK%%[[#^krtnudodyxf|show annotation]]
>%%COMMENT%%
>yield 关键字使得函数执行可以在每次产生值后暂停并保存状态，等待下次再被激活继续执行。
>%%TAGS%%
>
^krtnudodyxf


>%%
>```annotation-json
>{"created":"2024-04-26T02:41:25.034Z","updated":"2024-04-26T02:41:25.034Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":148429,"end":148454},{"type":"TextQuoteSelector","exact":"我们可以通过_结尾的方法将参数替换，从而初始化参数","prefix":"数据处理工具，nn模块定义了大量的神经网络层和常见损失函数。• ","suffix":"。练习1. 如果将小批量的总损失替换为小批量损失的平均值，需要如"}]}]}
>```
>%%
>*%%PREFIX%%数据处理工具，nn模块定义了大量的神经网络层和常见损失函数。•%%HIGHLIGHT%% ==我们可以通过_结尾的方法将参数替换，从而初始化参数== %%POSTFIX%%。练习1. 如果将小批量的总损失替换为小批量损失的平均值，需要如*
>%%LINK%%[[#^4d7020zb7a6|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^4d7020zb7a6


>%%
>```annotation-json
>{"created":"2024-04-26T02:52:06.924Z","updated":"2024-04-26T02:52:06.924Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":151289,"end":151319},{"type":"TextQuoteSelector","exact":"softmax回归是一个线性模型（linear model）","prefix":"，但softmax回归的输出仍然由输入特征的仿射变换决定。因此，","suffix":"。3.4. softmax回归 1073.4.5 小批量样本的矢"}]}]}
>```
>%%
>*%%PREFIX%%，但softmax回归的输出仍然由输入特征的仿射变换决定。因此，%%HIGHLIGHT%% ==softmax回归是一个线性模型（linear model）== %%POSTFIX%%。3.4. softmax回归 1073.4.5 小批量样本的矢*
>%%LINK%%[[#^v4lu8417ef|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^v4lu8417ef


>%%
>```annotation-json
>{"created":"2024-04-26T03:02:46.991Z","updated":"2024-04-26T03:02:46.991Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":152995,"end":153040},{"type":"TextQuoteSelector","exact":"此损失称为交叉熵损失（cross‐entropy loss），它是分类问题最常用的损失之一","prefix":"们使用(3.4.8)来定义损失l，它是所有标签分布的预期损失值。","suffix":"。本节我们将通过介绍信息论基础来理解交叉熵损失。如果想了解更多信"}]}]}
>```
>%%
>*%%PREFIX%%们使用(3.4.8)来定义损失l，它是所有标签分布的预期损失值。%%HIGHLIGHT%% ==此损失称为交叉熵损失（cross‐entropy loss），它是分类问题最常用的损失之一== %%POSTFIX%%。本节我们将通过介绍信息论基础来理解交叉熵损失。如果想了解更多信*
>%%LINK%%[[#^t97i4a8cxuo|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^t97i4a8cxuo


>%%
>```annotation-json
>{"created":"2024-04-26T06:41:41.183Z","updated":"2024-04-26T06:41:41.183Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":158604,"end":158651},{"type":"TextQuoteSelector","exact":"数据迭代器是获得更高性能的关键组件。依靠实现良好的数据迭代器，利用高性能计算来避免减慢训练过程","prefix":"将高度h像素，宽度w像素图像的形状记为h ×w或（h,w）。• ","suffix":"。114 3. 线性神经网络练习1. 减少batch_size（"}]}]}
>```
>%%
>*%%PREFIX%%将高度h像素，宽度w像素图像的形状记为h ×w或（h,w）。•%%HIGHLIGHT%% ==数据迭代器是获得更高性能的关键组件。依靠实现良好的数据迭代器，利用高性能计算来避免减慢训练过程== %%POSTFIX%%。114 3. 线性神经网络练习1. 减少batch_size（*
>%%LINK%%[[#^uf64eo971v|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^uf64eo971v


>%%
>```annotation-json
>{"created":"2024-04-26T07:13:14.446Z","text":"= y[ [0, 1], [0, 2] ]\n= y[0, 0], y[1, 2]\n= 0.1,  0.5","updated":"2024-04-26T07:13:14.446Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":161213,"end":161229},{"type":"TextQuoteSelector","exact":"y_hat[[0, 1], y]","prefix":".1, 0.3, 0.6], [0.3, 0.2, 0.5]])","suffix":"tensor([0.1000, 0.5000])现在我们只需一行"}]}]}
>```
>%%
>*%%PREFIX%%.1, 0.3, 0.6], [0.3, 0.2, 0.5]])%%HIGHLIGHT%% ==y_hat[[0, 1], y]== %%POSTFIX%%tensor([0.1000, 0.5000])现在我们只需一行*
>%%LINK%%[[#^fk2ykvhoqeg|show annotation]]
>%%COMMENT%%
>= y[ [0, 1], [0, 2] ]
>= y[0, 0], y[1, 2]
>= 0.1,  0.5
>%%TAGS%%
>
^fk2ykvhoqeg


>%%
>```annotation-json
>{"created":"2024-04-26T07:36:17.906Z","text":"每一行的最大值的索引","updated":"2024-04-26T07:36:17.906Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":162008,"end":162022},{"type":"TextQuoteSelector","exact":"argmax(axis=1)","prefix":"_hat.shape[1] > 1:y_hat = y_hat.","suffix":"cmp = y_hat.type(y.dtype) == yre"}]}]}
>```
>%%
>*%%PREFIX%%_hat.shape[1] > 1:y_hat = y_hat.%%HIGHLIGHT%% ==argmax(axis=1)== %%POSTFIX%%cmp = y_hat.type(y.dtype) == yre*
>%%LINK%%[[#^fvkdl4b0q9|show annotation]]
>%%COMMENT%%
>每一行的最大值的索引
>%%TAGS%%
>
^fvkdl4b0q9


>%%
>```annotation-json
>{"created":"2024-04-26T08:41:18.264Z","updated":"2024-04-26T08:41:18.264Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":162423,"end":162433},{"type":"TextQuoteSelector","exact":"将模型设置为评估模式","prefix":", torch.nn.Module):net.eval() # ","suffix":"metric = Accumulator(2) # 正确预测数、"}]}]}
>```
>%%
>*%%PREFIX%%, torch.nn.Module):net.eval() #%%HIGHLIGHT%% ==将模型设置为评估模式== %%POSTFIX%%metric = Accumulator(2) # 正确预测数、*
>%%LINK%%[[#^11tq33g2shyj|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^11tq33g2shyj


>%%
>```annotation-json
>{"created":"2024-04-27T01:03:43.334Z","updated":"2024-04-27T01:03:43.334Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":173745,"end":173835},{"type":"TextQuoteSelector","exact":"参数化ReLU（Parameterized ReLU，pReLU）函数(He et al., 2015)。该变体为ReLU添加了一个线性项，因此即使参数是负的，某些信息仍然可以通过","prefix":"度消失问题（稍后将详细介绍）。注意，ReLU函数有许多变体，包括","suffix":"：pReLU(x) = max(0, x) + α min(0,"}]}]}
>```
>%%
>*%%PREFIX%%度消失问题（稍后将详细介绍）。注意，ReLU函数有许多变体，包括%%HIGHLIGHT%% ==参数化ReLU（Parameterized ReLU，pReLU）函数(He et al., 2015)。该变体为ReLU添加了一个线性项，因此即使参数是负的，某些信息仍然可以通过== %%POSTFIX%%：pReLU(x) = max(0, x) + α min(0,*
>%%LINK%%[[#^wp24nhn3omj|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^wp24nhn3omj


>%%
>```annotation-json
>{"created":"2024-04-27T01:04:47.139Z","updated":"2024-04-27T01:04:47.139Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":174994,"end":175033},{"type":"TextQuoteSelector","exact":"函数的形状类似于sigmoid函数，不同的是tanh函数关于坐标系原点中心对称","prefix":"tanh函数。注意，当输入在0附近时，tanh函数接近线性变换。","suffix":"。y = torch.tanh(x)d2l.plot(x.det"}]}]}
>```
>%%
>*%%PREFIX%%tanh函数。注意，当输入在0附近时，tanh函数接近线性变换。%%HIGHLIGHT%% ==函数的形状类似于sigmoid函数，不同的是tanh函数关于坐标系原点中心对称== %%POSTFIX%%。y = torch.tanh(x)d2l.plot(x.det*
>%%LINK%%[[#^4fom5cbj5va|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^4fom5cbj5va


>%%
>```annotation-json
>{"created":"2024-04-27T01:14:42.705Z","text":"1. 学习的不稳定性。梯度估计可能有较大的方差，可能导致梯度消失或者梯度爆炸\n2. 模型泛化能力减少\n3. 梯度消失或者爆炸","updated":"2024-04-27T01:14:42.705Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":175819,"end":175858},{"type":"TextQuoteSelector","exact":"假设我们有一个非线性单元，将它一次应用于一个小批量的数据。这会导致什么样的问题","prefix":"明tanh(x) + 1 = 2 sigmoid(2x)。4. ","suffix":"？Discussions5959 https://discuss"}]}]}
>```
>%%
>*%%PREFIX%%明tanh(x) + 1 = 2 sigmoid(2x)。4.%%HIGHLIGHT%% ==假设我们有一个非线性单元，将它一次应用于一个小批量的数据。这会导致什么样的问题== %%POSTFIX%%？Discussions5959 https://discuss*
>%%LINK%%[[#^6pm1h54bxhq|show annotation]]
>%%COMMENT%%
>1. 学习的不稳定性。梯度估计可能有较大的方差，可能导致梯度消失或者梯度爆炸
>2. 模型泛化能力减少
>3. 梯度消失或者爆炸
>%%TAGS%%
>
^6pm1h54bxhq


>%%
>```annotation-json
>{"created":"2024-04-27T03:48:42.661Z","updated":"2024-04-27T03:48:42.661Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":230146,"end":230173},{"type":"TextQuoteSelector","exact":"研究讨论“比单个层大”但“比整个模型小”的组件更有价值","prefix":"可调参数，这些参数根据从下一层反向传播的信号进行更新。事实证明，","suffix":"。例如，在计算机视觉中广泛流行的ResNet‐152架构就有数百"}]}]}
>```
>%%
>*%%PREFIX%%可调参数，这些参数根据从下一层反向传播的信号进行更新。事实证明，%%HIGHLIGHT%% ==研究讨论“比单个层大”但“比整个模型小”的组件更有价值== %%POSTFIX%%。例如，在计算机视觉中广泛流行的ResNet‐152架构就有数百*
>%%LINK%%[[#^ln24xk86ihq|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ln24xk86ihq


>%%
>```annotation-json
>{"created":"2024-04-27T06:37:56.725Z","text":"在 NumPy 中，一维数组通常不会特定地作为行向量或列向量。它只是一个一维的数组，其方向性（行或列）取决于你如何在操作中使用它。\n直接生成的形状是(20,)\n指定为行向量之后是(1, 20)\n指定为列向量之后是(20, 1)","updated":"2024-04-27T06:37:56.725Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":185197,"end":185203},{"type":"TextQuoteSelector","exact":"np.dot","prefix":"ls的维度:(n_train+n_test,)labels = ","suffix":"(poly_features, true_w)labels +="}]}]}
>```
>%%
>*%%PREFIX%%ls的维度:(n_train+n_test,)labels =%%HIGHLIGHT%% ==np.dot== %%POSTFIX%%(poly_features, true_w)labels +=*
>%%LINK%%[[#^a2xr01ik0l9|show annotation]]
>%%COMMENT%%
>在 NumPy 中，一维数组通常不会特定地作为行向量或列向量。它只是一个一维的数组，其方向性（行或列）取决于你如何在操作中使用它。
>直接生成的形状是(20,)
>指定为行向量之后是(1, 20)
>指定为列向量之后是(20, 1)
>%%TAGS%%
>
^a2xr01ik0l9


>%%
>```annotation-json
>{"created":"2024-04-27T07:11:01.280Z","updated":"2024-04-27T07:11:01.280Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":189517,"end":189564},{"type":"TextQuoteSelector","exact":"权重衰减（weight decay）是最广泛使用的正则化的技术之一，它通常也被称为L2正则化。","prefix":"/18064.5. 权重衰减 149在训练参数化机器学习模型时，","suffix":"这项技术通过函数与零的距离来衡量函数的复杂度，因为在所有函数f "}]}]}
>```
>%%
>*%%PREFIX%%/18064.5. 权重衰减 149在训练参数化机器学习模型时，%%HIGHLIGHT%% ==权重衰减（weight decay）是最广泛使用的正则化的技术之一，它通常也被称为L2正则化。== %%POSTFIX%%这项技术通过函数与零的距离来衡量函数的复杂度，因为在所有函数f*
>%%LINK%%[[#^izkwqeyepd|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^izkwqeyepd


>%%
>```annotation-json
>{"created":"2024-04-27T07:44:45.823Z","updated":"2024-04-27T07:44:45.823Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":195666,"end":195718},{"type":"TextQuoteSelector","exact":"经典泛化理论认为，为了缩小训练和测试性能之间的差距，应该以简单的模型为目标。简单性以较小维度的形式展现，","prefix":"预测模型？我们期待“好”的预测模型能在未知的数据上有很好的表现：","suffix":"我们在4.4节讨论线性模型的单项式函数时探讨了这一点。此外，正如"}]}]}
>```
>%%
>*%%PREFIX%%预测模型？我们期待“好”的预测模型能在未知的数据上有很好的表现：%%HIGHLIGHT%% ==经典泛化理论认为，为了缩小训练和测试性能之间的差距，应该以简单的模型为目标。简单性以较小维度的形式展现，== %%POSTFIX%%我们在4.4节讨论线性模型的单项式函数时探讨了这一点。此外，正如*
>%%LINK%%[[#^nol8stbie9|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^nol8stbie9


>%%
>```annotation-json
>{"created":"2024-04-27T12:11:01.745Z","updated":"2024-04-27T12:11:01.745Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":204494,"end":204601},{"type":"TextQuoteSelector","exact":"要么是梯度爆炸（gradient exploding）问题：参数更新过大，破坏了模型的稳定收敛；要么是梯度消失（gradient vanishing）问题：参数更新过小，在每次更新时几乎不会移动，导致模型无法学习。","prefix":"；不稳定梯度也威胁到我们优化算法的稳定性。我们可能面临一些问题。","suffix":"梯度消失曾经sigmoid函数1/(1 + exp(−x))（4"}]}]}
>```
>%%
>*%%PREFIX%%；不稳定梯度也威胁到我们优化算法的稳定性。我们可能面临一些问题。%%HIGHLIGHT%% ==要么是梯度爆炸（gradient exploding）问题：参数更新过大，破坏了模型的稳定收敛；要么是梯度消失（gradient vanishing）问题：参数更新过小，在每次更新时几乎不会移动，导致模型无法学习。== %%POSTFIX%%梯度消失曾经sigmoid函数1/(1 + exp(−x))（4*
>%%LINK%%[[#^sjku7xv7k3|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^sjku7xv7k3


>%%
>```annotation-json
>{"created":"2024-04-27T12:18:41.098Z","updated":"2024-04-27T12:18:41.098Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":207929,"end":207956},{"type":"TextQuoteSelector","exact":"ReLU激活函数缓解了梯度消失问题，这样可以加速收敛。","prefix":"• 需要用启发式的初始化方法来确保初始梯度既不太大也不太小。• ","suffix":"• 随机初始化是保证在进行优化前打破对称性的关键。• Xavie"}]}]}
>```
>%%
>*%%PREFIX%%• 需要用启发式的初始化方法来确保初始梯度既不太大也不太小。•%%HIGHLIGHT%% ==ReLU激活函数缓解了梯度消失问题，这样可以加速收敛。== %%POSTFIX%%• 随机初始化是保证在进行优化前打破对称性的关键。• Xavie*
>%%LINK%%[[#^8ck9m0mcam2|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^8ck9m0mcam2


>%%
>```annotation-json
>{"created":"2024-04-27T12:22:53.191Z","updated":"2024-04-27T12:22:53.191Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":208387,"end":208467},{"type":"TextQuoteSelector","exact":"时，根据测试集的精度衡量，模型表现得非常出色。但是当数据分布突然改变时，模型在部署中会出现灾难性的失败。更隐蔽的是，有时模型的部署本身就是扰乱数据分布的催化剂。","prefix":"题。许多失败的机器学习部署（即实际应用）都可以追究到这种方式。有","suffix":"举一个有点荒谬却可能真实存在的例子。假设我们训练了一个贷款申请人"}]}]}
>```
>%%
>*%%PREFIX%%题。许多失败的机器学习部署（即实际应用）都可以追究到这种方式。有%%HIGHLIGHT%% ==时，根据测试集的精度衡量，模型表现得非常出色。但是当数据分布突然改变时，模型在部署中会出现灾难性的失败。更隐蔽的是，有时模型的部署本身就是扰乱数据分布的催化剂。== %%POSTFIX%%举一个有点荒谬却可能真实存在的例子。假设我们训练了一个贷款申请人*
>%%LINK%%[[#^g767xx5slsf|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^g767xx5slsf



>%%
>```annotation-json
>{"created":"2024-04-28T03:13:25.583Z","text":"需要对参数进行手动管理，并自己编写前向传播逻辑。","updated":"2024-04-28T03:13:25.583Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":235906,"end":235939},{"type":"TextQuoteSelector","exact":"如果将MySequential中存储块的方式更改为Python列表","prefix":"播。• 层和块的顺序连接由Sequential块处理。练习1. ","suffix":"，会出现什么样的问题？2. 实现一个块，它以两个块为参数，例如n"}]}]}
>```
>%%
>*%%PREFIX%%播。• 层和块的顺序连接由Sequential块处理。练习1.%%HIGHLIGHT%% ==如果将MySequential中存储块的方式更改为Python列表== %%POSTFIX%%，会出现什么样的问题？2. 实现一个块，它以两个块为参数，例如n*
>%%LINK%%[[#^f0k5yz5uxl|show annotation]]
>%%COMMENT%%
>需要对参数进行手动管理，并自己编写前向传播逻辑。
>%%TAGS%%
>
^f0k5yz5uxl


>%%
>```annotation-json
>{"created":"2024-04-28T06:36:47.434Z","updated":"2024-04-28T06:36:47.434Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":257813,"end":257846},{"type":"TextQuoteSelector","exact":"图像的平移不变性使我们以相同的方式处理局部图像，而不在乎它的位置。","prefix":"合理的网络设计选择？我们将在本章的其它部分讨论这些问题。小结• ","suffix":"• 局部性意味着计算相应的隐藏表示只需一小部分局部图像像素。• "}]}]}
>```
>%%
>*%%PREFIX%%合理的网络设计选择？我们将在本章的其它部分讨论这些问题。小结•%%HIGHLIGHT%% ==图像的平移不变性使我们以相同的方式处理局部图像，而不在乎它的位置。== %%POSTFIX%%• 局部性意味着计算相应的隐藏表示只需一小部分局部图像像素。•*
>%%LINK%%[[#^ligj3epmosp|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^ligj3epmosp


>%%
>```annotation-json
>{"created":"2024-04-28T07:03:28.259Z","updated":"2024-04-28T07:03:28.259Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":262682,"end":262732},{"type":"TextQuoteSelector","exact":"感受野（receptivefield）是指在前向传播期间可能影响x计算的所有元素（来自所有先前层）。","prefix":"的空间维度的转换器。在卷积神经网络中，对于某一层的任意元素x，其","suffix":"请注意，感受野可能大于输入的实际大小。让我们用图6.2.1为例来"}]}]}
>```
>%%
>*%%PREFIX%%的空间维度的转换器。在卷积神经网络中，对于某一层的任意元素x，其%%HIGHLIGHT%% ==感受野（receptivefield）是指在前向传播期间可能影响x计算的所有元素（来自所有先前层）。== %%POSTFIX%%请注意，感受野可能大于输入的实际大小。让我们用图6.2.1为例来*
>%%LINK%%[[#^o3b078x1dqp|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^o3b078x1dqp


>%%
>```annotation-json
>{"created":"2024-04-28T07:10:49.013Z","updated":"2024-04-28T07:10:49.013Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":266411,"end":266425},{"type":"TextQuoteSelector","exact":"填充可以增加输出的高度和宽度","prefix":"充，也就是说，我们通常有ph = pw和sh = sw。小结• ","suffix":"。这常用来使输出与输入具有相同的高和宽。• 步幅可以减小输出的高"}]}]}
>```
>%%
>*%%PREFIX%%充，也就是说，我们通常有ph = pw和sh = sw。小结•%%HIGHLIGHT%% ==填充可以增加输出的高度和宽度== %%POSTFIX%%。这常用来使输出与输入具有相同的高和宽。• 步幅可以减小输出的高*
>%%LINK%%[[#^3nxq36fjg8a|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^3nxq36fjg8a


>%%
>```annotation-json
>{"created":"2024-04-28T07:10:51.250Z","updated":"2024-04-28T07:10:51.250Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":266447,"end":266459},{"type":"TextQuoteSelector","exact":"步幅可以减小输出的高和宽","prefix":"增加输出的高度和宽度。这常用来使输出与输入具有相同的高和宽。• ","suffix":"，例如输出的高和宽仅为输入的高和宽的1/n（n是一个大于1的整数"}]}]}
>```
>%%
>*%%PREFIX%%增加输出的高度和宽度。这常用来使输出与输入具有相同的高和宽。•%%HIGHLIGHT%% ==步幅可以减小输出的高和宽== %%POSTFIX%%，例如输出的高和宽仅为输入的高和宽的1/n（n是一个大于1的整数*
>%%LINK%%[[#^3diy65fqmo4|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^3diy65fqmo4


>%%
>```annotation-json
>{"created":"2024-04-28T07:20:05.446Z","updated":"2024-04-28T07:20:05.446Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":268935,"end":268955},{"type":"TextQuoteSelector","exact":"其实1 ×1卷积的唯一计算发生在通道上。","prefix":"的特有能力——在高度和宽度维度上，识别相邻元素间相互作用的能力。","suffix":"图6.4.2展示了使用1 ×1卷积核与3个输入通道和2个输出通道"}]}]}
>```
>%%
>*%%PREFIX%%的特有能力——在高度和宽度维度上，识别相邻元素间相互作用的能力。%%HIGHLIGHT%% ==其实1 ×1卷积的唯一计算发生在通道上。== %%POSTFIX%%图6.4.2展示了使用1 ×1卷积核与3个输入通道和2个输出通道*
>%%LINK%%[[#^gw7140vwy4l|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^gw7140vwy4l


>%%
>```annotation-json
>{"created":"2024-04-28T07:21:18.789Z","updated":"2024-04-28T07:21:18.789Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":269042,"end":269087},{"type":"TextQuoteSelector","exact":"们可以将1 ×1卷积层看作在每个像素位置应用的全连接层，以ci个输入值转换为co个输出值。","prefix":"度，输出中的每个元素都是从输入图像中同一位置的元素的线性组合。我","suffix":"因为这仍然是一个卷积层，所以跨像素的权重是一致的。同时，1 ×1"}]}]}
>```
>%%
>*%%PREFIX%%度，输出中的每个元素都是从输入图像中同一位置的元素的线性组合。我%%HIGHLIGHT%% ==们可以将1 ×1卷积层看作在每个像素位置应用的全连接层，以ci个输入值转换为co个输出值。== %%POSTFIX%%因为这仍然是一个卷积层，所以跨像素的权重是一致的。同时，1 ×1*
>%%LINK%%[[#^idoedbqnzd|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^idoedbqnzd


>%%
>```annotation-json
>{"created":"2024-04-28T16:19:27.603Z","updated":"2024-04-28T16:19:27.603Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":291885,"end":291912},{"type":"TextQuoteSelector","exact":"深层且窄的卷积（即3 ×3）比较浅层且宽的卷积更有效。","prefix":"Simonyan和Ziserman尝试了各种架构。特别是他们发现","suffix":"258 7. 现代卷积神经网络练习1. 打印层的尺寸时，我们只看"}]}]}
>```
>%%
>*%%PREFIX%%Simonyan和Ziserman尝试了各种架构。特别是他们发现%%HIGHLIGHT%% ==深层且窄的卷积（即3 ×3）比较浅层且宽的卷积更有效。== %%POSTFIX%%258 7. 现代卷积神经网络练习1. 打印层的尺寸时，我们只看*
>%%LINK%%[[#^u1ecc7bl43d|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^u1ecc7bl43d


>%%
>```annotation-json
>{"created":"2024-05-04T09:15:46.027Z","updated":"2024-05-04T09:15:46.027Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":572940,"end":572967},{"type":"TextQuoteSelector","exact":"杰卡德系数（Jaccard）可以衡量两组之间的相似性。","prefix":"如何如何量化呢？直观地说，可以衡量锚框和真实边界框之间的相似性。","suffix":"给定集合A和B，他们的杰卡德系数是他们交集的大小除以他们并集的大"}]}]}
>```
>%%
>*%%PREFIX%%如何如何量化呢？直观地说，可以衡量锚框和真实边界框之间的相似性。%%HIGHLIGHT%% ==杰卡德系数（Jaccard）可以衡量两组之间的相似性。== %%POSTFIX%%给定集合A和B，他们的杰卡德系数是他们交集的大小除以他们并集的大*
>%%LINK%%[[#^3tgg6ypmp6y|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^3tgg6ypmp6y


>%%
>```annotation-json
>{"created":"2024-05-06T03:11:13.572Z","updated":"2024-05-06T03:11:13.572Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":574222,"end":574293},{"type":"TextQuoteSelector","exact":"我们为每个图像生成多个锚框，预测所有锚框的类别和偏移量，根据预测的偏移量调整它们的位置以获得预测的边界框，最后只输出符合特定条件的预测边界框。","prefix":"相关的对象的类别，后者是真实边界框相对于锚框的偏移量。在预测时，","suffix":"目标检测训练集带有真实边界框的位置及其包围物体类别的标签。要标记"}]}]}
>```
>%%
>*%%PREFIX%%相关的对象的类别，后者是真实边界框相对于锚框的偏移量。在预测时，%%HIGHLIGHT%% ==我们为每个图像生成多个锚框，预测所有锚框的类别和偏移量，根据预测的偏移量调整它们的位置以获得预测的边界框，最后只输出符合特定条件的预测边界框。== %%POSTFIX%%目标检测训练集带有真实边界框的位置及其包围物体类别的标签。要标记*
>%%LINK%%[[#^1x2st4uc6vf|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^1x2st4uc6vf


>%%
>```annotation-json
>{"created":"2024-05-06T09:01:38.490Z","updated":"2024-05-06T09:01:38.490Z","document":{"title":"动手学深度学习","link":[{"href":"urn:x-pdf:157da93b1afe8a748efb1869b3821e2a"},{"href":"vault:/0.plugin/pdf/d2l-pytorch.pdf"}],"documentFingerprint":"157da93b1afe8a748efb1869b3821e2a"},"uri":"vault:/0.plugin/pdf/d2l-pytorch.pdf","target":[{"source":"vault:/0.plugin/pdf/d2l-pytorch.pdf","selector":[{"type":"TextPositionSelector","start":606811,"end":606859},{"type":"TextQuoteSelector","exact":"与目标检测不同，语义分割可以识别并理解图像中每一个像素的内容：其语义区域的标注和预测是像素级的。","prefix":"on）问题，它重点关注于如何将图像分割成属于不同语义类别的区域。","suffix":"图13.9.1展示了语义分割中图像有关狗、猫和背景的标签。与目标"}]}]}
>```
>%%
>*%%PREFIX%%on）问题，它重点关注于如何将图像分割成属于不同语义类别的区域。%%HIGHLIGHT%% ==与目标检测不同，语义分割可以识别并理解图像中每一个像素的内容：其语义区域的标注和预测是像素级的。== %%POSTFIX%%图13.9.1展示了语义分割中图像有关狗、猫和背景的标签。与目标*
>%%LINK%%[[#^lb44tszwkha|show annotation]]
>%%COMMENT%%
>
>%%TAGS%%
>
^lb44tszwkha
