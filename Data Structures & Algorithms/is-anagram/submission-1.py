import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #1 we can use hashMap to count 
        #2 First make HashMap for each string
        #3 loop one string to check if the 


        dictS = {}
        dictT = {}


        alphabet_list = list(string.ascii_lowercase)
        for ch in alphabet_list : 
            dictS[ch] = 0
            dictT[ch] = 0
            
        for ch in s : 
            dictS[ch] += 1
            
        for ch in t : 
            dictT[ch] += 1 

        for alphabet in alphabet_list : 
            if (dictT[alphabet] != dictS[alphabet]) :
                print(alphabet)
                return False
        return True

        # print(dictS)

        # for key in dictS :
        #     if key not in dictT :
        #         return False
        #     else :
        #         if dictS[key] != dictT[key] :
        #             return False
