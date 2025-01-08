### Problem 3042. Count Prefix and Suffix Pairs I
### tags: string, array, hashfunction
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if(self.isPrefixAndSuffix(words[i], words[j])):
                    count += 1
        return count

    def isPrefixAndSuffix(self, str1, str2):
        if(len(str2)< len(str1)):
            return  False
        else:
            n = len(str1)
            m = len(str2)
            pref = str2[0:n]
            suff = str2[m - n: m]
            return suff == pref == str1