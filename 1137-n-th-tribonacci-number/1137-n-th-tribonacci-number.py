class Solution(object):
    def tribonacci(self, n):
        # def dp(seq):
        #     if seq == 0:
        #         return 0
        #     elif seq <= 2:
        #         return 1
        #     return dp(seq - 1) + dp(seq - 2) + dp(seq - 3)
        arr = []
        arr.append(0)
        arr.append(1)
        arr.append(1)
        for i in range(3,n+1):
            arr.append(arr[i-1]+arr[i-2]+arr[i-3])
        print(arr)
        return arr[n]

        """
        :type n: int
        :rtype: int
        """
        