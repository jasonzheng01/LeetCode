class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for letter in ransomNote:
            if letter not in magazine:
                return False
            else:
                index = magazine.find(letter)
                magazine = magazine[0:index] + magazine[index + 1:]
        return True
