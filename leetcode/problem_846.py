### Problem 846. Hand of Straights (Medium): https://leetcode.com/problems/hand-of-straights/
### Tags: Hash Table, Array, Greedy

### Hint:We
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = {}
        min_heap = []
        if(len(hand) % groupSize != 0):
            return False
        for number in hand:
            if(number not in freq):
                freq[number] = 1
            else:
                freq[number] += 1
        unique = sorted(list(freq.keys()))
        for num in unique:
            heapq.heappush(min_heap, num)
        result = True
        while(min_heap):
            minimum = min_heap[0]
            for j in range(minimum, minimum + groupSize):
                # we don't need to check for first element in group
                if(j in freq and freq[j] > 0):
                    freq[j]-= 1
                    if(freq[j] == 0):
                        # If the item to pop is not minimum
                        if(min_heap[0] != j):
                            return False
                        else:
                            heapq.heappop(min_heap)
                else:
                    result = False
                    break
        return result
