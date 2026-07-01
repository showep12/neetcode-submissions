#English
#“We want the largest window where all characters can be made the same by replacing 
# at most k characters, which is equivalent to window_len - max_freq <= k.”

#“We look for the largest window where the number of non-majority characters is at most k.”

#the most frequent character

#틀림 - now we are in the sufficient condition to expand the window
# “Now the window is valid, so we can expand it.”
# “Now we satisfy the condition, so we can expand the window.”
# “As long as the condition holds, we keep expanding the window.”
# “At this point, the window is within the constraint, so we continue expanding.”    

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #update the most frequent character each time,
        #if we reach the limit, move pointer 

        #if the most frequent character is equal?? - XXYYZZ
        #YYZX XXXDXY  k =2

        #XXXXX YYYYYY ZZZ k =2
        #L=0 R=6 -> max
        #L=0 R=7 -> move left pointer but it is still insufficient 
        #... L=3 R=7 -> Y  is the most frequent character XX YYY
        #... now the window is valid so we can expand the Window
        #... L=3 R = 11 -> max became larger than we consider X as the most frequent String
        #Because the process continues using a different 
        #variable Y, the maximum length becomes longer than when X is the dominant variable.

        #1. expand window from right until the it is valid
        #2. shrink window from left if the window is not valid
        #3. update the longest legnth of the window

        # maxFreq = s[0]
        # L = 0
        # R = 0
        # maxLen = 0
        # hashSet = dict()
        # for R in range(len(s)) : 
            
        #     if s[R] in hashSet.keys() : 
        #         hashSet[s[R]] += 1
        #     else : 
        #         hashSet[s[R]] = 1

        #     #switch maxFreq
        #     print("iter : ", R)
        #     print(hashSet, s[R], maxFreq)
        #     if maxFreq != s[R] and hashSet[maxFreq] < hashSet[s[R]] : 
        #         print("max change")
        #         maxFreq = s[R]

        #     #xyzyky k = 2
        #     while (R-L+1 - hashSet[maxFreq] > k) : 
        #         print("invalid-move", L,R, hashSet, R-L+1 - hashSet[maxFreq], maxFreq)
        #         hashSet[s[L]] -= 1
                
        #         print(hashSet)
        #         if maxFreq == s[L] and hashSet[maxFreq] < hashSet[s[R]]: 
        #             print("max change in left move")
        #             maxFreq = s[R]

        #         L+=1

        #     maxLen = max(maxLen, R-L + 1)
        
        # return maxLen
        hashMap = dict()
        maxLen = 0

        L = 0
        maxF = 0

        hashMap = {"a" : 1}
        print(hashMap.get("b",0))

        for R in range(len(s)) : 
            hashMap[s[R]] = 1 + hashMap.get(s[R],0) #add to hash map
            maxF = max(hashMap.values())
            
            while R-L-maxF + 1 > k : 
                hashMap[s[L]] -= 1
                #maxF = max(hashMap.values())
                L+=1
            
            maxLen = max(maxLen, R-L+1)

        return maxLen