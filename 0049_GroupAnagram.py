class Solution(object):
    def groupAnagrams(self, strs):
        d = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                count[ord(c) - ord("a")] += 1
            val = d.get(tuple(count), 0)
            if val == 0:
                d[tuple(count)] = [word]
            else:
                d[tuple(count)].append(word)
        
        return d.values()
