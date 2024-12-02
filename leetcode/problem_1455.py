### Problem 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence (Easy): https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/
### tags: strings, two pointers

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        wordCount = 0
        i = 0
        while(sentence[i] == ' '):
            sentence[i] = ''
            i += 1

        for i in range(len(sentence)):
            if(sentence[i - 1] == " " or i == 0):
                wordCount += 1
                k = i
                prefix = True
                j = 0
                while(j < len(searchWord) and k < len(sentence) and sentence[k] == searchWord[j]):
                    j += 1
                    k += 1
                if(j == len(searchWord)):
                    return wordCount
        return -1
                    
            
