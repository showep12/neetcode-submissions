class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        if len(nums) == 0  : 
            return False

        #this problem asks whether a duplicate element exists.”
        #we will use the HashSet if the new number already exits, then returns true

        hashSet = set()
        for num in nums : 
            if num in hashSet :                 
                return True
            else  : 
                print(num)
                if num not in hashSet :                 
                    hashSet.add(num)

        return False