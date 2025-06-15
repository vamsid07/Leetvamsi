class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        d1 = defaultdict(list) 
        d2 = defaultdict(int)   
        q = deque()
        d2[root.val] = 0 
        q.append((root, 0))
        d1[0].append((0, root.val))
        while q:
            node, row = q.popleft()
            col = d2[node.val]
            if node.left:
                d2[node.left.val] = col - 1
                d1[col-1].append((row + 1, node.left.val))
                q.append((node.left, row + 1))
            if node.right:
                d2[node.right.val] = col + 1
                d1[col + 1].append((row + 1, node.right.val))
                q.append((node.right, row + 1))
        ans = []
        keys = list(d1.keys())
        keys.sort()
        for key in keys:
            level = d1[key]
            level.sort()
            temp = []
            for i in level:
                temp.append(i[1])
            ans.append(temp)
        return ans