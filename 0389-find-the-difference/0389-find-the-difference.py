class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
      for i in set(t +  s):
        if s.count(i)!=t.count(i):
            return i        