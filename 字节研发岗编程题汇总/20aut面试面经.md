1.最长回文子串  
https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zui-chang-hui-wen-zi-chuan-by-leetcode-solution/  
```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = ""
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = (dp[i + 1][j - 1] and s[i] == s[j])
                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]
        return ans
```

2.枚举全排列  
```python
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(first = 0):
            # 所有数都填完了
            if first == n:  
                res.append(nums[:])
            for i in range(first, n):
                # 动态维护数组
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]
        
        n = len(nums)
        res = []
        backtrack()
        return res
```

3.最近公共祖先  
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.ancestor = None
        def help(root, p, q):
            if root is None:
                return False
            left = help(root.left, p, q)
            right = help(root.right, p, q)
            if root.val == p.val or root.val == q.val:
                if left or right:
                    self.ancestor = root
                else:
                    return True
            if left and right:
                self.ancestor = root
            elif left or right:
                return True
            elif not left and not right:
                return False
                
        help(root, p, q)
        return self.ancestor
```

4.快速排序  

5.leetcode354 信封嵌套问题  
最长递增子序列的二维问题。  
https://leetcode-cn.com/problems/russian-doll-envelopes/solution/python3-dong-tai-gui-hua-fa-er-fen-fa-by-yim-6/  
```python
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        n=len(envelopes)
        envelopes.sort(key=lambda x:(x[0],-x[1]))
        arr=[envelopes[0][1]]


        def bin_search(target):
            l,r=0,len(arr)-1
            while l<=r:
                mid=l+(r-l)//2
                if arr[mid]==target:
                    return mid
                elif arr[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return l            
           

        for i in range(1,n):
            w,h=envelopes[i]
            index = bin_search(h)
            if index==len(arr):
                arr.append(h)
            else:
                arr[index]=h
        return len(arr)
```

6.给定一个矩阵里面只包含0和1两种数字，给出每个单元距离最近的0的距离，上下左右都算作相邻，相邻的距离为1  
https://leetcode-cn.com/problems/01-matrix/solution/tao-lu-da-jie-mi-gao-dong-ti-mu-kao-cha-shi-yao-2/  

7.一个无序数组，数字代表挡板的高度，挡板没有厚度最多可以盛多少水，如[3, 1, 2] 输出:4  

8.S1, S2两个整数数组 已经从大到小排序。输出最大的K个数, 时间复杂度: 通过k/2的思想, 直到把k为到1为止  

9.S1, S2,..., Sx整数数组 已经从大到小排序。输出最大的K个数, 时间复杂度  

10.给定一个可包含重复数字的序列，返回所有不重复的全排列  

11.求二叉树的宽度  
```python
# 宽度优先搜索
def widthOfBinaryTree(self, root):
    queue = [(root, 0, 0)]
    cur_depth = left = ans = 0
    for node, depth, pos in queue:
        if node:
            queue.append((node.left, depth+1, pos*2))
            queue.append((node.right, depth+1, pos*2 + 1))
            if cur_depth != depth:
                cur_depth = depth
                left = pos
            ans = max(pos - left + 1, ans)

    return ans

# 深度优先搜索
class Solution(object):
    def widthOfBinaryTree(self, root):
        self.ans = 0
        left = {}
        def dfs(node, depth = 0, pos = 0):
            if node:
                left.setdefault(depth, pos)
                self.ans = max(self.ans, pos - left[depth] + 1)
                dfs(node.left, depth + 1, pos * 2)
                dfs(node.right, depth + 1, pos * 2 + 1)

        dfs(root)
        return self.ans
```

12."abcccbda"->"ada" 去除字符串的重复字符  

13.无序数组 Top K，时间复杂度，给出一个最坏复杂度的样例  

14.写一个 Softmax 实现，注意上下溢出问题  
```python
def softmax_loss_naive(W, X, y, reg):
  loss = 0.0
  dW = np.zeros_like(W)
  f=np.dot(X,W)  #N*C
  fm=np.reshape(np.max(f,axis=1),(X.shape[0],1)) #N*1
  L = -np.log(np.exp(f-fm)/np.sum(np.exp(f-fm),axis=1,keepdims=True))
  for i in xrange(X.shape[0]):
    for j in xrange(W.shape[1]):
        if (y[i]==j):
            loss+=L[i,j]
            
  loss=loss/X.shape[0]
  loss+=0.5 * reg * np.sum(W * W)
  return loss, dW
```

15.给前序中序，求后序  
```python
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def myBuildTree(preorder_left: int, preorder_right: int, inorder_left: int, inorder_right: int):
            if preorder_left > preorder_right:
                return None
            
            # 前序遍历中的第一个节点就是根节点
            preorder_root = preorder_left
            # 在中序遍历中定位根节点
            inorder_root = index[preorder[preorder_root]]
            
            # 先把根节点建立出来
            root = TreeNode(preorder[preorder_root])
            # 得到左子树中的节点数目
            size_left_subtree = inorder_root - inorder_left
            # 递归地构造左子树，并连接到根节点
            # 先序遍历中「从 左边界+1 开始的 size_left_subtree」个元素就对应了中序遍历中「从 左边界 开始到 根节点定位-1」的元素
            root.left = myBuildTree(preorder_left + 1, preorder_left + size_left_subtree, inorder_left, inorder_root - 1)
            # 递归地构造右子树，并连接到根节点
            # 先序遍历中「从 左边界+1+左子树节点数目 开始到 右边界」的元素就对应了中序遍历中「从 根节点定位+1 到 右边界」的元素
            root.right = myBuildTree(preorder_left + size_left_subtree + 1, preorder_right, inorder_root + 1, inorder_right)
            return root
        
        n = len(preorder)
        # 构造哈希映射，帮助我们快速定位根节点
        index = {element: i for i, element in enumerate(inorder)}
        return myBuildTree(0, n - 1, 0, n - 1)
```

16.顺时针输出矩阵  
```python
class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix: return []
        l, r, t, b, res = 0, len(matrix[0]) - 1, 0, len(matrix) - 1, []
        while True:
            for i in range(l, r + 1): res.append(matrix[t][i]) # left to right
            t += 1
            if t > b: break
            for i in range(t, b + 1): res.append(matrix[i][r]) # top to bottom
            r -= 1
            if l > r: break
            for i in range(r, l - 1, -1): res.append(matrix[b][i]) # right to left
            b -= 1
            if t > b: break
            for i in range(b, t - 1, -1): res.append(matrix[i][l]) # bottom to top
            l += 1
            if l > r: break
        return res
```

17.LCA（最近公共祖先）  
```python
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: return # 1.
        if not left: return right # 3.
        if not right: return left # 4.
        return root # 2. if left and right:
```

18.线段树的一些操作  

19.模糊匹配（一个字串里有些地方可能是错的或者缺了，在原来的地方找到最有可能的位置）  

20.n个人之间存在m个关系对，关系具有传递性，假如A关注B，B关注C，那么A就间接关注了C。如果一个人被除他之外的所有人都直接或间接关注，那么这个人就是抖音红人，求抖音红人的总数  

21.两个单链表找到第一个公共结点  

22.由0和1组成的二维矩阵，找出1的最大连通域，计算其面积  

23.长度为n的字符串中包含m个不同的字符，找出包含这m个不同字符的最小子串  

24.如果用数组实现，数组初始容量为n，每次push到容量上限之后都扩容到原来的两倍，现在push进去m个数，m远大于n，求相比于m的时间复杂度  

25.下一个全排列  

26.长度为n的数组中有一个数字出现了n/2次，快速找到这个数  

27.1）时间上如何优化：dp（2）空间上如何优化：滚动数组  

28.带括号的加减乘除字符串运算  

29.棋盘上的连通棋子团数，（最基本的dfs）  

30.dfs的变种  

31.每个数组任选一个数字，相邻求差的绝对值，然后再求和求最小  

32.稀疏向量的点乘 要求：尽量高效地实现，需要同时考虑时空复杂度。

33.leetcode958  判断是否是完全二叉树  

34.leetcode3 最长不重复子串  

35.非递减数组中查询某个目标值出现个数。解法：二分查找左右边界。  

36.leetcode 124 二叉树最大路径和  

37.正则表达式匹配  

38.字符串的转换，假设存在两种命名规范, lossEntropy可转换为 loss_entroy， someLSTMPre转换为some_lstm_pre。实现函数完成前者到后者的转换。  

39.删除链表重复节点。如1-2-3-3-5-5-6 变为1-2-6  

40.int64 a b c 判断 a(加号， 打不出来。。。)b>c(考虑溢出问题)  

41.从用户的访问日志中，选出访问次数最多的topK的用户  

42.leetcode 856  

43.dfs非递归遍历  

44.相关链表的公共节点（要考虑不相交的情况）  

45.小兔的棋盘  

46.寻找迷宫中的最短路径，迷宫中1表示有墙，路不通，0表示可以走  

47.LeetCode 76. Minimum Window Substring. Hard  

48.一个正整数数组，寻找连续区间使得和等于target  

49.Path_sum（两个相关的变形）  

50.最长上升子序列  

51.机器人在矩阵中寻找路径的一个dfs的问题  

52.按层次遍历二叉树  

53.LEETCODE 448，要求时间o(n)，空间o(1)  

54.买卖股票一次的最大收益，LEETCODE 123  

55.买卖股票两次的最大收益，LEETCODE 123  

56.给一字符串，只包含（和），求最长连续子串  

57.给一个字符串，列出所有可能的ip组合  

58.k个有序链表合并  

59.给你一个中文数字，比如一百二十，如何转换为整形数字  

60.稀疏向量的点乘。先要我自定义存储的结构体，然后写函数头，再编程  

61.链表反转，迭代+递归两种都要写  

62.由长度为length的array表示的整数，允许相邻位数交换，求n步交换内能得到的最小整数。  

63.Leetcode #72（hard）, 字符串的编辑距离  

64.一亿个浮点数，大小不超过2^32，均匀分布在值域内，求最快的排序方法；分析排序方法的复杂度  

65.完全二叉树输出最后一个节点  

66.求股票的最大利润，例如[1, 3, 1, 8, 10, 3]，只能买卖一次，计算最大收益  

67.排序数组中绝对值不同的个数  

68.字符串转整数  

69.1，2，...，N中，字符1出现的次数  

70.判断a+b>c?要考虑溢出  

71.二叉树先序遍历序列+后序遍历序列输出后序遍历序列  
 
72.写一个计算sqrt的函数，不能使用库函数  

73.判断链表有环  

74.二叉树中序遍历  

75.给定一个二叉树，求出这个二叉树的宽度  

76.给定一个数组，找到这个数组中，和等于0的所有三元组  

77.排序算法主要哪几种，时间/空间复杂度，稳定性  

78.topk 说了一下堆排序  

79.排序数组中绝对值不相等的元素个数  
 
80.多元一次方程组的解的数目。背包的裸题  

81.数轴上有只蚂蚁，他在起点s处以每秒k步的速度在数轴上爬（k为负代表负方向）。让你找一种策略。总能找到这只蚂蚁  

82.Power(a,n) 常规递归方法写完让写一个O（1）的方法  

83.岛计数问题 dfs  

84.字符串最小编辑路径  

85.找完全二叉树最后一个节点  

86.找字典序的第k个数  

87.【LeetCode】148. 排序链表  

88.【LeetCode】215. 数组中的第K个最大元素  

89.接雨水  

90.阿拉伯数字转中文计数  

91.两个数字字符串相加  

92.组合总和  

93.稀疏向量的点乘 要求：尽量高效地实现，需要同时考虑时空复杂度。
  
94.找一个链表中的环  

95.代码实现卷积  

96.两数之和；三数之和；四数之和。  
链表由节点传成，每个节点分为数据域和指针域，数据域存放元素，指针域存放下一个节点的地址。
python没有指针，所有变量都是对象，因此只能模拟一个链表。
模拟的val就是节点数据，next就是下一个节点。
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = ListNode() # 保留完整的链表
        l3 = a  # 保留完整的链表
        c = 0  # 进位
        while l1 or l2:
            x=l1.val if l1 else 0  # 没有下一节点时取0
            y=l2.val if l2 else 0
            tmp = x+y
            if tmp+c <10:
                l3.next = ListNode(tmp+c)
                c=0  # 不进位，清零
            else:
                l3.next = ListNode(tmp+c-10)
                c=1  # 进位，进1
            # print(tmp)
            # print(l1)
            # print(l2)
            if l1:
                l1 = l1.next  # 进入链表的下一节点
            if l2:
                l2 = l2.next  # 进入链表的下一节点
            l3 = l3.next
        if c==1:
            l3.next = ListNode(1)  # 最后一个进位增加一个末尾节点，元素为1
        return a.next  # a的第一个是0，因此去头节点
```

97.绝对众数查找  

98.p = "abcdfg", q = "abcd"，找出p中包含q所有字符的最短子序列  

99.给定一个二维数组，其中包含元素为0~9，要求矩阵中所有元素为0的行和列，并将所有0元素所在的行和列也全部更新为0。  

100.最低公共祖先  

101.01矩阵中最大全1矩形的面积  

102.求和最大的连续子数组  

103.由长度为length的array表示的整数，允许相邻位数交换，求n步交换内能得到的最小整数。  

104.Leetcode #72（hard）, 字符串的编辑距离  

105.一亿个浮点数，大小不超过2^32，均匀分布在值域内，求最快的排序方法  

106.完全二叉树输出最后一个节点  

107.大数相加  

108.字符串最小编辑路径  
```python
# 递归
def Levenshtein_Distance_Recursive(str1, str2):
 
    if len(str1) == 0:
        return len(str2)
    elif len(str2) == 0:
        return len(str1)
    elif str1 == str2:
        return 0
 
    if str1[len(str1)-1] == str2[len(str2)-1]:
        d = 0
    else:
        d = 1
    
    return min(Levenshtein_Distance_Recursive(str1, str2[:-1]) + 1,
                Levenshtein_Distance_Recursive(str1[:-1], str2) + 1,
                Levenshtein_Distance_Recursive(str1[:-1], str2[:-1]) + d)
 
print(Levenshtein_Distance_Recursive("abc", "bd"))

# 动态规划
def Levenshtein_Distance(str1, str2):
    """
    计算字符串 str1 和 str2 的编辑距离
    :param str1
    :param str2
    :return:
    """
    matrix = [[ i + j for j in range(len(str2) + 1)] for i in range(len(str1) + 1)]
 
    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if(str1[i-1] == str2[j-1]):
                d = 0
            else:
                d = 1
            
            matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+d)
 
    return matrix[len(str1)][len(str2)]
 
 
print(Levenshtein_Distance("abc", "bd"))
```
