# Problem 49: Group Anagrams (Medium): https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs):
        result = {}
        grouped = []
        for i in range(len(strs)):
            word = strs[i]
            sortedWord = "".join(sorted(word))
            if(sortedWord not in result):
                result[sortedWord] = [word]
            else:
                result[sortedWord].append(word)
        return list(result.values())

# hint: sort each character and map to a key
class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookUp = {}    
        result = []
        for i, s in enumerate(strs):
            sorted_s = ''.join(sorted(s, key=lambda x: ord(x)))
            if(sorted_s in lookUp):
                lookUp[sorted_s].append(s)
            else:
                lookUp[sorted_s] = [s]
        for key, value in lookUp.items():
            result.append(value)
        return result


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs)) # [["ate","eat","tea"],["nat","tan"],["bat"]]