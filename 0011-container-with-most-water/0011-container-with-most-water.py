class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        area = 0
        while left < right:
            area = max(area, (right-left)*min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return area
        # length = len(height)
        # f = height[0]
        # fi = 0
        # s = height[length - 1]
        # si = length-1
        # area = min(f,s) * (si-fi)
        # for i in range(1, length-1):
        #     print("Hi")
        #     print(fi)
        #     print(si)
        #     if f < height[i]:
        #         f = height[i]
        #         fi = i
        #     area = max(min(f,s) * (si - fi), area)
        #     if s < height[length-i-1]:
        #         s = height[length-i-1]
        #         si = length-i-1
        #     area = max(min(f,s) * (si - fi), area)
        # return area
            
        """
        :type height: List[int]
        :rtype: int
        """
        