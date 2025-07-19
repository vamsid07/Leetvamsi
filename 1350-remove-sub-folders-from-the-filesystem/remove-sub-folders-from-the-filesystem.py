class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        vis = set()
        ans = []
        folder.sort()
        for i in folder : 
            temp = ""
            flag = 1
            for j in i : 
                if j == '/' and temp in vis : 
                    flag = 0
                    break 
                temp += j
            if flag == 1 : 
                ans.append(temp)
                vis.add(temp)
        return ans