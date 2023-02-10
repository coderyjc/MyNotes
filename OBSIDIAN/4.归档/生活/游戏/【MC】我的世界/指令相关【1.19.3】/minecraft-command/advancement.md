
## 语法

```bash
/advancement [grant/revoke] [@a/e/p/r/s] [everything/from/only/through/until] <minecraft:条目/进度>
```

## 参数

grant是给与，revoke是移除

everything给与全部

from给与一个进度及下游进度

only指定的进度

through给与一个进度及上游和下游进度

until给与一个进度及上游进度

> 具体的进度英文所代表的进度可以在这个文件夹下查看：
> `.minecraft/version/版本/版本.jar`
> 需要解压后查看

## 举例

```bash
# 给与所有人所有的进度
/advancement grant @a everything

# 移除所有人的“冒险的时光”进度
/advancement revoke @a only minecraft:adventure/adventuring_time
```
