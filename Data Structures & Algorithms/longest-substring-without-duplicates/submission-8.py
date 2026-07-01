class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #duplicate check - hashSet
        #but we have to remember the duplicate string's index so use hashMap

        hashMap = dict() #key,value = string, index

        #find the longist subarray -> max

        L = 0
        maxLen = 0
        #expand the subarray from the right pointer to find the logest possibly array
        #abcdddfghic 
        #bcaxec
        #if we meet duplicate, move the left pointer to the index of duplicated character
        for R in range(len(s)) : 
            
            if s[R] in hashMap.keys() : 
                print("duplicated :", L, R, hashMap, s[R], hashMap[s[R]] )
                L = max(hashMap[s[R]] + 1,L) #never go left
                #hashMap = dict() #we have to initialize hash map because we find the next window
                hashMap[s[R]] = R #we have to move left pointer to the next of first duplicate index
                #because we have to start again
                #for example - bcaxe...c -> maxLen = 5 then c is duplicated
                #              caxec is also duplicate so just start from a
                #              axecfocgjceg.... we
                print("initialized Hash :", hashMap, L, R, hashMap[s[R]] )
            else : 
                hashMap[s[R]] = R
            
            
            maxLen = max(maxLen, R-L+1)
            # print("R ",R)
            # print("L ",L)
            print(hashMap, maxLen)
        return maxLen