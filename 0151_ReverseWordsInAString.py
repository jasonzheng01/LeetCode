class Solution(object):
    def reverseWords(self, s):
        """
        !!! One Liner - didn't do bc I think reversing string with splicing is cheap !!!
        *** Can't be done in 1 line in other languages
        words = s.split()
        words = words[::-1]
        return ' '.join(words)
        """
        words = s.split()
        if len(words) == 1:
            return words[0]
        i = 0
        j = len(words) - 1
        while i < j:
            words[i], words[j] = words[j], words[i]
            i += 1
            j -= 1
        return " ".join(words)
