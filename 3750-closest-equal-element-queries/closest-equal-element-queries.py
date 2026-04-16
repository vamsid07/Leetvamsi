class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # [ 1,2,3,4,2,3,3,1,2 ]
        d = {}
        n = len(nums)
        first = {}
        last = {}
        for i in range(n) : 
            if nums[i] in first : 
                last[nums[i]] = i
                continue 
            else : 
                first[nums[i]] = i
            last[nums[i]] = i
        min_d = [float('inf')]*(n+1)
        for i in range(len(nums)) : 
            if nums[i] in d : 
                c1 = i - d[nums[i]]
                c2 = n - i + d[nums[i]]
                c3 = n - i + first[nums[i]]
                c4 = n - last[nums[i]] + d[nums[i]] 
                print(i,c1,c2,c3,c4,last[nums[i]],d[nums[i]])
                min_d[i] = min(c1,c2,c3)
                min_d[d[nums[i]]] = min(min_d[d[nums[i]]],c1,c2,c4)
            d[nums[i]] = i 
        ans = []
        for i in range(len(queries)) : 
            if min_d[queries[i]] == float('inf') : 
                ans.append(-1)
            else : 
                ans.append(min_d[queries[i]])
        return ans