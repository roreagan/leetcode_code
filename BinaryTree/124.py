#! /home/work/tools/python27/bin python
#  -*- coding: utf-8 -*-
#  @Time    : 2021-05-16 18:57
#  @Author  : luolvgen@baidu.com
#  @Site    :
#  @File    : 124.py.py
#  @Software: PyCharm

"""
路径 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。
路径和 是路径中各节点值的总和。
给你一个二叉树的根节点 root ，返回其 最大路径和

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

解析：
该问题是一道二叉树遍历的套路问题，其根本方法在于二叉树的DFS方法，DFS引入递归即可

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def helper(self, root):
        if root == None:
            return 0
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        tmp_res = root.val
        if left_sum > 0:
            tmp_res += left_sum
        if right_sum > 0:
            tmp_res += right_sum
        self.res = max(self.res, tmp_res)
        return max(left_sum, right_sum, 0) + root.val

    def maxPathSum(self, root: TreeNode) -> int:
        if root == None:
            return 0
        self.res = root.val
        self.helper(root)
        return self.res


nodes = [TreeNode(i) for i in [9, -10, 20, 15, 7]]
nodes[1].left = nodes[0]
nodes[1].right = nodes[2]
nodes[2].left = nodes[3]
nodes[2].right = nodes[4]

s = Solution()
print(s.maxPathSum(nodes[1]))