class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        #return the number of sub-arrays of size k and average greater than or equal to threshold.
        #fixed k size of window 
        #check the average

        #we just update the avg and move the window
        L = 0
        #R = L + k - 1
        #k is the size of window R - L == k-1
        avg = 0
        cnt = 0
        nums = []
        for R in range(len(arr)) : 
            # if R - L < k-1 : 
            #     R += 1
            #     continue

            
            
            if R - L > k-1 : 
                print("move - ", L, R)
                print(arr[L])
                nums.remove(arr[L])
                L += 1
                
            nums.append(arr[R])
            print("end-",nums)
            print("curr - ", R,k)
            print("avg - ", sum(nums)/k)
            if len(nums) == k and sum(nums)/k >= threshold : 
                print("find")
                cnt += 1
            
        return cnt


