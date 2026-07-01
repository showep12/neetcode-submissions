class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #We have to loop through this list one time
        #We have to iterate through the list once
        #So the time complexity is O(n) (Big O of n)

        #Solution 1 : We have to count each number and record it to HashMap
        #############################################################       
        NumHash = set()

        for num in nums : 
            if (num in NumHash) : 
                return True
            NumHash.add(num) #        
        return False
        #############################################################       










        #Solution 2 - Start    
        #(My) Solution 2 : We can sort the list, and if the same number appears twice, it returns True 
        #(GPT) Solution 2 : Second approcah is to sort the list and check if any adjacent elements are the same
        # Time complexity: O(nlogn)
        # Space complexity: O(n)
        #############################################################       
        # nums_sorted = sorted(nums) #sort the input list
        # cntSameNum = 0
        # currentNum = 0
        # print(range(len(nums_sorted)))
        # for i in range(len(nums_sorted)) :
        #     #print(i)
        #     if (i == 0) : 
        #         currentNum = nums_sorted[i]
        #         cntSameNum = cntSameNum + 1                
        #     else : 
        #         print(i)
        #         if currentNum == nums_sorted[i] : 
        #             print("match")
        #             cntSameNum = cntSameNum + 1
                    
        #             if (cntSameNum > 1) :
        #                 return True
        #         else : #if currentNum != n
        #             print("not match")
        #             currentNum = nums_sorted[i]
        #             cntSameNum = 1

        # return False
        ############################################################
        #Solution 2 - End

