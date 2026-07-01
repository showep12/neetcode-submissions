class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #maximize width x height 
        #we always start from leftmost and rightmost 
        #   ->because the all the height could be same value...
        #   ->and we just move into the inside of the range... 

        #each step... we have to decide which 
        #we only move to the inside... and move the optimal point...

        left = 0
        right = len(heights) - 1
        max_area = 0

        while left < right : 
            width = right - left# + 1
            height = min(heights[left], heights[right])

            max_area = max(max_area, width*height)

            if heights[left] >= heights[right] : 
                right -= 1
            else : 
                left += 1
        return max_area

