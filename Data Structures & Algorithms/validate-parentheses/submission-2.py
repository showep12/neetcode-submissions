class Solution:
    def isValid(self, s: str) -> bool:
        #Use stack
        #always 2n because it is always closed
        #cut the array to half                
        dic = {'(': ')', '[' : ']', '{':'}'}
        print(dic)

        stack = []
        if (len(s)%2 > 0) : 
            return False
        else :
            #Put open bracket into the stack
            #If we meet a close bracket, extract the stack item and check if it corresponds with the same type
            for item in s : 
                #Put open bracket into the stack
                if (item in dic.keys()) :
                    stack.append(item)
                else : 
                    if (len(stack) ==0) : 
                        return False
                    else : 
                        stackItem = stack.pop()
                        if (dic[stackItem] != item) :                            
                            return False            
            
            #if there is no open brackets, it is true
            if (len(stack) == 0) :
                return True
            else : 
                return False

            # idx_mid = len(s)//2
            # left = list(s[:idx_mid])
            # right = list(s[idx_mid:])
            # right.reverse()
                        

#             for idx in range(0, idx_mid) :                
#                 left_item = left[idx]
#                 right_item = right[idx]
#                 print(left_item)
#                 print(dic[left_item])
#                 print(right_item)
#                 if (dic[left_item] != right_item) :
#                     return False


# s="()[]{}"

# {}
#             #extract an item from a stack list 
#             #it means 
#         return True
