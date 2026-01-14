class Solution(object):
    def removeDuplicates(self, nums):
        nums.sort()
        if len(nums) < 2:
            return
        prev = nums[0]
        new = []
        idx = []
        for i in range(1, len(nums)):
            if prev == nums[i]:
                new.append(i)
            prev = nums[i]
        while new:
            nums.pop(new.pop())

                


        """
        :type nums: List[int]
        :rtype: int
        """
        