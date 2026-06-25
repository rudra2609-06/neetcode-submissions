class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1
        
        for i in range(len(heights)):
            h1 = heights[i]
            for j in range(i + 1,len(heights)):
                width = j - i
                height = min(h1,heights[j])
                volume = width * height
                if res < volume:
                    res = volume
        return res


        