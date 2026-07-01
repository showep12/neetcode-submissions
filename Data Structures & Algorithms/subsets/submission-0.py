class Solution:    

    def makeSubset(self, idx, nums, currSubsets, resultSubsets) : 
            if idx >= len(nums) : 
                resultSubsets.append(currSubsets.copy())
                return
            
            currSubsets.append(nums[idx])
            self.makeSubset(idx+1, nums, currSubsets, resultSubsets)

            currSubsets.pop()
            self.makeSubset(idx+1, nums, currSubsets, resultSubsets)
    
                   
        
        
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #A subset problem is typically modeled by iterating through the elements and making a binary choice at each step: include or exclude.”
        # For subset problems, you loop through the list and decide whether to include the current element in the subset or not.
        
        resultSubsets = []
        currSubsets = []     

        idx = 0
        self.makeSubset(idx, nums, currSubsets, resultSubsets)
        print(resultSubsets)
        return resultSubsets

        