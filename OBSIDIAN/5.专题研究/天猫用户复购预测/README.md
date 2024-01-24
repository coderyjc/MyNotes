# tmall users repurchase forecast

复购率的两种计算方法

$$复购率=\frac{重复购买用户数量}{用户样本数量}$$

$$复购率＝\frac{重复重复购买行为次数（或者交易次数）}{用户样本数量}$$

## 数据介绍

### 用户日志表

| Data Fields | Definition                                       |
| ----------- | ------------------------------------------------ |
| user_id     | 用户id                                           |
| item_id     | 商品id                                           |
| cat_id      | 商品类目id                                       |
| seller_id   | 商家id                                           |
| brand_id    | 品牌id                                           |
| time_stamp  | 行为发生时间                                     |
| action_type | 操作类型｛0、1、2、3｝表示点击、加购、购买、收藏 |

```python
user_log = pd.read_csv("../data/user_log_format1.csv")
user_log.head(5)
```

![[assets/Pasted image 20240124102713.png]]

### 用户特征表

| Data Fields | Definition                                                                                                                                |
| ----------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| user_id     | 用户id                                                                                                                                    |
| age_range   | 顾客（用户）年龄范围：1表示<18；2表示[18，24]；3表示[25，29]；4表示[30，34]；5表示[35，39]；6表示[40，49]；7and8表示≥50；0andNull表示未知 |
| gender      | 0表示女性、1表示男性、2和null表示未知                                                                                                     |

```python
user_info = pd.read_csv("../data/user_info_format1.csv")
user_info.head(5)
```

![[assets/Pasted image 20240124102746.png]]

### 训练数据和测试数据

| Data Fields | Definition               |
| ----------- | ------------------------ |
| user_id     | 用户id                   |
| merchant_id | 商家id                   |
| label       | 1表示复购、0表示不是复购 |

```python
train_data = pd.read_csv("../data/train_format1.csv")  
train_data.head(5)
```

![[assets/Pasted image 20240124102911.png]]

```python
test_data = pd.read_csv("../data/test_format1.csv")  
test_data.head(5)
```

![[assets/Pasted image 20240124102920.png]]

## 评估指标

AUC为本赛题的评估指标

$$AUC={ \sum_{i \in positive Class}rank_{i} - {M(1+M) \over 2} \over {M*N}}$$

含义：
1. 只反映模型对正负样本排序能力的强弱，对score的大小和精度没有要求。
2. AUC越高，模型排序能力越强。理论上，当模型把所有正样本都排在负样本之前时，AUC为1.0，是理论的最大值。例如，有100个样本，其中有20个正样本，80个负样本。我们通过模型给每个样本打分，如果每个正样本的score/probability都高于所有负样本，则AUC为最高值1.0。

调用方法：

