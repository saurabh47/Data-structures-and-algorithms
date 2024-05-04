# Problem  12. Integer to Roman (Medium): https://leetcode.com/problems/integer-to-roman/
class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M",
        }
        keys = list(symbols.keys())
        i = len(symbols) -1 
        result = '';
        while(num != 0):
            # 1994 > 1000 = M
            # 994 > 500 
            if(num >= keys[i]):
                if(num >= 4 and num < 5):
                    result += 'IV'
                    num -= 4
                elif(num >= 9 and num < 10):
                    result += 'IX'
                    num -= 9
                elif(num >= 40  and num < 50):
                    result += 'XL'
                    num -= 40
                elif(num >= 90 and num < 100):
                    result += 'XC'
                    num -= 90
                elif(num >= 400 and num < 500):
                    result += 'CD'
                    num -= 400
                elif(num >= 900 and num <1000):
                    result += 'CM'
                    num -= 900
                else:
                    result += symbols[keys[i]]
                    num -= keys[i]
            else:
                i -= 1
        return result


class Solution2:
    def intToRoman(self, num: int) -> str:
        symbols = {
            1 : "I",
            4 : "IV", #added
            5 : "V",
            9 : "IX", #added
            10 : "X",
            40 : "XL", #added
            50 : "L",
            90 : "XC", #added
            100 : "C",
            400 : "CD", #added
            500 : "D",
            900 : "CM", #added
            1000 : "M",
        }
        keys = list(symbols.keys())
        result = '';
        k = len(keys) - 1
        for i in range(len(symbols)-1, -1, -1):
            k = i
            while (num >= keys[k]):
                num = num - keys[k]
                result += symbols[keys[i]]
        return result

if __name__ == "__main__":
    num = 3
    print(Solution().intToRoman(num)) # III
    print(Solution2().intToRoman(num)) # III
    num = 4
    print(Solution().intToRoman(num)) # IV
    print(Solution2().intToRoman(num)) # IV
    num = 9
    print(Solution().intToRoman(num)) # IX
    print(Solution2().intToRoman(num)) # IX
    num = 58
    print(Solution().intToRoman(num)) # LVIII
    print(Solution2().intToRoman(num)) # LVIII
    num = 1994
    print(Solution().intToRoman(num)) # MCMXCIV
    print(Solution2().intToRoman(num)) # MCMXCIV
    num = 3999
    print(Solution().intToRoman(num)) # MMMCMXCIX
    print(Solution2().intToRoman(num)) # MMMCMXCIX
    num = 399
    print(Solution().intToRoman(num)) # CCCXCIX
    print(Solution2().intToRoman(num)) # CCCXCIX
    num = 3990
    print(Solution().intToRoman(num)) # MMMCMXC
    print(Solution2().intToRoman(num)) # MMMCMXC
    num = 39900
    print(Solution().intToRoman(num)) # MMM