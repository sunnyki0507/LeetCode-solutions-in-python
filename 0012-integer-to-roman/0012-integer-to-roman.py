class Solution(object):
    def intToRoman(self, num):
        roman = {}
        roman[1] = 'I'
        roman[4] = 'IV'
        roman[5] = 'V'
        roman[9] = 'IX'
        roman[10] = 'X'
        roman[40] = 'XL'
        roman[50] = 'L'
        roman[90] = 'XC'
        roman[100] = 'C'
        roman[400] = 'CD'
        roman[500] = 'D'
        roman[900] = 'CM'
        roman[1000] = 'M'
        string = ""

        strNum = str(num)
        length = len(strNum)
        for i in range(length):
            n = int(strNum[i])
            unit = 10 ** (length-1-i)
            if n < 5:
                if n == 4:
                    string += roman[n*unit]
                    continue
                string += (roman[unit] * n)
                continue
            if n == 9:
                string += roman[n*unit]
                continue
            string += roman[unit*5]
            n = n-5
            string += (roman[unit] * n)

        return string

        """
        :type num: int
        :rtype: str
        """
        