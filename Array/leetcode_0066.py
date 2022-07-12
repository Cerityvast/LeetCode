from typing import List

# 将其转换为真实数字进行运算
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        nums = 0
        for i, num in enumerate(digits[::-1]):
            nums += 10**i * num
        new_nums = nums + 1
        return [int(c) for c in str(new_nums)]


# 按题意分析为两种情况：无进位时个位加1；有进位时低位置0高位加1（在所有位均进位时需额外添加最高位）
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            digits[i] += 1
            digits[i] %= 10
            if digits[i] != 0:
                return digits
        return [1] + digits