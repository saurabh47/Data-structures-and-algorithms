# Problem 380. Insert Delete GetRandom O(1) (Medium): https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:

    def __init__(self):
        self.arr = {}

    def insert(self, val: int) -> bool:
        if(val not in self.arr):
            self.arr[val] = val
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if(val not in self.arr):
            return False
        else:
            del self.arr[val]
            return True

    def getRandom(self) -> int:
        high = len(self.arr) - 1
        index = random.randint(0, high)
        return self.arr[list(self.arr.keys())[index]] 


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()