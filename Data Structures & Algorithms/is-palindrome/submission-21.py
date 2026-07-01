class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        print(s)
        alnumList = [ch for ch in s.lower() if ch.isalnum()]
        print(alnumList)
        LP = 0
        RP = len(alnumList) - 1

        while (LP < RP) : 
            if (alnumList[LP] != alnumList[RP]) : 
                return False
            LP = LP + 1
            RP = RP - 1
            if (LP == RP) : 
                break

        return True

        