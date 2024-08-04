#
'''
Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	    1
V	    5
X	    10
L   	50
C   	100
D	    500
M	    1000
'''


class Solution:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        result = []

        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                result.append(symbols[i])

        return ''.join(result)