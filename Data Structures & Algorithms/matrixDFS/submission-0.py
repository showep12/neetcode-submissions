class Solution:

    def dfs(self, currRow, currCol, grid, visit) : 
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1 

        if (currRow > maxRow or
            currCol > maxCol or
            currRow < 0 or
            currCol < 0 or
            grid[currRow][currCol] == 1 or
            (currRow, currCol) in visit
           ) : 
            return 0
        
        if (currRow == maxRow and currCol == maxCol) : 
            return 1
        
        visit.append((currRow, currCol))
        #object of visit - to avoid duplicate visit
        count = 0 #calculate possible ways at the current position
        count += self.dfs(currRow + 1, currCol, grid, visit)
        count += self.dfs(currRow, currCol + 1, grid, visit)
        count += self.dfs(currRow - 1, currCol, grid, visit)
        count += self.dfs(currRow, currCol - 1, grid, visit)

        visit.remove((currRow, currCol))
        return count #always return to mother
        
    def countPaths(self, grid: List[List[int]]) -> int:
        
        
        visit = []        
        answer = self.dfs(0,0, grid, visit)
        return answer
        #for each cells, visit 4 different ways
        #recursively, we calculate every possible ways
        #for each step, report to mother the result