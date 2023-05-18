class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        lst = [[] for i in range(len(nums) + 1)]

        for num in nums:
            d[num] = 1 + d.get(num, 0)
        for n, c in d.items():
            lst[c].append(n)
        
        ret = []
        for i in range(len(lst) - 1, 0, -1):
            for j in lst[i]:
                ret.append(j)
                if len(ret) == k:
                    return ret
