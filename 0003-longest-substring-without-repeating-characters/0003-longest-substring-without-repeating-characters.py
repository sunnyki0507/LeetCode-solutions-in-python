class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char = []
        maxL = 1
        if not s:
            return 0
        for i in s:
            if i in char:
                if maxL < len(char):
                    maxL = len(char)
                while i in char:
                    char.pop(0)
            char.append(i)
        if maxL < len(char):
            maxL = len(char)
        return maxL
        """
        :type s: str
        :rtype: int
        """
        