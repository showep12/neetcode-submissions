class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        #sorted array
        #target value
        #distinct integer

        #Implement binary search
        #
        startPoint = 0 #the target value could be exist on the nums at index 0
        endPoint = len(nums) - 1 #off-by-one error  the length of nums minus one

        #mid
        
        #we have to continue calculating the midValue
        #if the midValue is over than target, 
        #it means we can narrow down the range by moving the EndPoint to midPoint - 1
        #if the midValue is less than target, 
        #it means we can narrow down the range by changing the startPoint to midPoint + 1
        #because we have to find bigger value than midValue  
        #the end of loop is when the StartPoint is greater than or equl to EndPoint

        while startPoint < endPoint :
            midPoint = (startPoint + endPoint) //2 
            if (nums[midPoint]==target) : 
                return midPoint
            elif (nums[midPoint] > target) : #if target value is less than value of midPoint
                endPoint = midPoint - 1
            elif (nums[midPoint] < target) :
                startPoint = midPoint + 1

        if (nums[startPoint] == target) : 
            return startPoint
        else : 
            return -1            


        
        