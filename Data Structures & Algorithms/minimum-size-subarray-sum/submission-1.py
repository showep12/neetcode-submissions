class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        #sliding window O(n)
        L = 0
        R = 0

        #increment Right pointer until we find the value which is grater than or equal to target
        #if we find it, we try to shrink our window from the left
        curSum = 0
        minLen = len(nums) + 1
        for R in range(len(nums)) : 
            curSum += nums[R]
            # print("iterate : ", R)
            
            while curSum >= target and R >= L :                  
                #  print("before shrink : ", nums[L:R+1])
                 minLen = min(minLen, R-L+1)
                 curSum -= nums[L]
                 L += 1
                #  praint("after shrink : ", nums[L:R+1])                   
        
        if minLen == len(nums) + 1 :
            return 0
        else :
            return minLen
        


        
        



