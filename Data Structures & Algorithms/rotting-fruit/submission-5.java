// ==============================================================================
// 1. 문제 접근 및 알고리즘 선택 이유 (Deep Strategy & Justification)
// ==============================================================================

// [치면서 할 말] Why do we use BFS instead of DFS? Because this is a shortest-path problem in terms of time.
// [인터뷰 설명] The fundamental reason we choose BFS over DFS here is that this is essentially a 'shortest-time' or 'shortest-path' problem. DFS explores a single path to its absolute end before backtracking, which is blind to time. BFS, on the other hand, expands like a wave, ensuring that when an orange is reached, it is reached via the minimum possible number of minutes.
// [해석]        여기서 DFS 대신 BFS를 선택하는 근본적인 이유는 이 문제가 본질적으로 '최단 시간' 또는 '최단 경로' 문제이기 때문입니다. DFS는 한 경로의 끝까지 파고든 뒤 역추적(Backtracking)하므로 시간에 무감각합니다. 반면 BFS는 파도처럼 사방으로 확장하기 때문에, 어떤 오렌지에 도달하는 순간 그게 '최소 몇 분 만에' 도달한 것인지를 보장해 줍니다.
// [실제 노트]     # Why BFS: DFS is time-blind. BFS guarantees the shortest path/time because of wave-like expansion.


// [치면서 할 말] Also, we have multiple rotten oranges starting at the same time.
// [인터뷰 설명] Furthermore, because the rot starts from multiple sources simultaneously, we need a mechanism that can manage concurrent timelines. A standard single-source algorithm won't work. A multi-source BFS allows us to inject all initial rotten coordinates into Level 0, ensuring that every independent infection wave advances at the exact same pace.
// [해석]        게다가, 여러 상한 오렌지가 동시에 시작하기 때문에 우리는 동시다발적인 타임라인을 관리할 메커니즘이 필요합니다. 일반적인 단일 시작점 알고리즘은 통하지 않죠. 멀티 소스 BFS를 사용하면 초기 상한 좌표들을 전부 레벨 0에 집어넣어, 각각의 독립적인 오염 파도가 정확히 동일한 속도로 전진하도록 만들 수 있습니다.
// [실제 노트]     # Multi-source Strategy: Enqueue all sources at Level 0 to keep concurrent timelines in sync.


// ==============================================================================
// 2. 실제 구현 및 설명 단계 (Implementation)
// ==============================================================================



