### 2559. Count Vowel Strings in Ranges
### tags: prefix sum, array
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        result = []
        vowels = ['a', 'e', 'i', 'o', 'u']
        prefix_vowels = []
        
        def isVowel(i):
            return words[i][0] in vowels and words[i][-1] in vowels
        prefix_vowels.append(1 if isVowel(0) else 0)
        
        for i in range(1, len(words)):
                w =  1 if isVowel(i) else 0
                prefix_vowels.append(prefix_vowels[i-1] + w)
        print(prefix_vowels)
        
        for s, e in queries:
            c = 1 if isVowel(s) else 0
            result.append(prefix_vowels[e] - prefix_vowels[s] +  c)
        return result