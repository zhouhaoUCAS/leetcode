"""
动态规划——运筹学的一个分支， 求解决策过程最优化的结果

    最重要的是定义初始状态、和状态转移方程； 空间换时间

"""

"""
一、最大回文子串
给你一个字符串s，找到s中的最长的回文子串
"""

# 1. 动态规划 2. 中心扩散法



# 中心扩散法——递归； 时间复杂度——O(N^2); 空间复杂度: O(1)，只使用到常数个临时变量，与字符串长度无关

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        result_length = -1

        for index_i in range(length):
            i, j = 0, 0
            if (index_i + 1 < length) and (s[index_i] == s[index_i + 1]):
                i, j = self.recursion_method(s, index_i, i + 1, j, length)
            if i - j + 1 > result_length:
                result = s[index_i + j: index_i + i + 1]
                result_length = i - j + 1
            i, j = 0, 0
            if (index_i + 2 < length) and (s[index_i] == s[index_i + 2]):
                i, j = self.recursion_method(s, index_i, i + 2, j, length)
            if i - j + 1 > result_length:
                result = s[index_i + j: index_i + i + 1]
                result_length = i - j + 1
        return result

    def recursion_method(self, s, index_i, i, j, length):
        if ((index_i + j - 1) < 0) or ((index_i + i + 1) >= length):
            return i, j
        if s[index_i + j - 1] == s[index_i + i + 1]:
            j = j - 1
            i = i + 1
            return self.recursion_method(s, index_i, i, j, length)
        return i, j