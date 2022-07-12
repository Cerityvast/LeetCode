from typing import List

# 暴力解（多次遍历数组）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 哈希表（一次遍历并记录遍历过元素）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for i, num in enumerate(nums):
        # 先判断后记录元素可防止遍历时num与自身匹配（当target为num两倍时）
            if target - num in hashtable:
                return [hashtable[target-num], i]
            hashtable[num] = i