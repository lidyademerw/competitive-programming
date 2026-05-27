class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper() or word == word.lower():
            return True
        elif word[0].upper()== word[0] and word[1::].lower() == word[1::]:
            return True
        else:
            return False
        