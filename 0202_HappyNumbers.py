class Solution(object):
    def isHappy(self, n):
        used = [n]
        while n != 1:
            strnum = str(n)
            total = 0
            for num in strnum:
                total += int(num)**2
            if total in used:
                return False
            used.append(total)
            n = total
        return True
