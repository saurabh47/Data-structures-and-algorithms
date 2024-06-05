### Problem 1442. Count Triplets That Can Form Two Arrays of Equal XOR (Medium): https://leetcode.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor/

### Tags: Array, Bit Manipulation

# Time Complexity: O(n^3)
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        count = 0
        for i in range(len(arr)):
            a = 0
            for j in range(i + 1 ,len(arr)):
                a = a ^ arr[j-1] 
                b = 0
                for k in range(j ,len(arr)):
                    b = b ^ arr[k] 
                    if(a==b):
                        count +=1
        return count