class Solution(object):
    def rotate(self, nums, k):
        l = k % len(nums)
        if l < 1:
            return
        nums.reverse()
        for i in range(int(l/2)):
            print(int(k/2))
            first = nums[i]
            last = nums[l-1-i]
            nums[i] = last
            nums[l-i-1] = first
        j = 1
        for i in range(l, ((len(nums)-l)/2)+l):
            print(i)
            first = nums[i]
            last = nums[len(nums)-j]
            nums[i] = last
            nums[len(nums)-j] = first
            j += 1





        # left = k % len(nums)
        # print(left)
        # if left<(len(nums)/2):
        #     for i in range(left):
        #         add = nums.pop()
        #         nums.insert(0, add)
        # else:
        #     for i in range(len(nums) - left):
        #         add = nums.pop(0)
        #         nums.append(add)


        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        