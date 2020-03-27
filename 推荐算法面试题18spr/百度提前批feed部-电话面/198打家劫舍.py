https://leetcode-cn.com/problems/house-robber
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        length = len(nums)
        if length == 1:
            return nums[0]
        else:
            prev = nums[0]
            cur = max(prev, nums[1])
            for i in range(2, length):
                cur, prev = max(prev + nums[i], cur), cur
            return cur
