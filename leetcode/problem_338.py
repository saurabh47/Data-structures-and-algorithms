### 338. Counting Bits

### Tags: Dynamic Programming, Bit Manipulation
class Solution:
    def countBits(self, n: int) -> List[int]:
        # f(n) gives number of bits in n
        # f(0) -> 0000 => 0
        # f(1) -> 0001 => f(0) + (1 if odd) => 1
        # f(2) -> 0010 => f(1) + (1 if odd) => 1
        # f(3) -> 0011 => f(1) + (1 if odd) => 2
        # f(4) -> 0100 => f(2) + (1 if odd) => 1
        # f(5) -> 0101 => f(2) + (1 if odd) => 2
        # f(6) -> 0110 => f(3) + (1 if odd) => 2
        result = [0]
        for num in range(1, n+1):
            number_of_bits = result[num >> 1] + (num & 1);
            result.append(number_of_bits)
        return result

class Solution2:
    def countBits(self, n: int) -> List[int]:
        result = []
        for number in range(n+1):
            if(number == 0):
                result.append(0)
            else:
                offset = 1 << int(floor(log(number, 2)))
                result.append(1 + result[number-offset])
        return result

class Solution3:
    def countBits(self, n: int) -> List[int]:
        result = []
        for number in range(n+1):
            result.append(0)

        for number in range(n+1):
            target = number
            count = 0
            while(target !=0):
                if(target & 1 == 1):
                    count+=1
                target = target >> 1
            result[number] = count
        return result