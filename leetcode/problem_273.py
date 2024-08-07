### Problem 273. Integer to English Words
### tags: Math, String, Recursion
class Solution:
    def numberToWords(self, num: int) -> str:
        def build_hundreds(n):
            result = []
            # 372, 
            # 007
            # 000
            # 111
            o, t = n % 10, n % 100
            n = n // 100
            if(n > 0):
                result.append(ones[n] + " Hundred")
            if(t > 0 and t < 20):
                result.append(ones[t])
            else:
                t = (t // 10)
                if(t > 0):
                    result.append(tens[t])
                if(o > 0):
                    result.append(ones[o])
            return " ".join(result)
        ones = ["Zero", "One", "Two", "Three", "Four", "Five", "Six","Seven","Eight","Nine", "Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens = ["Zero", "Ten", "Twenty", "Thirty","Forty","Fifty","Sixty","Seventy","Eighty", "Ninety"]
        if(num < 20):
            return ones[num]
        places = ["", " Thousand", " Million", " Billion"]
        result = []
        i = 0
        while(num):
            rem = num % 1000
            res = build_hundreds(rem)
            if(res):
                result.append(res + places[i])
            num = num // 1000
            i += 1
        result.reverse()
        return " ".join(result)
