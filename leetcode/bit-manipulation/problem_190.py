class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        count = 0
        while(count < 32):
            # legft shift reverse by 1 bit
            reverse = reverse << 1;
            # add lsb of n to reverse using Bitwise OR
            reverse = reverse | (n & 1);
            # divide n by 2 using Bitwise right shift
            n = n >> 1 ;
            count += 1
        return reverse
      
