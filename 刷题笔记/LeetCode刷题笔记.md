# LeetCode刷题笔记

## 1480.一维数组的动态和

![](images/1480.png)

关键点：问清楚面试官是否可以修改穿入的nums数组

如果能修改nums数组：

```C++
/*
作者：liuyubobobo
链接：https://leetcode-cn.com/problems/running-sum-of-1d-array/solution/ru-guo-mian-shi-yu-dao-zhe-ge-wen-ti-zhe-yi-dian-z/
来源：力扣（LeetCode）
*/

class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        //从第1个开始，让后面的数字依次加等于其前面一位，这样可以节省空间
        for(int i = 1; i < nums.size(); i ++)
            nums[i] += nums[i - 1];
        return nums;
    }
};
```