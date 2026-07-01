# ==============================================================================
# 1. 문제 접근 및 분석 단계 (Approach & Analysis)
# ==============================================================================

# [치면서 할 말] This is a grid problem, and the rot spreads at the same time, so I will use BFS.
# [인터뷰 설명] Since the rot spreads simultaneously from multiple sources, this naturally maps to a Breadth-First Search (BFS) approach. 
# [실제 노트]     # Approach: Multi-source BFS because of simultaneous spreading.


# [치면서 할 말] I need to find all rotten oranges first and count the fresh ones.
# [인터뷰 설명] First, I'll scan the grid to find all initial rotten oranges to populate the queue, and also count the total fresh oranges to check the impossible cases later.
# [실제 노트]     # Strategy: Scan grid for initial rotten states and fresh orange count.


# ==============================================================================
# 2. 실제 구현 및 설명 단계 (Implementation)
# ==============================================================================

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # [치면서 할 말] I will make a deque named rotten_oranges.
        # [인터뷰 설명] I'm initializing a queue to track the initial positions of rotten oranges.
        # [실제 주석]     # Queue to track coordinates of rotten oranges for BFS
        rotten_oranges = deque()

        # [치면서 할 말] Next, directions equals down, up, right, left.
        # [인터뷰 설명] Here, I'm setting up the 4-directional offsets to explore adjacent cells.
        # [실제 주석]     # Offsets for 4-directional neighbor exploration
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        # [치면서 할 말] I need to get the grid size for rows and columns.
        # [인터뷰 설명] First, I will store the row and column dimensions of the grid.
        # [실제 주석]     # Get grid dimensions
        row_len = len(grid)
        col_len = len(grid[0])        

        # [치면서 할 말] I will loop through the grid and find all rotten oranges.
        # [인터뷰 설명] I'm iterating through the grid to find the initial coordinates of the rotten oranges and push them into our queue.
        # [실제 주석]     # Find initial rotten oranges and enqueue them
        for row in range(row_len) : 
            for col in range(col_len) : 
                if grid[row][col] == 2 : 
                    rotten_oranges.appendleft((row,col))

        # [치면서 할 말] I will initialize the time variable to zero.
        # [인터뷰 설명] I will set up a time tracker starting at zero minutes.
        # [실제 주석]     # Track elapsed time in minutes
        time = 0
        
        # [치면서 할 말] While the queue has elements, I will run the BFS loop.
        # [인터뷰 설명] We run the standard BFS loop to process the rotten oranges layer by layer.
        # [실제 주석]     # BFS loop for minute-by-minute spread
        while rotten_oranges :             
            
            # [치면서 할 말] I will loop through the current size of the queue to handle this minute.
            # [인터뷰 설명] By locking the queue size for the current loop, we ensure we only process the oranges that turned rotten in the same minute.
            # [실제 주석]     # Process all oranges rotten at the current minute mark
            for _ in range(len(rotten_oranges)) : 
                curr_row, curr_col = rotten_oranges.pop()
                
                # [치면서 할 말] I will check all four directions around the current orange.
                # [인터뷰 설명] We look at the adjacent neighbors in all four directions.
                # [실제 주석]     # Explore 4-way neighbors
                for dr_row, dr_col in directions : 
                    next_row, next_col = curr_row + dr_row, curr_col + dr_col
                    
                    # [치면서 할 말] If the next cell is in bounds and has a fresh orange, I will turn it rotten.
                    # [인터뷰 설명] If the neighbor is within the grid boundaries and contains a fresh orange, we infect it.
                    # [실제 주석]     # Check boundary conditions and if the neighbor is fresh
                    if (0 <= next_row < row_len and
                       0 <= next_col < col_len and
                       grid[next_row][next_col] == 1) : 
                       
                       # [치면서 할 말] I will change the grid value to two and add it to the queue.
                       # [인터뷰 설명] We mark the fresh orange as rotten and push its coordinates into the queue for the next minute.
                       # [실제 주석]     # Infect fresh orange and add to queue
                       grid[next_row][next_col] = 2
                       rotten_oranges.appendleft((next_row,next_col))
                       
            # [치면서 할 말] If there are new rotten oranges in the queue, I will increase time by one.
            # [인터뷰 설명] If any fresh oranges were newly infected during this round, we increment our time counter.
            # [실제 주석]     # Increment time only if new infections occurred
            if len(rotten_oranges) > 0 :
                time += 1
        
        # [치면서 할 말] I will check the grid one more time for any remaining fresh oranges.
        # [인터뷰 설명] After BFS finishes, we inspect the grid. If there are still fresh oranges left, it means they are isolated, so we return negative one.
        # [실제 주석]     # Check for any remaining fresh oranges (impossible cases)
        for row in range(row_len) : 
            for col in range(col_len) : 
                if grid[row][col] == 1 : 
                    return -1
                    
        # [치면서 할 말] If everything is okay, I will return the total time.
        # [인터뷰 설명] Otherwise, we successfully turned all oranges rotten and return the total minutes elapsed.
        # [실제 주석]     # Return total minutes taken
        return time


# ==============================================================================
# 3. 복잡도 분석 단계 (Complexity Analysis)
# ==============================================================================

# [치면서 할 말] Time complexity is O(N * M) because we visit each cell.
# [인터뷰 설명] The time complexity is O(V + E), which simplifies to O(N by M) where N is rows and M is columns, because we visit each cell a constant number of times.
# [실제 주석]     # Time Complexity: O(N * M) - Each cell is visited at most a constant number of times.


# [치면서 할 말] Space complexity is O(N * M) because of the queue.
# [인터뷰 설명] The space complexity is also O(N by M) in the worst case, because the queue can hold up to all the oranges if the entire grid is rotten.
# [실제 주석]     # Space Complexity: O(N * M) - Worst-case size of the BFS queue.


# ==============================================================================
# 4. 코드 검증 단계 (Dry Run / Trace)
# ==============================================================================

# [치면서 할 말] Let's do a dry run with a simple 2 by 2 grid.
# [인터뷰 설명] Let's trace the logic with a simple two-by-two grid to ensure the edge cases and boundaries work correctly.
# [실제 노트]     # Dry Run: Grid [[2, 1], [1, 0]]


# [치면서 할 말] At minute 0, queue has (0,0). Fresh count is 2.
# [인터뷰 설명] At minute zero, the queue is initialized with the coordinates zero-zero, and the fresh orange count stands at two.
# [실제 노트]     # T=0: queue=[(0,0)], fresh_count=2


# [치면서 할 말] At minute 1, we pop (0,0) and infect (0,1) and (1,0). They go to the queue.
# [인터뷰 설명] In the first iteration, we pop zero-zero, explore its neighbors, and infect zero-one and one-zero. These new rotten coordinates are then pushed back into the queue.
# [실제 노트]     # T=1: pop (0,0) -> infect (0,1), (1,0) -> queue=[(1,0), (0,1)]


# [치면서 할 말] The queue becomes empty, and no fresh oranges left. Return time.
# [인터뷰 설명] The queue eventually becomes empty. We check the remaining fresh count—it's zero, so the code successfully returns the final elapsed time.
# [실제 노트]     # Final: Queue empty, fresh_count=0 -> return time