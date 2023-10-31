"""
https://leetcode.com/problems/merge-sorted-array/description/
"""

from typing import List

class Solution:
    def merge_1attempt(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # должно равняться n
        nums1_tail_to_remove = len(nums1) - m

        idx1 = 0
        idx2 = 0
        while idx2 < n:
            # дошли до конца первого массива
            # ИЛИ нашли место для вставки элемента из второго массива
            if idx1 == m or nums1[idx1] >= nums2[idx2]:
                nums1.insert(idx1, nums2[idx2])

                idx1 += 1
                m += 1
                idx2 += 1

                continue

            idx1 += 1

        # в конце удалим нули
        for _ in range(nums1_tail_to_remove):
            nums1.pop()

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]

        nums1.sort()
