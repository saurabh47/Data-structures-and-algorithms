### Problem 1598: Crawler Log Folder (Easy): https://leetcode.com/problems/crawler-log-folder/
### Tags: Array, String, Stack

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if(log == '../'):
                if(depth > 0):
                    depth -= 1
            elif(log == './'):
                pass
            else:
                depth += 1
        return depth