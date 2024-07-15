### Problem 2196. Create Binary Tree From Descriptions
#### Tags: Binary Tree, Tree, LeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        maps = {}
        parent = {}
        root = None
        for i in range(len(descriptions)):
            node = descriptions[i]
            node_root = None
            child = None
            if(node[0] in maps):
                node_root = maps[node[0]]
            else:
                node_root = TreeNode(node[0])
                # store ptr of new node in map
                maps[node[0]] = node_root

            if(node[1] in maps):
                child = maps[node[1]]
            else:
                child = TreeNode(node[1])
                # store only if new node in map
                maps[node[1]] = child
            
                # link child 
            if(node[2] == 1):
                node_root.left = child
            else:
                node_root.right = child
                
            if(child.val not in parent):
                parent[child.val] = node_root
            if(root is None):
                root = node_root
            else:
                # this root has appeared as child of a node
                if(root.val in parent):
                    temp = parent[root.val]
                    while(temp.val in parent):
                        temp = parent[temp.val]
                    root = temp
        return root    
            