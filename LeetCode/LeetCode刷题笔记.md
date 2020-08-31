# LeetCode刷题笔记

## 1480.一维数组的动态和

![](LeetCodeImages/1480.png)

关键点：问清楚面试官是否可以修改传入的nums数组

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
        //从第1个开始，让后面的数字依次加等于其前面一位，这样可以【节省空间】。
        for(int i = 1; i < nums.size(); i ++) 
        //在这里，不用再使用一个变量来保存nums.size()，因为开辟内存的时间要比直接调用函数的时间多太多了。
            nums[i] += nums[i - 1];
        return nums;
    }
};
```

如果不能修改nums数组：

```C++
/*
作者：liuyubobobo
链接：https://leetcode-cn.com/problems/running-sum-of-1d-array/solution/ru-guo-mian-shi-yu-dao-zhe-ge-wen-ti-zhe-yi-dian-z/
来源：力扣（LeetCode）
*/
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {

        vector<int> res(nums.size()); 
        //提前开辟好空间而不是push_back()，降低时间复杂度
        res[0] = nums[0];
        for(int i = 1; i < nums.size(); i ++)
            res[i] = res[i - 1] + nums[i];
        return res;
    }
};
```

我的代码：

```C++
class Solution {
public:
    vector<int> runningSum(vector<int>& nums) {
        vector<int> rst; //重开了一个数组->没必要，并且没有提前开辟空间->时间复杂度大
        int sum = 0;
        for(auto i : nums){
            sum += i;
            rst.push_back(sum); //插入的时间复杂度大
        }
        return rst;
    }
};
```

总结：

1. 能修改原来的数据就尽量修改原来的数据，降低空间复杂度

2. 数组能提前开辟就不要在中途插入的时候开辟
