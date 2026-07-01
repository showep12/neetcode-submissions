class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #[1,2,3,4] target = 5

        #if we use hash map... it requires O(n) space complexity
        left = 0
        right = len(numbers) - 1
        #we can move in only one direction
        #it is non-decreasing order... so 
        #if curr
        while left < right : 
            if numbers[left] + numbers[right] == target : 
                return [left+1, right+1]
            elif numbers[left] + numbers[right] < target : 
                #we have to increase the sum so move left pointer to the right
                left += 1
            else : 
                right -= 1
