### Problem 1346. Check If N and Its Double Exist (Easy): https://leetcode.com/problems/check-if-n-and-its-double-exist/

### tags: array, hash table
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hmap = set()
        for i in range(len(arr)):
            num = arr[i]
            target = arr[i] * 2
            if(target not in hmap and num / 2 not in hmap):
                hmap.add(arr[i])
            else:
                return True
        return False
