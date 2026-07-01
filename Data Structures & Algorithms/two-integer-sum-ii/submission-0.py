class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        LP = 0
        RP = len(numbers) - 1
        answer = None
        while answer is None or sum(answer) != target: 
            answer = [numbers[LP], numbers[RP]]
            # print(answer)
            # print(sum(answer))
            if (sum(answer) < target) : 
                LP += 1 
            elif (sum(answer) > target) : 
                RP -= 1
        # print(answer)
        return [LP + 1 , RP + 1]
        # A or B <> !A and !B


        #Use two pointer and Binary Search together

        # mid = (LP + RP)//2

        # while RP - LP > 0 and numbers[RP] - numbers[LP] > 0 :
        #      mid = (LP + RP)//2
        #      if ()

        