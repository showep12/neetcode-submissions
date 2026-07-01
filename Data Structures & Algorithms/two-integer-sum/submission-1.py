class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]: 


        #1: Use HashMap - O(n)

        ## Sort (log(n)) and then to findout every element, n + n-1 + n-2 .... 1 = n+1*2
        #Space Complexity        
        #Time Complexity
        ## Sort (log(n)) and then to findout every element, n + n-1 + n-2 .... 1 = n+1*2
        #Space Complexity



        #Sol3 : Usual HashSet
        #We have to remember indices of every element
        #



        #Here, I create an empty dictionary called enum(이눔)
        enum = {} 

        #1: Then, I use the [enumerate] function to loop through the list nums
        #2-1 : The [Enumerate] function allows us to loop through a sequence while keeping track of both the index and the value of the dictionray
        #2-2 : With enumerate(), we can loop through a list and get both the index and the element at the same time.
        #3-1 : And in the loop, I assign each number in nums as a key and its index as the value in the dictionary enum.
        #3-2 : And in the loop, I map each number as a key to its index as the value.”
        for idx,num in enumerate(nums): 
            enum[num] = idx #Here I assign the index to the key num in the dictionary enum
        
        
        for i in range(len(nums)) : #Iterate through the indices of original list nums
            #Basic : Here I calculate the difference between the target and the current number.
            #Proff : We compute the diff by subtracting the current element from the target.          
            diff = target - nums[i] 

            #Basic : Here I calculate the difference between the target and the current number.
            #Proff : We compute the diff by subtracting the current element from the target.          
            if (diff in enum and enum[diff] != i) : #[in] checks keys only in Python Dictionary
                return [i, enum[diff]] #return a list containing i and the value of diff in enum

                
        # return nums
        
        # for i, n in nums : 
        #     print(i,n)
        # numsHash = set(nums) #O(n)
        
        # for num in nums : 
        #     target_diff = target - num #calculate difference


        #New Learning
        ######################################
        ###
        # enumerate(iterable, start=0) : let us loop through a sequence (like a list or tuple) 
        # while keeping track of both the index and the value.
        ###
        ######################################
        #New Learning
            
