class Solution(object):
    def isSubsequence(self, s, t):
        idx = 0
        length = len(s)
        if not s:
            return True
        for i in t:
            if i == s[idx] and idx < length:
                idx += 1
            if idx >= length:
                return True
        return False
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        