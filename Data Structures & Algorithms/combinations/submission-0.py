class Solution:

    def dfs(self, level, n, k, comb, answer) : 
        if (len(comb) == k) : 
            answer.append(comb.copy())
            return

        if level > n : 
            return

        comb.append(level)
        self.dfs(level+1, n, k, comb, answer)

        comb.pop()
        self.dfs(level+1, n, k, comb, answer)






    def combine(self, n: int, k: int) -> List[List[int]]:
        #for each number, recursively enter and choose to include or not
        #if we reach the target lenth, add the combination to answer and return
        #

        comb = []
        answer = []
        self.dfs(1, n, k, comb,answer)
        return answer

        