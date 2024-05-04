# Problem 706. Design HashMap (Easy): https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.hashMap = []

    def put(self, key: int, value: int) -> None:
        mapArr = [key, value] 
        if(len(self.hashMap) == 0):
            self.hashMap.append(mapArr)
            return
        for i in range(len(self.hashMap)):
            if(key == self.hashMap[i][0]):
                self.hashMap[i][1] = value
                return;
        self.hashMap.append(mapArr)

    def get(self, key: int) -> int:
        if(len(self.hashMap) == 0):
            return -1
        for i in range(len(self.hashMap)):
            if(key == self.hashMap[i][0]):
                return self.hashMap[i][1]
        return -1

    def remove(self, key: int) -> None:
        for i in range(len(self.hashMap)):
            if(key == self.hashMap[i][0]):
                del self.hashMap[i]
                break;

    def __repr__(self):
        return self.hashMap.__repr__()

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

if __name__ == "__main__":
    obj = MyHashMap()
    obj.put(1, 1)
    obj.put(2, 2)
    print(obj.get(1)) # 1
    print(obj.get(3)) # -1
    obj.put(2, 1)
    print(obj.get(2)) # 1
    obj.remove(2)
    print(obj.get(2)) # -1
    obj.put(3, 2)
    print(obj.get(3)) # 2
    obj.remove(3)
    print(obj.get(3)) # -1
    print(obj)