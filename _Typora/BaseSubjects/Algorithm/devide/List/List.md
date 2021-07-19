#### [面试题 02.03. 删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci/)

既然杀不掉你，我就变成你，然后干掉你。

```C
class Solution {
public:
    void deleteNode(ListNode* node) {
        node->val = node->next->val;
        node->next = node->next->next;
    }
};
```

#### [剑指 Offer 18. 删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/)







#### [剑指 Offer 22. 链表中倒数第k个节点](https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/)

**快慢指针**

双指针初始位置都是首节点，前指针先走k步，结束之后两个指针之间的间距为k

```c++
class Solution {
public:
    ListNode* getKthFromEnd(ListNode* head, int k) {
        ListNode* header = head;
        ListNode* trailer = head;
        
        while(header->next && --k){
            header = header->next;
        }
        while(header->next){
            header = header->next;
            trailer = trailer->next;
        }
        return trailer;
    }
};

```



#### [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number/)

快慢双指针 + 循环链表

