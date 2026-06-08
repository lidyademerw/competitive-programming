class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        letters = list(s)
        n=len(letters)
        left = 0
        right = n - 1
        while left < right:
            if letters[left] not in vowels:
                left += 1
            elif letters[right] not in vowels:
                right-=1
            else:
                letters[left], letters[right] = letters[right], letters[left]
                left += 1
                right-=1
        return "".join(letters)


        