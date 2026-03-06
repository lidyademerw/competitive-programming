class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        right=len(height)-1
        maxArea=0
        while i<right:
            w=right-i
            length=min(height[i],height[right])
            area=w*length
            maxArea=max(maxArea,area)
            if height[i]<height[right]:
                i+=1
            else:
                right-=1
        return maxArea


        