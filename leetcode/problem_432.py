### Problem 432. All O`one Data Structure (Hard): https://leetcode.com/problems/all-oone-data-structure/
### tags: Design, Hash Table, Doubly Linked List

class AllOne:
    def __init__(self):
        self.keys = {}

    def inc(self, key: str) -> None:
        if(key in self.keys):
            self.keys[key] += 1
        else:
            self.keys[key] = 1

    def dec(self, key: str) -> None:
        if(key in self.keys):
            self.keys[key] -= 1
        if(self.keys[key] <= 0):
            self.keys.pop(key)

    def getMaxKey(self) -> str:
        if(len(self.keys) == 0):
            return ""
        maxVal, maxKey = 0, ""
        for key, val in self.keys.items():
            if(val > maxVal):
                maxKey = key
                maxVal = val
        return maxKey

    def getMinKey(self) -> str:
        if(len(self.keys) == 0):
            return ""
        minVal, minKey = 10**5, ""
        for key, val in self.keys.items():
            if(val < minVal):
                minKey = key
                minVal = val
        return minKey