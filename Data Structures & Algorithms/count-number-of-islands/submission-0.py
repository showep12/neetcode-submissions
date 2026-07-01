class Solution:
    def dfs(self, currRow, currCol, grid, visitGlobal, visitTemp, answers) : 
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) -1

        if (currRow < 0 or
            currCol < 0 or
            currRow > maxRow or
            currCol > maxCol or            
            (currRow, currCol) in visitGlobal
           ) : 
           return 
        print("c")
        print(grid[currRow][currCol])

        if grid[currRow][currCol] == "1" :             
            visitGlobal.append((currRow,currCol))
            visitTemp.append((currRow,currCol))
            print("d")
            print(visitTemp)
            self.dfs(currRow + 1, currCol, grid, visitGlobal, visitTemp, answers)
            self.dfs(currRow, currCol + 1,  grid, visitGlobal, visitTemp, answers)
            self.dfs(currRow - 1, currCol,  grid, visitGlobal, visitTemp, answers)
            self.dfs(currRow, currCol - 1,  grid, visitGlobal, visitTemp, answers)
        
        else : #if it is 0, water, we can not go further 
            return


    def numIslands(self, grid: List[List[str]]) -> int:
        visitGlobal = []
        visitTemp = []
        answer = []

        for row in range(len(grid)) : 
            for col in range(len(grid[0])) : 
                if (grid[row][col] == "1") :
                    if ((row,col) in visitGlobal) : 
                        print("already visited")
                        continue
                    else : 
                        visitTemp = []
                        print("new Land!!")
                        self.dfs(row,col, grid, visitGlobal, visitTemp, answer)
                        answer.append(visitTemp)
        print(answer)
        return len(answer)
        #for every position, they order there children to report
        #visit every land, and check it is visited before
        #if we visit new land but it is alreay visited 

        