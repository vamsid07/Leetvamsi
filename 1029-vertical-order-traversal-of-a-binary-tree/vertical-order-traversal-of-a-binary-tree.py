class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d1 = defaultdict(list)  # col: list of (row, val)
        d2 = defaultdict(int)   # val: col
        q = deque()
        d2[root.val] = 0 
        q.append((root, 0))  # (node, row)
        d1[0].append((0, root.val))  # col = 0, row = 0

        while q:
            node, row = q.popleft()
            col = d2[node.val]
            if node.left:
                d2[node.left.val] = col - 1
                d1[col - 1].append((row + 1, node.left.val))
                q.append((node.left, row + 1))
            if node.right:
                d2[node.right.val] = col + 1
                d1[col + 1].append((row + 1, node.right.val))
                q.append((node.right, row + 1))

        ans = []
        for key in sorted(d1.keys()):
            level = sorted(d1[key], key=lambda x: (x[0], x[1]))
            ans.append([val for row, val in level])
        return ans
