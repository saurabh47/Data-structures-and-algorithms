class Solution:
    def isCircularSentence(self, sentence: str) -> bool:

        # one word
        # first and last letter of sentence should be equal
        # if space at i > 0 i-1 and i + 1 should be equal
        # no leading or trailing space
        for i, letter in enumerate(sentence):
            if(sentence[i] == ' ' and i > 0 and sentence[i - 1] != sentence[i + 1]):
                return False
            elif(i == 0 and sentence[0] != sentence[-1]):
                return False
        return True