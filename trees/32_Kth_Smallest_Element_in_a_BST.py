from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem Statement
# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the 
# values of the nodes in the tree.

# Constraints:
# The number of nodes in the tree is n.
# 1 <= k <= n <= 10^4
# 0 <= Node.val <= 10^4

# Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the 
# kth smallest frequently, how would you optimize?

# Brute Force Approach
# We need to return Kth smallest element in given BST, which means if we will arrange all nodes of BST in sorted 
# ascending order then we need to return Kth element.
# In BST, if we perform inorder traversal then we will get elements in sorted order. That's the property of BST.
# And from that result we can return kth index as an answer.
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode], traversal) -> List[int]:
        if root:
            self.inorderTraversal(root.left)
            traversal.append(root.val)
            self.inorderTraversal(root.right)
        return traversal

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = self.inorderTraversal(root)
        return order[k-1]
# Time Complexity = O(N) + O(N) : to traverse the tree + to find kth smallest element = O(N)
# Space Complexity = O(N)+O(N) : for recursive stack + for array = O(N)

# Can we use inorder traversal in such a way that, we need not to store each element's value and also when we 
# found Kth smallest element then no need to move further?
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0

        def inorder(root):
            nonlocal count, k
            if root:
                left = inorder(root.left)
                if left:
                    return left
                count += 1
                if count == k:
                    return root.val
                right = inorder(root.right)
                if right:
                    return right
            return 0
        
        return inorder(root)
                    

# Morris Traversal
# Can we optimize space complexity? Can we solve it in constant space complexity?
# Yes, we can do that using morris traversal.
# What does morris traversal say?
# Morris traversal is a tree traversal algorithm that allows you to traverse a binary tree without using extra 
# space for a stack or recursion. It's a clever technique that uses the tree structure itself to keep track of 
# where you are.
# Morris Traversal Reference : https://medium.com/@mssandeepkamath/morris-tree-traversal-the-o-n-time-and-o-1-space-algorithm-5d2d2d47814a
# It's like, suppose if we are pointing to a node and if it has left subtree then we will find predecessor of current
# node. And we will make current as right child of it's predecessor's right node. We will kept on doing this till
# when we are getting left subtree.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        current = root
        while k:
            # if left child exists
            if current.left:
                # finding right most node
                right_most_node = current.left
                while right_most_node.right:
                    right_most_node = right_most_node.right
                
                # make current points to right of right most node
                right_most_node.right = current
                # mark current's left as null
                temp = current
                current = current.left

                temp.left = None
            else:
                k -= 1
                if k == 0:
                    break
                current = current.right
        return current.val
# Time Complexity = O(N)
# Space Complexity = O(1)