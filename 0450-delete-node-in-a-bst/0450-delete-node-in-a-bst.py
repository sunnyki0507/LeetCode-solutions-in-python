# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        self.result = None
        if not root:
            return None
        self.tmp = None
        self.found = 0
        self.prev = None


        if not root.right and not root.left:
            if root.val == key:
                return None
            else:
                return root

        def find(node, value, PreNode):
            if node.val == value:
                self.prev = PreNode
                self.tmp = node
                self.found = 1
                return
            elif self.found == 0:
                if node.left:
                    find(node.left, value, node)
                if node.right:
                    find(node.right, value, node)

        find(root, key, None)

        if not self.tmp:
            return root
        

        # def dfs(node):
        #     arr = deque()
        #     arr.append(root)
        #     arrVal = []
        #     while arr:
        #         nodes = arr.popleft()
        #         arrVal.append(nodes.val)
        #         if nodes.left:
        #             arr.append(nodes.left)
        #         if nodes.right:
        #             arr.append(nodes.right)
        #     print(arrVal)
        
        if not self.tmp.left and not self.tmp.right:
            if self.prev.right and self.prev.right.val == self.tmp.val:
                self.prev.right = None
            else:
                self.prev.left = None
            return root

        leftNode = self.tmp.left
        rightNode = self.tmp.right
        self.preVal = self.tmp
        self.change = None

        def replaceLeft(node, preNode):
            self.preVal = preNode
            self.change = node
            if node.right:
                replaceLeft(node.right, node)
            return
        
        def replaceRight(node, preNode):
            self.preVal = preNode
            self.change = node
            if node.left:
                replaceRight(node.left, node)
            return

        if leftNode:
            replaceLeft(leftNode, self.preVal)
        elif rightNode:
            replaceRight(rightNode, self.preVal)

        if self.preVal:
            if self.preVal.left and self.preVal.left.val == self.change.val:
                if self.change.left:
                    self.preVal.left = self.change.left
                elif self.change.right:
                    self.preVal.left = self.change.right
                else:
                    self.preVal.left = None
            else:
                if self.change.left:
                    self.preVal.right = self.change.left
                elif self.change.right:
                    self.preVal.right = self.change.right
                else:
                    self.preVal.right = None

        self.change.left = self.tmp.left
        self.change.right = self.tmp.right

        if self.prev:
            if self.prev.right and self.prev.right.val == self.tmp.val:
                self.prev.right = self.change
            else:
                self.prev.left = self.change
        else:
            root = self.change
        
        return root

        """
        :type root: Optional[TreeNode]
        :type key: int
        :rtype: Optional[TreeNode]
        """
        