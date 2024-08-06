### Problem 3016.Minimum Number of Pushes to Type Word II (Medium)
### tags: greedy, string, sorting, counter, hashmap
class Solution:
    def minimumPushes(self, word: str) -> int:
        maps = {}
        visited = [False for i in range(26)]
        freq = Counter(word)
        sorted_freq = sorted(freq.items(), key=lambda item: item[1], reverse=True)
        count = 0
        tap = 1
        taps = 0
        for i in range(len(sorted_freq)):
            if(count % 8 == 0 and count != 0):
                tap += 1
            taps += (tap * sorted_freq[i][1])
            count += 1
        return taps