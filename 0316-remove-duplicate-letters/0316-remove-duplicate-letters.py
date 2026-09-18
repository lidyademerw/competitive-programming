class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        seen=set()
        last={letter:i for i,letter in enumerate(s)}
        for i,letter in enumerate(s):
            if letter not in seen:
                while stack and last[stack[-1]]>i and stack[-1]>letter:
                    seen.remove(stack.pop())
                seen.add(letter)
                stack.append(letter)
        return "".join(stack)
        