class Solution {
    public int orangesRotting(int[][] grid) {
        // [치면서 할 말] I will initialize a queue to store the coordinates as int arrays.
        // [인터뷰 설명] I'm initializing a standard Java Queue implemented as a LinkedList to track the coordinates of rotten oranges.
        // [실제 주석]     // Queue to track coordinates of rotten oranges for BFS
        Queue<int[]> rottenOranges = new LinkedList<>();

        // [치면서 할 말] Next, I will define the 4-directional offsets.
        // [인터뷰 설명] Here, I'm setting up the 2D direction array for our 4-directional neighbor exploration.
        // [실제 주석]     // Offsets for 4-directional neighbor exploration
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        // [치면서 할 말] I need to get the grid size for rows and columns.
        // [인터뷰 설명] First, I will store the row and column dimensions of the grid.
        // [실제 주석]     // Get grid dimensions
        int rowLen = grid.length;
        int colLen = grid[0].length;

        // [치면서 할 말] I will loop through the grid and find all rotten oranges.
        // [인터뷰 설명] I'm iterating through the matrix to locate the initial coordinates of the rotten oranges and push them into the queue.
        // [실제 주석]     // Find initial rotten oranges and enqueue them
        for (int r = 0; r < rowLen; r++) {
            for (int c = 0; c < colLen; c++) {
                if (grid[r][c] == 2) {
                    rottenOranges.offer(new int[]{r, c});
                }
            }
        }

        // [치면서 할 말] I will initialize the time variable to zero.
        // [인터뷰 설명] I will set up a minutes counter starting at zero.
        // [실제 주석]     // Track elapsed time in minutes
        int time = 0;

        // [치면서 할 말] While the queue is not empty, I will run the BFS loop.
        // [인터뷰 설명] We run the standard BFS loop to process the rotten oranges layer by layer.
        // [실제 주석]     // BFS loop for minute-by-minute spread
        while (!rottenOranges.isEmpty()) {
            
            // [치면서 할 말] I will lock the current size of the queue for this level.
            // [인터뷰 설명] By locking the queue size at the start of each layer, we ensure we only process the oranges that turned rotten at the exact same minute mark.
            // [실제 주석]     // Process all oranges rotten at the current minute mark
            int size = rottenOranges.size();
            for (int i = 0; i < size; i++) {
                int[] curr = rottenOranges.poll();
                int currRow = curr[0];
                int currCol = curr[1];

                // [치면서 할 말] I will check all four directions around the current cell.
                // [인터뷰 설명] We look at the adjacent neighbors in all four directions.
                // [실제 주석]     // Explore 4-way neighbors
                for (int[] dir : directions) {
                    int nextRow = currRow + dir[0];
                    int nextCol = currCol + dir[1];

                    // [치면서 할 말] If the next cell is inside bounds and has a fresh orange, I will turn it rotten.
                    // [인터뷰 설명] If the neighbor is within the grid boundaries and contains a fresh orange, we infect it.
                    // [실제 주석]     // Check boundary conditions and if the neighbor is fresh
                    if (nextRow >= 0 && nextRow < rowLen && nextCol >= 0 && nextCol < colLen && grid[nextRow][nextCol] == 1) {
                        
                        // [치면서 할 말] I will change the grid value to two and add it to the queue.
                        // [인터뷰 설명] We mark the fresh orange as rotten and push its coordinates into the queue for the next minute mark.
                        // [실제 주석]     // Infect fresh orange and add to queue
                        grid[nextRow][nextCol] = 2;
                        rottenOranges.offer(new int[]{nextRow, nextCol});
                    }
                }
            }

            // [치면서 할 말] If the queue still has elements, it means a new wave happened, so increase time.
            // [인터뷰 설명] If there are newly infected oranges waiting in the queue, it means another minute has passed, so we increment the timer.
            // [실제 주석]     // Increment time only if a next wave exists
            if (!rottenOranges.isEmpty()) {
                time++;
            }
        }

        // [치면서 할 말] I will check the grid one more time for any fresh oranges left.
        // [인터뷰 설명] After the BFS process completely finishes, we scan the grid once more. If there are any isolated fresh oranges left, we return negative one.
        // [실제 주석]     // Check for any remaining fresh oranges (impossible cases)
        for (int r = 0; r < rowLen; r++) {
            for (int c = 0; c < colLen; c++) {
                if (grid[r][c] == 1) {
                    return -1;
                }
            }
        }

        // [치면서 할 말] If everything is okay, I will return the total time.
        // [인터뷰 설명] Otherwise, we successfully turned all oranges rotten and return the total elapsed minutes.
        // [실제 주석]     // Return total minutes taken
        return time;
    }
}


// ==============================================================================
// 3. 복잡도 분석 단계 (Complexity Analysis)
// ==============================================================================

// [치면서 할 말] Time complexity is O(N * M) because we visit each cell.
// [인터뷰 설명] The time complexity is O(V + E), which simplifies to O(N by M) where N is rows and M is columns, because we visit each cell a constant number of times.
// [실제 주석]     // Time Complexity: O(N * M) - Each cell is visited at most a constant number of times.


// [치면서 할 말] Space complexity is O(N * M) because of the queue.
// [인터뷰 설명] The space complexity is also O(N by M) in the worst case, because the queue can hold up to all the oranges if the entire grid is rotten.
// [실제 주석]     // Space Complexity: O(N * M) - Worst-case size of the BFS queue.


// ==============================================================================
// 4. 코드 검증 단계 (Dry Run / Trace)
// ==============================================================================

// [치면서 할 말] Let's do a dry run with a simple 2 by 2 grid.
// [인터뷰 설명] Let's trace the logic with a simple two-by-two grid to ensure the edge cases and boundaries work correctly.
// [실제 노트]     # Dry Run: Grid [[2, 1], [1, 0]]


// [치면서 할 말] At minute 0, queue has (0,0). Fresh count is 2.
// [인터뷰 설명] At minute zero, the queue is initialized with the coordinates zero-zero, and the fresh orange count stands at two.
// [실제 노트]     # T=0: queue=[(0,0)], fresh_count=2


