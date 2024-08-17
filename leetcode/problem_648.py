### Problem 648. Replace Words (Medium)
### Tags: Array, Hash Table, String, Trie
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        sentence = sentence.split(' ')
        # print("sentence=", sentence)
        for root in dictionary:
            minlength = len(root)
            for i in range(len(sentence)):
                word = sentence[i]
                #  we don't have to check for 
                # length, isRoot will return false
                # if word is already short than root  
                if(self.isRoot(root, word)):
                   sentence[i] = root
        # print("resulting sentence=", sentence)
        return ' '.join(sentence)
        

    def isRoot(self, root, word):
        if(len(root) > len(word)):
            return False
        result = True
        for i in range(len(root)):
            if(root[i] != word[i]):
                result = False
                break
        return result