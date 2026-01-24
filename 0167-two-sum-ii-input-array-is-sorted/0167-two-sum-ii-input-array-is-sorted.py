class Solution(object):
    def twoSum(self, numbers, target):
        res = []
        arr = list(set(numbers))
        arr.sort()
        for i,n in enumerate(arr):
            left = target - n
            if left in arr:
                first = numbers.index(n)
                second = numbers.index(left)
                if first == second:
                    second += 1
                return[first+1,second+1]
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        