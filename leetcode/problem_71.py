### Problem 71. Simplify Path
### tags: stack
### company: Meta

# The idea is to use a stack to keep track of the path
# We split the path by "/" and then iterate through the parts
# If the part is "." or "", we continue
# If the part is "..", we pop the last element from the stack
# Otherwise, we push the part onto the stack
class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split("/")
        stack = []
        # /home/user/Documents/../Pictures"
        # [home, user, Documents,..,Pictures]
        for part in parts:
            if(part == "." or part ==""):
                continue
            elif(part == ".."):
                if(len(stack) > 0):
                    stack.pop()
            else:
                stack.append(part)
        return "/" + "/".join(stack)