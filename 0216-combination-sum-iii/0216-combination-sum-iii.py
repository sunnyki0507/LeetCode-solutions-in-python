class Solution(object):
    def combinationSum3(self, k, n):
        def backtracking(start, pairs):
            if sum(pairs) is not n and len(pairs) == k:
                return
            if sum(pairs) > n or len(pairs) > k:
                return
            if sum(pairs) == n and len(pairs) == k:
                print("Hello")
                result.append(pairs[:])
                return     
            for i in range(start, 10):
                if (len(pairs) + (10-start)) < k:
                    return
                pairs.append(i)
                # print(pairs)
                backtracking(i + 1, pairs)
                pairs.pop()
                # print(pairs)
        j = 0
        result = []
        backtracking(1, [])
        print("Hello2")
        print(result)
        return result

        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        