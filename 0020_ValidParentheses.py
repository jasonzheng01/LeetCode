class Solution(object):
    def isValid(self, s):
        stack = []
        d = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in d.values():
                stack.append(c)
            else:
                if len(stack) == 0 or d[c] != stack.pop():
                    return False
        if len(stack) != 0:
            return False
        return True
