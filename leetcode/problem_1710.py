# Problem 1710. Maximum Units on a Truck (Easy): https://leetcode.com/problems/maximum-units-on-a-truck/
class Solution:
    def maximumUnits(self, boxTypes, truckSize):
        units = 0
        count = 0
        index = 0
        # sort boxes by number of Units per box
        sortedBoxes = self.sortBoxes(0,len(boxTypes)-1, boxTypes)
        # or
        # sort using lambda
        # boxTypes.sort(key=lambda x:x[1],reverse = True)
        while(count <= truckSize and index < len(sortedBoxes)):
            box = sortedBoxes[index][0]
            unitPerBox = sortedBoxes[index][1]
            if(count + box < truckSize):
                count += box
            else:
                box = truckSize - count
                count +=box
            units += box * unitPerBox
            index += 1
        return units

    def sortBoxes(self, start, end, box):
        result = []
        if(start == end):
            result.append(box[start])
            return result
        else:
            mid = (start + end)// 2
            left = self.sortBoxes(start, mid, box)
            right = self.sortBoxes(mid + 1, end, box)
            return self.merge(left,right)

    def merge(self, left, right):
        l = 0
        r = 0
        result = []
        while(l != len(left) and r != len(right)):
            if(left[l][1] > right[r][1]):
                result.append(left[l])
                l+=1
            else:
                result.append(right[r])
                r+=1
        if(l != len(left)):
            while(l != len(left)):
                result.append(left[l])
                l+=1
        else:
            while(r != len(right)):
                result.append(right[r])
                r+=1
        return result


if __name__ == "__main__":
    obj = Solution()
    print(obj.maximumUnits([[1,3],[2,2],[3,1]], 4)) # 8
    print(obj.maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)) # 91
    print(obj.maximumUnits([[1,3],[5,5],[2,5],[4,2],[4,1],[3,1],[2,2],[5,2],[5,3],[1,2],[2,5],[5,5]], 20)) # 66

