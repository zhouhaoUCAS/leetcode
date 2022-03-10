"""
一、给定一个字符串 s ，请你找出其中不含有重复字符的最长子串的长度。
"""

# 1.滑动窗口 2.hash


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result_set = set()
        result = 0
        left = 0  # 记录当前指针开始
        for i in range(len(s)):
            while s[i] in result_set:  # 从左直到删到不存在重复元素
                result_set.remove(s[left])
                left += 1
            result_set.add(s[i])
            result = max(result, len(result_set))
        return result


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_dict = {}
        result = 0
        j = -1  # 记录当前指针开始， 为0如果” “字符则为错
        for i in range(len(s)):
            if s[i] in hash_dict:
                j = max(j, hash_dict[s[i]])  # 两指针之间才更新
            hash_dict[s[i]] = i
            result = max(result, i-j)
        return result
