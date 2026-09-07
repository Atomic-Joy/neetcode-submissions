class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = [root]
        front = 0

        while front < len(queue):
            level = []
            level_size = len(queue) - front
            for _ in range(level_size):
                node = queue[front]
                front += 1
                level.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result