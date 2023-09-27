class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freqS1 = {}
        freqS2 = {}
        for i in range(len(s1)):
            if(s1[i] in freqS1):
                freqS1[s1[i]] += 1
            else:
                freqS1[s1[i]] = 1
        for i in range(len(s2)):
            if(s2[i] in freqS2):
                freqS2[s2[i]] += 1
            else:
                freqS2[s2[i]] = 1
            if(i >= len(s1)):
                overflowedIndex = i - len(s1)
                if(freqS2[s2[overflowedIndex]] == 1):
                    del freqS2[s2[overflowedIndex]]
                else:
                    freqS2[s2[overflowedIndex]] -= 1
            print(freqS1, freqS2)
            if(freqS1 == freqS2):
                return True
        return False


if __name__ == "__main__":
    print(Solution().checkInclusion("ab", "eidbaooo"))