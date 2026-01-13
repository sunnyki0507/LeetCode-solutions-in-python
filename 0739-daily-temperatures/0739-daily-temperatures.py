class Solution(object):
    def dailyTemperatures(self, temperatures):
        nextB = []
        stack = []
        temp = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                idx = stack.pop()
                temp[idx] = i - idx
            stack.append(i)
        # for j,num in enumerate(temp):
        #     if num == 0:
        #         nextB.append(0)
        #     else:
        #         idx = temperatures.index(num, j+1)
        #         add = idx - j
        #         nextB.append(add)
        return temp
            


        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        