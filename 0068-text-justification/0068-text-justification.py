class Solution(object):
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]
        # res = []
        # n = len(words)
        # i = 0
        # while i<n:
        #     j = i
        #     length = 0
        #     while j<n and length + len(words[j]) + j - i <= maxWidth:
        #         length += len(words[j])
        #         j += 1
        #     gap = maxWidth - length
        #     count = j-i-1
        #     add = ''
        #     if j == n or count == 0:
        #         for w in range(i, j):
        #             if w != (j-1):
        #                 add += words[w] + ' '
        #             else:
        #                 add += words[w] + ' '*(gap - count)
        #         res.append(add)
        #     else:
        #         each = gap//count
        #         extra = gap % count
        #         for w in range(i,j):
        #             if w != (j-1):
        #                 if extra > 0:
        #                     add += words[w] + ' ' * (each+1)
        #                 else:
        #                     add += words[w] + ' ' * each
        #             else:
        #                 add += words[w]
        #             extra -= 1
        #         res.append(add)
        #     i = j
        # return res


        # res = []
        # add = []
        # string = ""
        # for i in words:
        #     if len(string) == 0:
        #         string += i
        #         add.append(i)
        #         continue
        #     else:
        #         if (len(string) + len(i) + 1) <= maxWidth:
        #             string += " "
        #             string += i
        #             add.append(i)
        #         else:
        #             left = maxWidth - len(string)
        #             gap = len(add) - 1
        #             if gap == 0:
        #                 gap = 1
        #             for j in range(left):
        #                 add[j%gap] += " "
        #             res.append(" ".join(add))
        #             string = i
        #             add = []
        #             add.append(i)

        # if add:
        #     left = maxWidth - len(string)
        #     for j in range(left):
        #         string += " "
        #     res.append(string)
        # return res
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        