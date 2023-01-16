
> [【哈迪斯（Hades）】夜之圣镜修改指南](https://www.bilibili.com/video/BV1Sr4y1u7Qk)

> [!info] Attention
> 
> 游戏根目录在 `steam\steamapps\common\Hades`
> 
> 游戏脚本在 `steam\steamapps\common\Hades\Content`

---

文件：`Scripts/MetaUpgradeData.lua`
行数：882

`MetaUpgradeOrder` 包含了一个12行的列表，定义了技能的排序

![[assets/Pasted image 20230116154133.png]]

这些对应的对象，就是各种天赋，我们可以在这里自定义各种天赋组合。

修改这些对象对应的参数，就可以实现自定义BUFF突破升级。

## 举例1：修改死里逃生

死里逃生对应为 `ExtraChanceMetaUpgrade`

在该文件中搜索 `ExtraChanceMetaUpgrade`

![[assets/Pasted image 20230116164325.png]]

定位到了399行

我们很容易可以知道以下内容：

```lua
	ExtraChanceMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", }, 
		Icon = "MirrorIcon_ExtraChance", 
		Starting = true, 
		CostTable = { 30, 500, 1000 }, -- 每一级对应的花费
		Color = { 255, 255, 255, 255 }, 
		ShortTotal = "ExtraChanceMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "ExtraChanceMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 1, -- 每一级所改变的数值
		KeywordOverride =
		{
			Key = "ExtraChance",
			Value = "ExtraChance",
		},
	},

```

通过修改每一级对应的花费和每一级改变的数值，我们可以实现改变死里逃生的数量

比如：


```lua
	ExtraChanceMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", }, 
		Icon = "MirrorIcon_ExtraChance", 
		Starting = true, 
		CostTable = { 30, 500, 1000, 1, 1 }, -- 每一级对应的花费
		Color = { 255, 255, 255, 255 }, 
		ShortTotal = "ExtraChanceMetaUpgrade_ShortTotal",
		ShortTotalNoIcon = "ExtraChanceMetaUpgrade_ShortTotalNoIcon",
		ChangeValue = 3, -- 每一级所改变的数值
		KeywordOverride =
		{
			Key = "ExtraChance",
			Value = "ExtraChance",
		},
	},

```

每一级的花费中添加了两个1，每一级改变的 数值为3，这样每升一级就增加3个死里逃生了，一共5级，升满之后一共15个死里逃生


## 举例2：修改必出传奇或者双重祝福

对应的天赋为神之恩赐，对应的对象为：`DuoRarityBoonDropMetaUpgrade`

搜索

![[assets/Pasted image 20230116165114.png]]

可以看出

```lua
	DuoRarityBoonDropMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_DuoRarityBoon",
		Starting = true,
		Cost = 250, -- 每一次升级花费250黑暗
		MaxInvestment = 10, -- 最多升10级
		ShortTotal = "DuoRarityBoonDropMetaUpgrade_ShortTotal",
		ChangeValue = 1.01, -- 每一次改变1%的几率
	},
```

可以改成：

```lua
	DuoRarityBoonDropMetaUpgrade =
	{
		InheritFrom = { "BaseMetaUpgrade", },
		Icon = "MirrorIcon_DuoRarityBoon",
		Starting = true,
		Cost = 1, -- 每一次升级花费1黑暗
		MaxInvestment = 10, -- 最多升10级
		ShortTotal = "DuoRarityBoonDropMetaUpgrade_ShortTotal",
		ChangeValue = 1.10, -- 每一次改变10%的几率
	},
```

这样，10黑暗就可以升到100%几率了。

但是传奇祝福和双重祝福的出现是有前置条件的，改成100%容易造成游戏崩溃，因此最好不要修改太多。

