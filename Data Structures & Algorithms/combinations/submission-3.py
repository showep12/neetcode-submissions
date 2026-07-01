class Solution:
    def recursiveFunc(self, currNum, n_maxNum, k_maxlen, currComb, answer) : 
        if (len(currComb) == k_maxlen) : 
            answer.append(currComb.copy())
            # print("Find - Add to answer : " + str(currComb))
            # print(answer)
            return

        
        if (currNum > n_maxNum) : 
            # print("error - overNumber : " + str(currNum))
            return
        
        
        
        for i in range(currNum ,n_maxNum+1) : 
            # print("level - " + str(i))
            currComb.append(i)
            #decide to include curr Number
            # print("include - " + str(currComb))
            self.recursiveFunc(i +1, n_maxNum, k_maxlen, currComb, answer)

            #decide not to include cur Number -> if we
            currComb.pop()
            # print("Not include - " + str(currComb))
            # self.recursiveFunc(currNum +1, n_maxNum, k_maxlen, currComb, answer)
            


        


    def combine(self, n: int, k: int) -> List[List[int]]:

        currComb = []
        answer = []
        self.recursiveFunc(1, n, k, currComb, answer)
        return answer

            



        #5,3 -> 1,2 1,3 1,4 1,5 2,3 2,4 2,5 3,

        