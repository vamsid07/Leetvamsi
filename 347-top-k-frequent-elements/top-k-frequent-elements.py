class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]] += 1 
            else:
                d[nums[i]] = 1 
        arr = []
        keys = list(d.keys())
        for i in range(len(keys)):
            num = keys[i]
            cnt = d[num]
            arr.append([cnt, num]) 
        arr.sort(reverse=True)
        ans = []
        for i in range(k) : 
            ans.append(arr[i][1])
        return ans