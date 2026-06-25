class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = -1
        i = 0
        j = len(heights) - 1

        while i < j:
            width = j - i
            volume = width * min(heights[i],heights[j])
            if volume > res:
                res = volume
                

            if heights[j] < heights[i]:
                j -= 1
            else:
                i += 1
        
        return res


        