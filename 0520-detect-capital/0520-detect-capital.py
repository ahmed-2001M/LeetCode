class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True
        if word == word.lower():
            return True
        if word == word.title():
            return True
        return False
        