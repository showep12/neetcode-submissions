class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
         
        
        nums.sort()
        print(nums)
        answer = []

        for idx in range(len(nums) - 2) : 
            if (idx>0 and (nums[idx]==nums[idx-1])) : 
                continue
            LP = idx + 1
            RP = len(nums) - 1    
            while LP < RP : 
                threeSum = nums[idx] + nums[LP] + nums[RP]
                if (threeSum > 0) : 
                    #move RP to Left to decrease the threeSum
                    RP -= 1
                elif (threeSum < 0) : 
                    #move LP to Right to increase the threeSum
                    LP += 1
                else : 
                    answer.append([nums[idx], nums[LP], nums[RP]])
                    LP += 1
                    RP -= 1
                    while nums[LP] == nums[LP -1] and LP < RP : 
                        LP += 1

        print(answer)
        return answer        

        #two pointer = O(n)
        #loop = O(n)

        # LP = 0
        # MP = LP + 1
        # RP = len(nums) - 1
        # answer = []
        # print(nums[LP] + nums[MP] + nums[RP])
        # while MP < RP : 
        #     if ((nums[LP] + nums[MP] + nums[RP]) == 0) :#“nums at L-P” ⭐ (가장 흔함 
        #         answer.append([nums[LP], nums[MP], nums[RP]])
            
        #     if ((RP - 1) == MP) : 
        #         MP = LP + 1
        #         RP -= 1
        #         print("Reset MP")
        #         print("LP :" + str(LP))
        #         print("MP :" + str(MP))
        #         print("RP :" + str(RP))
        #     else : 
        #         MP += 1
        #         print("Increment MP")
        #         print("LP :" + str(LP))
        #         print("MP :" + str(MP))
        #         print("RP :" + str(RP))

        # LP = 0
        # RP = len(nums) - 1        
        # MP = RP - 1
        
        # while LP < MP : 
        #     if ((nums[LP] + nums[MP] + nums[RP]) == 0) :#“nums at L-P” ⭐ (가장 흔함 
        #         answer.append([nums[LP], nums[MP], nums[RP]])
            
        #     if ((LP + 1) == MP) : 
        #         MP = RP - 1
        #         LP += 1
        #         print("Reset MP")
        #         print("LP :" + str(LP))
        #         print("MP :" + str(MP))
        #         print("RP :" + str(RP))
        #     else : 
        #         MP -= 1
        #         print("Increment MP")
        #         print("LP :" + str(LP))
        #         print("MP :" + str(MP))
        #         print("RP :" + str(RP))
                
        # print(answer)
        # seen = set()
        # result = []
        # for lst in answer : 
        #     key = tuple(sorted(lst)) 
        #     if key not in seen : 
        #         seen.add(key)
        #         result.append(lst)
        # print(result)
        # return result

#         lists = [[2, 1], [1, 2], [1, 2, 3], [3, 2, 1]]

# seen = set()
# result = []

# for lst in lists:
#     key = tuple(sorted(lst))     # order-insensitive signature
#     if key not in seen:
#         seen.add(key)
#         result.append(lst)
