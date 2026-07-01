class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        #prefix_sum
        prefix_sum = [0]*(len(nums) + 1)
        curr_sum = 0
        for idx in range(len(nums)) : 
            prefix_sum[idx+1] = prefix_sum[idx] + nums[idx]
        print(prefix_sum)
        #prefix_sum [0,2,1,2,4]


        #subarray sum(left,right) = from nums[left] .. nums[left +1]....nums[right]
        #= prefix_sum[right+1] - prefix_sum[left] 
        #prefix_sum [0,2,1,2,4] -> target 2 
        #prefix_sum[1] - prefix_sum[0] = 2 == target
        #prefix_sum[2] - prefix_sum[0] = 1 != target

        #iterate prefix_sum -> we check if we saw the other value before
        #   current_prefix_sum - left_prefix_sum = target k
        #   memo the current prefix_sum
        #   check the need value = left_prefix_sum = current_prefix_sum - target k

        hash_lefsum_seen = {}    
        cnt = 0
        print(prefix_sum)
        for num in prefix_sum : 
            #prefix_sum [0,2,1,2,4]
            need_leftsum = num - k
            if (need_leftsum in hash_lefsum_seen) : 
                cnt += hash_lefsum_seen[need_leftsum]
            hash_lefsum_seen[num] = hash_lefsum_seen.get(num,0) + 1
        
        return cnt

        
        #[2,-1,1,2] target = 2
        #[2](idx0) / [2,-1,1] / [-1,1,2] / [2] (idx3)

        #[2,1,2,4] target = 2
        #[0,2,1,2,4] target = 2
        #{0:2, }
        #two sum
        #[1,4,2,5,2] -> remember 1 remain value and it's index
        #

        #[0,2,1,2,4] # target = 2
        #current_sum - previous_sum = k
        #prev_sum = curr_sum - k        
        #0 -> currsum = 0 / need = prevsum = -2 
        #     currsum - prevsum = k 
        #     hash {0:1}

        #1 -> currsum = 2 / need = prevsum = 0
        #     currsum - prevsum = k 
        #     hash {0:1, 2:1} cnt + 1

        #2 -> currsum = 1 / need = prevsum = -1
        #     currsum - prevsum = k
        #     hash {0:1, 2:1, 1:1}

        #3 -> currsum = 2 / need prevsum = 0
        #     currsum - prevsum = k
        #     hash {0:1, 2:2, 1:1} cnt + 1

        #4 -> currsum = 4 / need = prevsum = 2
        #     currsum - prevsum = k
        #     hash {0:1, 2:1, 1:1} cnt + 2

        #1 -> currsum = 2 / need = 2-2 = 0 / {0:1, 2:1} cnt+1
        #2 -> currsum = 1 / need = 2-1 = 1 / {0:1, 2:1, 1:1}

        #[2,0,1,0,2]
        #1 meet 


        #{2:1, 0:2, 1:1, -2:1}

        #1 meet 0 -> {0(curr):1}
        #2 meet 2 -> check if we met 0(target-curr) -> cnt +1
        #         -> {0(prev):1, 2:1}
        #3 meet 1 -> check we met 1 -> no
        #           -> {0:1, 2:1, 1:1}
        #4 meet 2 -> check if we met 0 -> cnt + 1 -> cnt = 2
        #5 meet 4 -> check if we met (-2)


        #0,2 find
        #0,

        #brute force 
        #O(n^2)
        # cnt = 0
        # for i in range(len(nums)) : 
        #     cum_sum = 0
        #     for j in range(i,len(nums)) :
        #         cum_sum += nums[j]
        #         if cum_sum == k :
        #             cnt +=1 
        
        # return cnt
