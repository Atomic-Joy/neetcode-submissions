class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = [root]
        front = 0

        while front < len(queue):
            level_size = len(queue) - front
            for i in range(level_size):
                node = queue[front]
                front += 1
                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result