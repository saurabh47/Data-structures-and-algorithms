# Problem 771. Jewels and Stones (Easy): https://leetcode.com/problems/jewels-and-stones/
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew_map = {} 
        for j in jewels:
            if j not in jew_map:
                jew_map[j] = 1
            else:
                jew_map[j] += 1
        count = 0
        for stone in stones:
            if stone in jew_map:
                count +=1
        return count

# Time complexity: O(n)
# Space complexity: O(n)

if __name__ == '__main__':
    s = Solution()
    print(s.numJewelsInStones("aA","aAAbbbb")) # 3
    print(s.numJewelsInStones("z","ZZ")) # 0
    print(s.numJewelsInStones("a","A")) # 0
    print(s.numJewelsInStones("a","a")) # 1
    print(s.numJewelsInStones("a","")) # 0
