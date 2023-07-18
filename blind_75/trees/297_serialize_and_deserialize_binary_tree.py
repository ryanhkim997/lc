from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        queue = deque([root])
        serialized_output = []
        while queue:
            curr = queue.popleft()
            if curr:
                serialized_output.append(str(curr.val))
                queue.append(curr.left)
                queue.append(curr.right)
            else:
                serialized_output.append("&")

        return ",".join(serialized_output)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        bt = data.split(",")

        root = TreeNode(bt[0])
        queue = deque([root])
        i = 1
        while queue and i < len(bt):
            curr = queue.popleft()
            left = bt[i]

            if left == "&":
                curr.left = None
            else:
                curr.left = TreeNode(int(left))
                queue.append(curr.left)
            i += 1

            right = bt[i]
            
            if right == "&":
                curr.right = None
            else:
                curr.right = TreeNode(int(right))
                queue.append(curr.right)
            i += 1

        return root


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))