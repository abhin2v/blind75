# Definition for a binary tree node.
from typing import List, Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Problem Statement:
# Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary 
# tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

# Constraints:
# 1 <= preorder.length <= 3000
# inorder.length == preorder.length
# -3000 <= preorder[i], inorder[i] <= 3000
# preorder and inorder consist of unique values.
# Each value of inorder also appears in preorder.
# preorder is guaranteed to be the preorder traversal of the tree.
# inorder is guaranteed to be the inorder traversal of the tree.

# Let me first explain about preorder and inorder.
# Preorder : root, left, right
# Inorder : left, root, right

# From preorder we will get to know that first node of preorder will going to be root of tree.
# Now find that root node in inorder, elements present at left side of that node will going to be lie in left subtree
# and elements present at right side of root node will going to be lie in right subtree.
# Find out number of elements in left subtree from inorder, same number of elements after root node from preorder, we 
# will be preorder traversal for left subtree and after that other elements will going to preorder traversal of right
# subtree.
# This thing we will keep on doing in recursion. Find out root node of each tree/subtree then pass their correspondings
# preorder and inorder traversal to left and right subtree.
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        root = None
        if preorder:
            root = TreeNode(preorder[0])
            in_root_index = 0
            while preorder[0] != inorder[in_root_index]:
                in_root_index += 1
            root.left = self.buildTree(preorder[1:1+in_root_index], inorder[:in_root_index])
            root.right = self.buildTree(preorder[1+in_root_index:], inorder[in_root_index+1:])
        return root