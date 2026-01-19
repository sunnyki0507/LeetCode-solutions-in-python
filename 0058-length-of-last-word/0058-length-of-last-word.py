class Solution(object):
    def lengthOfLastWord(self, s):
        rev = "".join(reversed(s))
        length = 0
        for i in rev:
            if i == ' ' and length == 0:
                continue
            if i == ' ':
                return length
            else:
                length += 1
        return length
        """
        :type s: str
        :rtype: int
        """
        