class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # for idx, num in enumerate(nums) : 
        #     print(idx,num)

        L = 0
        R = len(nums) - 1

        while L < R : 
            mid = (L+R)//2
            print("mid ", mid)
            if nums[mid] < target : #if the mid value is less than target value, we have to search right
                L = mid + 1            
            elif nums[mid] > target : #if the mid value is greater than target value
                R = mid - 1
            else : 
                return mid

        if nums[L] == target : 
            return L
        else :
            return -1

