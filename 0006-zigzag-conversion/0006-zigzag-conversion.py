class Solution(object):
    def convert(self, s, numRows):
        row = [[] for _ in range(numRows)]
        idx = -1
        add = 1
        if numRows == 1:
            return s
        for i in s:
            idx += add
            if idx == 0:
                add = 1
            if idx == (numRows - 1):
                add = -1
            row[idx].append(i)

        return "".join("".join(inner) for inner in row)

        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        