class Solution(object):
    def threeSum(self, nums):
        # nums = list(set(nums))
        nums.sort()
        res = []
        length = len(nums)

        for i in range(length-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = length - 1
            s = nums[i]
            while left < right:
                s += nums[left]
                s += nums[right]
                if s == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    s -= (nums[left] + nums[right])
                    left += 1
                    right -= 1

                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
                elif s < 0:
                    s -= nums[left] + nums[right]
                    left += 1
                    while left<right and nums[left] == nums[left-1]:
                        left += 1
                else:
                    s -= nums[left] + nums[right]
                    right -= 1
                    while left<right and nums[right] == nums[right+1]:
                        right -= 1
        return res


        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        