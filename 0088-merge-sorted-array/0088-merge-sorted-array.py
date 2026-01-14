class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if m == 0 and n == 0:
            return []
        if n == 0:
            nums1.sort()
        else:
            idx = 0
            for i in range(m, m+n):
                nums1[i] = nums2[idx]
                idx += 1
            nums1.sort()

        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        