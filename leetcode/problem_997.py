# Problem 997: Find the Town Judge (Easy): https://leetcode.com/problems/find-the-town-judge/description/

### tags: Graph, Directed Graph, Indegree, Outdegree

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = [0 for i in range(n+1)]
        for out, inc in trust:
            delta[out] -= 1
            delta[inc] += 1
        
        for i in range(1, n+1):
            if(delta[i] == n-1):
                return i
        return -1

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        delta = defaultdict(int)
        for edge in trust:
            delta[edge[1]] += 1
            delta[edge[0]] -= 1
        
        for i in range(1, n+1):
            if(delta[i] == n-1):
                return i
        return -1

class Solution:
    def findJudge(self, n: int, trust) -> int:
        judge = -1
        if(len(trust) == 0):
            if n == 1:
                return 1
            else:
                return judge

        incoming = [0 for _ in range(n)]
        outgoing = [0 for _ in range(n)]
        for edge in trust:
            out_edge = edge[0]
            in_edge = edge[1]
            incoming[in_edge - 1] += 1
            outgoing[out_edge - 1] += 1
        for i in range(n):
            if(incoming[i] == n-1 and outgoing[i]==0):
                judge = i+1
        return judge



if __name__ == "__main__":
    solution = Solution()
    trust = [[1,3],[2,3],[3,1]]
    n = 3
    print(solution.findJudge(n,trust),"Expected") # 3
    trust = [[1,3],[2,3]]
    n = 3
    print(solution.findJudge(n,trust)) # 3
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    n = 4
    print(solution.findJudge(n,trust)) # 3
    trust = [[1,2],[2,3]]
    n = 3
    print(solution.findJudge(n,trust)) # -1
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    n = 4
    print(solution.findJudge(n,trust)) # 3
    trust = []
    n = 1
    print(solution.findJudge(n,trust)) # 1
    trust = [[1,2]]
    n = 2
    print(solution.findJudge(n,trust)) # 2
    trust = [[1,2],[2,3]]
    n = 3
    print(solution.findJudge(n,trust)) # -1
    trust = [[1,3],[2,3],[3,1]]
    n = 3
    print(solution.findJudge(n,trust)) # 3
    trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
    n = 4
    print(solution.findJudge(n,trust)) # 3
