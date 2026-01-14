class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            erase = nums.index(val)
            nums.pop(erase)
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        