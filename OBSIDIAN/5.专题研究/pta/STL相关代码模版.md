## MAP


### map按照value排序

```cpp
struct CmpByValue {  
  bool operator()(const pair<int, int>& lhs, const pair<int, int>& rhs) {  
    return lhs.second > rhs.second;  
  }  
};

// ....
// 先转换为vector<pair>，再进行排序
vector<pair<int, int>> name_score_vec(name_score_map.begin(), name_score_map.end());
sort(name_score_vec.begin(), name_score_vec.end(), CmpByValue());
```


