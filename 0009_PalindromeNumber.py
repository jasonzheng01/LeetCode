class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        else:
            x = str(x)
            p1 = 0
            p2 = len(x) - 1
            while p1 < p2:
                if x[p1] != x[p2]:
                    return False
                p1 += 1
                p2 -= 1
            return True
