class Solution(object):
    def productExceptSelf(self, nums):
        answer = []
        front = []
        back = []
        fAdd = 1
        bAdd = 1
        length = len(nums)
        for i in range(len(nums)-1):
            fAdd *= nums[i]
            bAdd *= nums[length-1-i]
            front.append(fAdd)
            back.append(bAdd)

        back.reverse()
        back.append(1)
        front.insert(0,1)
        return [x*y for x,y in zip(front,back)]


            
            # if i == 0:
            #     answer.append(math.prod(nums[1:]))
            #     continue
            # if i == (len(nums) - 1):
            #     answer.append(math.prod(nums[:len(nums)-1]))
            #     continue
            # product = math.prod(nums[:i]) * math.prod(nums[i+1:])
            # answer.append(product)
        return answer
            
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        