import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we can use the hashmap to manage
        
        #we can use heap 
        #remain the numbers in the heap with size k
        #Maxheap

        num_counts = {}
        for num in nums : 
            num_counts[num] = num_counts.get(num,0) + 1

        #bucket : index is the frequency....
        maxFreq = len(nums)
        #index = freq / value = list of number (because two or more numbers can have the same frequency)
        bucket = [[] for _ in range(maxFreq + 1)]
        
        


        for num, freq in num_counts.items() : 
            bucket[freq].append(num)

        #6

        result = []
        for idx in range(maxFreq,0,-1) : 
            #each element is list
            for num in bucket[idx] : 
                result.append(num)
                if len(result) == k :
                    return result             
        

    



        #Bucket Sort 
        #How can I determine a safe bucket size?
        #->I check the maximum possible bucket index and compare it with memory limits.
        #store the frequency data in hashMap...

        #
