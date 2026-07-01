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
        while L < R : #we have to compare every possible values
            distance = R - L #distance of the container

            #the amount can be calculated by distance times minimum height between Left bar
            #and right bar beacuse the water will be spilled at the lower bar's boundary
            
            currAmount = min(heights[L], heights[R]) * distance
            print(currAmount, L, R, distance)
            
            #we have to update maximum amount by moving two pointer  
            maxAmount = max(maxAmount, currAmount)

            #the point is how can we move the pointer??? 
            #if we do this by brute force, we have to fix for example fix left pointer
            #and check the other every pointers as right pointer and update max value
            #and then increment the left pointer's index and again check the every possible 
            #right pointer
            #this is takes like this n-1 + n-2 + n-3 + n-4. ...1 
            #n-1/2 * n  O(n^2)


            #how can we move pointers
            #should we move left one? or right one?
            #if we move right one, the amount of water drops largely because 
            #the height of the right bar after shifting left is too short
            #then how about if we move left pointer?? 
            #the amount off water increased compared with previous one
            
            #the way of getting the most amount of water is maximizing the lower bar's height
            #and also maximizing the distance

            #if we have to choose left or right
            #we always move lower bar's pointer because 
            #it is obvious that in the same distance, maximizing the lower bar's height is important
            #it means discard the lower one and move to next
            
            #we are already decreasing the distance,
            #at this moment, we are cleary know discarding higher bar
            #can never be the larger one, even if there is a much higher bar next to the bar
            #because the max height of water in the container is always determined by lower bar
            #so if we have to move the bar, we have to move lower bar assuming the possibility
            #at least there could be a higher bar

            if heights[L] < heights[R] : 
                L+= 1
            elif heights[L] > heights[R] : 
                R-= 1
            else : #
                L+=1
        
        return maxAmount