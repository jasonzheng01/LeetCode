class Solution(object):
    def plusOne(self, digits):
        digits[-1] += 1
        if digits[-1] != 10:
            return digits
        else:
            for i in range(len(digits) - 1, 0, -1):
                if digits[i] == 10:
                    digits[i] = 0
                    digits[i - 1] += 1
                else:
                    break
        if digits[0] == 10:
            digits[0] = 0
            return [1] + digits
        else:
            return digits
