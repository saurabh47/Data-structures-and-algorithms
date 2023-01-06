# Problem 49: Group Anagrams (Medium): https://leetcode.com/problems/group-anagrams/

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
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

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAnagrams(strs)) # [["ate","eat","tea"],["nat","tan"],["bat"]]