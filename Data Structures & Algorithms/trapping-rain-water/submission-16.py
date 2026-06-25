class Solution:
    def trap(self, height: List[int]) -> int:

        res = 0
        for i in range(1,len(height)):
            left = height[i]

            for j in range(i):
                left = max(height[j],left)
            
            right = height[i]
            for k in range(i + 1,len(height)):
                right = max(height[k],right)
            
            h = min(left,right)

            trapped = h - height[i]
            res += trapped
        return res
        