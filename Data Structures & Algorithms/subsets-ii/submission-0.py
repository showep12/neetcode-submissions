class Solution:

    def dfs(self, level, nums, current, answer) : 
        if (level >= len(nums)) :  #if index = 3 -> out index error, return
            answer.append(current.copy())
            return 

        current.append(nums[level])
        self.dfs(level + 1, nums, current, answer)
        current.pop()
        while (level+1) < len(nums) and nums[level] == nums[level+1] : #should not reach to the last index -> level + 1 will occur out of index
              #즉 마지막 인덱스에서는 중복 체크 안함
            level += 1 #그냥 포함안한다의 조건에서 중복도 절대 포함 안할거라, 중복 원소있으면 어차피 포함안할거니 미리 index를 옮기는 거임                        
        self.dfs(level +1, nums, current, answer)


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        #order by list - nlogn
        nums.sort()
        
        answer = []
        current = []
        self.dfs(0, nums, current, answer)

        return answer
        #there is 3 case - include / contain / involve 
        #case 1 - include element
            #case 1-1 - include duplicate element
            #case 1-2 - skip duplicate element
        #case 2 - not include element
        

"""
Explanation for LeetCode Subsets II

In Subsets II, the key challenge is preventing duplicate subsets when the input array contains duplicate values.

At each index, we conceptually have two choices:

Include the current element

Exclude the current element

The crucial rule is how we handle the exclude case.

When we decide to exclude a value, we must exclude all of its consecutive duplicates at once.
If we exclude duplicate elements one by one, the recursion will generate the same subset through multiple paths, which results in duplicate outputs.

Therefore, in the exclude branch:

We advance the index forward while the next element is the same value.

This groups all identical values into a single exclude decision.

Then we continue recursion from the next distinct value.

In contrast:

The include branch does not skip duplicates, because including one occurrence versus including multiple occurrences leads to different subsets, which are valid and should be preserved.

In short:

Include branch → move to the next index normally

Exclude branch → skip all consecutive duplicates before recursing

This guarantees that:

Every unique subset is generated exactly once

No duplicate subsets appear in the result

Key sentence (one-liner summary)

In Subsets II, duplicates are handled by skipping all consecutive equal elements only in the exclude branch, ensuring that identical subsets are not generated multiple times.
"""
        