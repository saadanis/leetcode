"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        if j < len(nums2):
            merged = merged + nums2[j::]
        elif i < len(nums1):
            merged = merged + nums1[i::]
        
        if len(merged)%2 == 1:
            median = merged[len(merged) // 2]
        else:
            median = (merged[len(merged) // 2] + merged[(len(merged) // 2) - 1]) / 2

        return median