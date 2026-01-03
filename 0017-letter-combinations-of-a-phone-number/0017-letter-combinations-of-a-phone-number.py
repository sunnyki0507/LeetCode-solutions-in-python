class Solution(object):
    def letterCombinations(self, digits):
        # arr = [[] for _ in range(10)]
        arr = []
        arr.append("abc")
        arr.append("def")
        arr.append("ghi")
        arr.append("jkl")
        arr.append("mno")
        arr.append("pqrs")
        arr.append("tuv")
        arr.append("wxyz")
        length = len(digits)
        tmp = deque()
        result = deque()
        for i in range(length):
            tmp.append(digits[i])
        # for j in range(length):
        while tmp:
            ch  = int(tmp.popleft()) - 2
            # print(ch)
            string = arr[ch]
            print(string)
            if not result:
                for c in string:
                    result.append(c)
                    print(c)
            else:
                iterN = len(result)
                for i in range(iterN):
                    change = result.popleft()
                    for st in string:
                        insert = change + st
                        print(insert)
                        result.append(insert)
        
        return list(result)
                        



        """
        :type digits: str
        :rtype: List[str]
        """
        