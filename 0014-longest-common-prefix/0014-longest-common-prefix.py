class Solution(object):
    def longestCommonPrefix(self, strs):
        short = min(strs, key=len)
        prefix = ""
        match = True
        for i in range(len(short)):
            for j in strs:
                if short[i] != j[i]:
                    match = False
            if match:
                prefix += short[i]
            else:
                break
        return prefix
        # short = min(strs, key=len)
        # exist = [1] * len(short)
        # for i in range(len(short)):
        #     for j in strs:
        #         if short[i] in j:
        #             continue
        #         else:
        #             exist[i] = 0
        #             break
        # result = ""
        # out = []
        # print(exist)
        # for i, c in enumerate(exist):
        #     if c == 1:
        #         result += short[i]
        #     else:
        #         result = ""
        #     out.append(result)
        # print(out)
        # if not out:
        #     return ""
        # return max(out, key=len)
        """
        :type strs: List[str]
        :rtype: str
        """
        