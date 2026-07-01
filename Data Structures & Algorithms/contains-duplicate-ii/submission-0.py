class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #abs(i - j) <= k -> The index difference between i and j is at most k.
        #-> We maintain a window where the index difference is bounded by k.
        #-> if k is 3 then the maximum size of window is 4 because index starts from 0 in the array
         

        #If nums[i] == nums[j], we need to check whether the duplicate occurs within the current window.

        #1. We use hash sets because we have to check the duplicate and index does not matter
        hashSet = set()
        L = 0
        
        #start 
        

        for R in range(L, len(nums)) : #iterate from index L+1 to the end of array
            
            if (R - L) > (k) : #move to the next window if the size of window exceeds k + 1
                #it means R-L + 1 > k + 1 -> it is expressed considering the size of array 
                #we can change this as R - K > k                       
                hashSet.remove(nums[L])
                L += 1 #increment L
            
            if nums[R] in hashSet and R-L > 0 : 
                print(hashSet)
                print(nums[R])
                return True

            hashSet.add(nums[R]) 
        
        return False

