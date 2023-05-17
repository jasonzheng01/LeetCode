class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        string = list(s)
        i, j = 0, len(s) - 1
        while i < j:
            if string[i] in vowels and string[j] in vowels:
                string[i], string[j] = string[j], string[i]
                i += 1
                j -= 1
            elif string[i] in vowels:
                j -= 1
            elif string[j] in vowels:
                i += 1
            else:
                i += 1
                j -= 1
        return "".join(string)
