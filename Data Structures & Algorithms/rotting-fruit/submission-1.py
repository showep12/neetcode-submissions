from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #So, An impossible case means that some fresh oranges can not be reached by rotten oranges

# Keep in mind that all rotten oranges spread the rot simultaneously.
# So, we need to track the state minute by minute. This means we must
# extract all current rotten oranges from the queue and explore their adjacent cells.
# If we find any adjacent fresh oranges, we add them to the queue as the next rotten oranges.


        # [치면서 할 말] I will make a deque named rotten_oranges.
        # [인터뷰 설명] I'm initializing a queue to track the initial positions of rotten oranges.
        # [실제 주석]     # Queue to track coordinates of rotten oranges for BFS
        rotten_oranges = deque()

        # [치면서 할 말] Next, directions equals down, up, right, left.
        # [인터뷰 설명] Here, I'm setting up the 4-directional offsets to explore adjacent cells.
        # [실제 주석]     # Offsets for 4-directional neighbor exploration
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        row_len = len(grid)
        col_len = len(grid[0])        

        for row in range(row_len) : 
            for col in range(col_len) : 
                if grid[row][col] == 2 : 
                    rotten_oranges.appendleft((row,col))

        time = 0
        
        while rotten_oranges :             
            
            for _ in range(len(rotten_oranges)) : 
                curr_row, curr_col = rotten_oranges.pop()
                print("curr",curr_row, curr_col)
                print("time",time)
                for dr_row, dr_col in directions : 
                    next_row, next_col = curr_row + dr_row, curr_col + dr_col
                    print("next",next_row, next_col)
                    if (0<= next_row < row_len and
                       0<= next_col < col_len and
                       grid[next_row][next_col] == 1) : 
                       print("hit",grid[next_row][next_col])
                       grid[next_row][next_col] = 2
                       rotten_oranges.appendleft((next_row,next_col))
            if len(rotten_oranges) > 0 :
                time += 1
        

        for row in range(row_len) : 
            for col in range(col_len) : 
                if grid[row][col] == 1 : 
                    return -1
        return time