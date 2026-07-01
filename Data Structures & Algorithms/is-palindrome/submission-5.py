class Solution:
    def isPalindrome(self, s: str) -> bool:
        #LeftPoint = LP
        #RightPoint = RP

        #Devide the list into two list
        #onlyStr = ["".join(ch for ch in s if ch.isalnum())]
        
        alnumList = [ch for ch in s.lower() if ch.isalnum()]
        print(alnumList)
        LP = 0 #First Index
        RP = len(alnumList) -1 # Last Index
        
        while (LP < RP) : 
            if (alnumList[LP] != alnumList[RP]) : 
                return False
            else : 
                LP += 1
                RP -= 1
        return True
        #print(list(onlyStr))
        # listStr = list(s)
        # #print(listStr)
        # return False