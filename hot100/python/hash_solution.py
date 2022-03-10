"""
哈希表:
    1. 散列表（Hash table，也叫哈希表），是根据关键码值(Key value)而直接进行访问的数据结构。
    2. 它通过把关键码值映射到表中一个位置来访问记录，以加快查找的速度。这个映射函数叫做散列函数，存放记录的数组叫做散列表。
    3. 给定表M，存在函数f(key)，对任意给定的关键字值key，代入函数后若能得到包含该关键字的记录在表中的地址，则称表M为哈希(Hash）表，
       函数f(key)为哈希(Hash) 函数。

"""


"""
一、两数之和
给定一个整数数组 nums和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。
"""

from typing import List


class Solution(object):
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        hash_dict = {}  # python字典是由hash表实现，所以查询复杂度为O(1)
        for num_id, num in enumerate(nums):
            another_num = target - num
            if another_num in hash_dict:
                return [hash_dict[another_num], num_id]
            hash_dict[num] = num_id

Solution.two_sum([2, 7, 9, 11], 9)
