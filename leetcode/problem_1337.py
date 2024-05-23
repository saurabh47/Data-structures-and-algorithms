### Problem 1337. The K Weakest Rows in a Matrix (Easy)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = {}

        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if(j == 1):
                    count += 1
                else:
                    break
            soldiers[i] = count
        print(soldiers)
        # return index of k smallest elements
        sorted_soldiers = dict(sorted(soldiers.items(), key = lambda items: items[1]))
        result = []
        for key, value in sorted_soldiers.items():
            if(k < 1):
                break
            result.append(key)
            k -= 1
        return result

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = {}

        for i in range(len(mat)):
            count = 0
            for j in mat[i]:
                if(j == 1):
                    count += 1
                else:
                    break
            soldiers[i] = count
        print(soldiers)
        # return index of k smallest elements
        priority_queue = []
        for key, value in soldiers.items():
            pair = (value, key)
            heapq.heappush(priority_queue, pair)
        weakest = heapq.nsmallest(k, priority_queue)
        result = []
        for pair in weakest:
            result.append(pair[1])
        return result
