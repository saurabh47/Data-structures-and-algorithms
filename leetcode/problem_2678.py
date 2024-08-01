### Problem 2678. Number of Senior Citizens

### Tags: Array, String

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for passenger in details:
            age = passenger[11:13]
            if(int(age[0]) > 6):
                count +=1
            elif(age[0] == '6' and age[1] != '0'):
                count+=1
        return count