// [치면서 할 말] At minute 1, we pop (0,0) and infect (0,1) and (1,0). They go to the queue.
// [인터뷰 설명] In the first iteration, we pop zero-zero, explore its neighbors, and infect zero-one and one-zero. These new rotten coordinates are then pushed back into the queue.
// [실제 노트]     # T=1: pop (0,0) -> infect (0,1), (1,0) -> queue=[(1,0), (0,1)]


// [치면서 할 말] The queue becomes empty, and no fresh oranges left. Return time.
// [인터뷰 설명] The queue eventually becomes empty. We check the remaining fresh count—it's zero, so the code successfully returns the final elapsed time.
// [실제 노트]     # Final: Queue empty, fresh_count=0 -> return time


// ==============================================================================
// 5. 실무 도메인 매핑 & 한 줄 평 (Real-world Use Cases & High-Level Phrase)
// ==============================================================================

// ------------------------------------------------------------------------------
// 실무 케이스 1: 마이크로서비스 장애 전파 (Blast Radius / Cascading Failure)
// ------------------------------------------------------------------------------
// [인터뷰 설명] In distributed systems, this exact multi-source BFS logic is used to calculate the blast radius of a service outage. If Service A and Service B go down simultaneously, we track how that failure propagates to adjacent downstream dependencies minute by minute to prevent a total cascading failure.
// [해석]        분산 시스템에서 이 정확한 멀티 소스 BFS 로직은 서비스 장애의 폭발 반경(Blast Radius)을 계산하는 데 사용됩니다. 서비스 A와 B가 동시에 다운되면, 전체 시스템의 연쇄 장애를 막기 위해 그 실패가 인접한 다운스트림 의존성으로 분 단위로 어떻게 전파되는지 추적합니다.
// [실제 노트]     # Real-world 1: Outage blast radius analysis in microservices.


// ------------------------------------------------------------------------------
// 실무 케이스 2: 소셜 네트워크 시스템의 알림 푸시 (Notification Fan-out)
// ------------------------------------------------------------------------------
// [인터뷰 설명] This is also directly connected to the fan-out architecture in social media systems. When high-profile creators post content, that update acts like a rotten orange, spreading radially through the follow-graph to reach active users' feeds in near real-time.
// [해석]        이것은 소셜 미디어 시스템의 팬아웃(Fan-out) 아키텍처와도 직접 연결됩니다. 영향력 있는 크리에이터가 콘텐츠를 게시하면, 그 업데이트는 상한 오렌지처럼 작동하여 팔로우 그래프를 통해 방사형으로 퍼져나가 실시간에 가깝게 활성 사용자의 피드에 도달하게 됩니다.
// [실제 노트]     # Real-world 2: Live notification and feed fan-out simulation.


// ------------------------------------------------------------------------------
// 6. 인터뷰 뇌절 단계 (Advanced Trade-off Exploration)
// ------------------------------------------------------------------------------

// [인터뷰 설명] From a production standpoint, we must consider the memory footprint. In a worst-case scenario where the grid is massive and infections peak, storing O(N by M) coordinates in a raw queue could cause an Out-Of-Memory (OOM) error. If I were designing this for a large-scale real-world network, I would consider a batched or sliding-window processing model to throttle memory consumption.
// [해석]        실제 운영 환경 관점에서 우리는 메모리 사용량을 고려해야 합니다. 그리드가 거대하고 오염이 정점에 달하는 최악의 시나리오에서는 생 큐(Raw queue)에 O(N*M)개의 좌표를 저장하다가 OOM(메모리 고갈) 에러가 날 수 있습니다. 만약 대규모 실무 네트워크를 위해 이걸 설계한다면, 메모리 소비를 조절하기 위해 배치 처리나 슬라이딩 윈도우 모델을 고려할 것입니다.
// [실제 노트]     # Scale Trade-off: High memory footprint in peak waves. Consider throttling or batching to avoid OOM.


// ------------------------------------------------------------------------------
// 7. 인터뷰 치트키 한 줄 평 (Interview High-Level Phrase)
// ------------------------------------------------------------------------------
// [인터뷰 설명] Ultimately, this grid problem is an elegant, simplified simulation of dependency propagation and blast radius analysis in distributed networks.
// [해석]        궁극적으로, 이 그리드 문제는 분산 네트워크에서의 의존성 전파 및 폭발 반경 분석을 우아하게 단순화한 시뮬레이션입니다.
// [실제 노트]     # Summary: Grid BFS = Simplified network propagation.