class Solution:
    def findMin(self, nums: List[int]) -> int:
        #We can divide list into two groups, small / large
        #[5,6,1,2,3,4] -> we can see [5,6] is large number group
        #[1,2,3,4] is small number group
        #if the mid value is greater than right most value 
        #-> mid value is in the large number group and it means we can discard left group
        #   including mid value because we clearly know that the value is not the smallest value

        #if the mid value is less than right most value
        #-> mid value is in the small number group and there is a possibility that the mid value
        #is the smallest value so we can discard left group but this time we should not discard mid value
        #because it is also the candidate of the smallest value

        #[5,6,1,2,3,4]
        #mid value = 1 and 1 is less than 4 which means 1 is in the small number group
        #and we can discard right group, 2,3,4 because current mid value is in the small group and
        #right of this value is must be always greater than mid value 
        # [5,6,1]  #mid value is 6 then 6 is greater than 1 
        #it means 6 is in the large number group and we can discard left group including mid value
        #we have only [1] and it is the minimum value

        L = 0
        R = len(nums) - 1

        while L < R :
            mid = (L+R)//2 

            if nums[mid] < nums[R] : #mid value is less than right most value -> we can
            #we can judge that mid value is in the small values group and we can discard
            #right group except mid value, it means we move the right pointer to mid
                R = mid
            else : #nums[mid] > nums[R] == mid value is greater than right most value
            #we can judge that mid value is in the large group and we can discard left group
            #including mid value, it means we move the left pointer to mid plus one
                L = mid+1
        
        return nums[L]
                


        
        # 
        

