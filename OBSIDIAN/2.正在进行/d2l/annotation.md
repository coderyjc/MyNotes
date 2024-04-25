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
