class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        #koko 
        #hours is always greater than length 
        #the worst but possible k is the max value in the piles
        #ex) in Example 2, if k is 24, the condition is not valid since in the position 
        #Because at the index where the value is 25, the operation must be performed twice.

        #the best k is 1 because if we have enough time, we can eat very slowly and it is 1
        #the best

        #We have some candidates that are sorted values.
        #and we have to find the optimal value with out checking every value
        #we can use binary search, find the mid value and check if it is valid, 
        #if it is not valid, we 

        #if mid value is sufficient, we can discard the right values because we already found 
        #mid value that currently is at most possible minimum value

        #if mid value is insufficient, we can discard the left values since they are also insufficient

        maxK = max(piles)
        minK = 1
        pilesSorted = sorted(piles)
        print(pilesSorted)
        L = 1
        R = maxK

        while L < R : 
            mid = (L+R)//2
            time = 0
            print("roop",mid, L, R)
            #check if it is valid
            for num in pilesSorted : 
                time += math.ceil(num/mid)

            
            if time > h : #if it is not valid, move to a higher rate
                print("not valid", time, h)
                L = mid + 1
            else : #mid can be the optimal
                print("valid", time, h)
                R = mid #if it is valid, move to a lower rate
            print("End roop",mid, L, R)
        return L

        #Binary Search
        #1. find min/max - 정답이 한쪽에만 있따
        #2. False / True boundary exist


            


        

        