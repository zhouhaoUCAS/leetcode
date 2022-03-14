"""
递归算法：

二分法变成log N算法复杂度

"""

"""
一、 寻找两个正序数组的中位数
给定两个大小分别为 m 和 n 的正序（从小到大）数组nums1 和nums2。请你找出并返回这两个正序数组的 中位数 。
"""

from typing import List


class Solution:  # 二分法找第K小
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1 = 0
        left2 = 0
        length1 = len(nums1)
        length2 = len(nums2)
        # 先考虑极端情况
        if length1 == 0:
            return (nums2[length2 // 2] + nums2[length2 // 2 + (length2 % 2 - 1)]) / 2
        if length2 == 0:
            return (nums1[length1 // 2] + nums1[length1 // 2 + (length1 % 2 - 1)]) / 2
        # 偶数向下取整
        mid_num = (length1 + length2) // 2 + (length1 + length2) % 2
        mid_num_add = 1 - (length1 + length2) % 2
        return (self.get_k_value(mid_num, nums1, nums2, left1, left2, length1, length2) + self.get_k_value(
            mid_num + mid_num_add, nums1, nums2, left1, left2, length1, length2)) / 2

    def get_k_value(self, mid_num, nums1, nums2, left1, left2, length1, length2):
        while True:
            update1 = min(mid_num // 2, length1)
            update2 = min(mid_num // 2, length2)
            if nums1[update1 + left1 - 1] <= nums2[update2 + left2 - 1]:
                left1 = left1 + update1
                length1 = length1 - update1
                mid_num = mid_num - update1
            else:
                left2 = left2 + update2
                length2 = length2 - update2
                mid_num = mid_num - update2
            # 先考虑极端情况
            if length1 == 0:
                return nums2[mid_num + left2 - 1]
            if length2 == 0:
                return nums1[mid_num + left1 - 1]
            if mid_num == 1:
                return min(nums1[left1], nums2[left2])
            return self.get_k_value(mid_num, nums1, nums2, left1, left2, length1, length2)


class Solution1:  # 二分法更新值
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        left1 = 0
        left2 = 0
        right1, m = len(nums1), len(nums1)
        right2, n = len(nums2), len(nums2)

        # 保证nums1 长度小于nums2
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        while left1 <= right1:
            i = (left1 + right1) // 2
            j = (m + n + 1)//2 - i
            if (i != 0) & (i != m) & (nums2[j-1] > nums1[i]):
                left1 = i + 1
            elif (j != 0) & (j != n) & (nums2[j] < nums1[i-1]):
                right1 = i - 1
            else:
                # 先考虑极端情况
                if i == 0:
                    max_left = nums2[j-1]
                elif j == 0:
                    max_left = nums1[i-1]
                else:
                    max_left = max(nums2[j-1], nums1[i-1])
                if (m+n) % 2 == 1:
                    return max_left
                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums2[j], nums1[i])
                return (max_left+min_right)/2
