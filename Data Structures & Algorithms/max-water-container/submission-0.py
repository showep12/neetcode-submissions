class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #if there is a height 
        #There is a assumption that usally the widest container store the largest amount 
        #of water but there is a exceptional case like this one
        #the left most bar's height is one, it means if the     
        #the bar immediately to the right of this bar

        #we have to find move each leftmost and right most bar and update the max amount
        #how can we calcute??? it is simple, 
        #the length between two point times the lower bar's height
        #for example L = 1 / R = 6 -> distance = 7 * 1 = 7
        # L = 2 / R = 6 -> distance = 6 / lower = 6 -> 36
        # L = 2 / R = 

        #there can be some execptional case like this one
        #[5,1,1,1,1000,1,1000,1,1,1,5]

        L = 0
        R = len(heights) - 1
        maxAmount = 0
        while L < R : 
            distance = R - L
            currAmount = min(heights[L], heights[R]) * distance
            print(currAmount, L, R, distance)
            maxAmount = max(maxAmount, currAmount)
            if heights[L] < heights[R] : 
                L+= 1
            elif heights[L] > heights[R] : 
                R-= 1
            else : #
                L+=1
        
        return maxAmount