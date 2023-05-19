class Solution(object):
    def isPalindrome(self, s):
        p1 = 0
        p2 = len(s) - 1
        w = s.lower()
        while p1 < p2:
            if not w[p1].isalnum():
                p1 += 1
            if not w[p2].isalnum():
                p2 -= 1
            if w[p1].isalnum() and w[p2].isalnum():
                if w[p1] == w[p2]:
                    p1 += 1
                    p2 -= 1
                else:
                    return False
        return True
