### Problem 207. Course Schedule (Medium): https://leetcode.com/problems/course-schedule/

### tags: graph, topological `sort, DFS, BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereq = {}
        visited = set()
        for course, pre in prerequisites:
            if(course not in prereq):
                prereq[course] = [pre]
            else:
                prereq[course].append(pre)
        
        for i in range(numCourses):
            if(i not in prereq):
                prereq[i] = []

        def take_course_dfs(c):
            # loop
            if(c in visited):
                return False
            # no prerequisite
            if(len(prereq[c]) == 0):
                return True
            visited.add(c)
            for p in prereq[c]:
                if(not take_course_dfs(p)):
                    return False
            visited.remove(c)
            prereq[c] = []
            return True

        for course in range(numCourses):
            if(not take_course_dfs(course)):
                return False
        return True