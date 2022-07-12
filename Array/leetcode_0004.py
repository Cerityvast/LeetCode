from typing import List

# 暴力解
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        array = [0] * (m + n)
        start, i, j = 0, 0, 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                array[start] = nums1[i]
                i += 1
            else:
                array[start] = nums2[j]
                j += 1
            start += 1
        array[start:] = nums1[i:] if i < m else nums2[j:]
        return array[(m + n)//2] if (m+n) % 2 == 1 else (array[int((m+n)/2 - 1)] + array[int((m+n)/2)]) / 2


# 无需合并为新数组，仅需找出中位数对应位置元素
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        length = m + n
        left, right = -1, -1
        start1, start2 = 0, 0
        for i in range(length//2+1):
            left = right
            if start1 < m and (start2 >= n or nums1[start1] < nums2[start2]):
                right = nums1[start1]
                start1 += 1
            else:
                right = nums2[start2]
                start2 += 1
        if length % 2 == 1:
            return right
        else:
            return (left + right) / 2

# 采用二分查找, 每次最多筛除k-1小的数（两个数组仅比较第k//2 -1大小，即可排除较小的k//2个数）
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def getKthElement(k: int) -> int:
            start1, start2 = 0, 0
            while True:
                # 第一个数组为空，直接返回第二个数组的第K元素
                if start1 == m:
                    return nums2[start2 + k - 1]
                # 第二个数组为空，直接返回第一个数组的第K元素
                if start2 == n:
                    return nums1[start1 + k - 1]
                # 当k为1时即返回两个数组中最小的元素，仅需比较两个数组第一个元素
                if k == 1:
                    return min(nums1[start1], nums2[start2])
                # 设定两个数组第k//2 -1的索引，k//2-1超过数组长度时定义为数组的最后一个位置
                newstart1 = min(start1 + k // 2 - 1, m - 1)
                newstart2 = min(start2 + k // 2 - 1, n - 1)
                # 删除较小数组的k//2个数，并重新设定数组起始索引
                if nums1[newstart1] < nums2[newstart2]:
                    k -= newstart1 - start1 + 1
                    start1 = newstart1 + 1
                else:
                    k -= newstart2 - start2 + 1
                    start2 = newstart2 + 1
        m, n = len(nums1), len(nums2)
        length = m + n
        # 分奇偶情况讨论
        if length % 2 == 1:
            return getKthElement(length // 2 + 1)
        else:
            return (getKthElement(length // 2) + getKthElement(length // 2 + 1)) / 2