class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cnt = 0
        thresholdSum = threshold*k 
        curSum = sum(arr[:k-1]) #k-2, k-3,...0
        print(curSum)
        for L in range(len(arr) -k + 1) : #in python this value is non-inclusive
            curSum += arr[L + k - 1]#==R
            if curSum >= thresholdSum : 
                cnt += 1            
            curSum -= arr[L]
        
        return cnt