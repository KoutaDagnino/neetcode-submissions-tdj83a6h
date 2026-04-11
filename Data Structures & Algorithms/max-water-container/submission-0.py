class Solution:
    def maxArea(self, heights: List[int]) -> int:
        hset = sorted(set(heights))
        left = 0
        right = len(heights)-1
        maxarea = 0
        for h in hset:
            while left < right and heights[right] < h:
                right -= 1
            while left < right and heights[left] < h:
                left += 1
            if h * (right - left) > maxarea:
                maxarea = h * (right - left)
            print(maxarea)
        return maxarea
                


