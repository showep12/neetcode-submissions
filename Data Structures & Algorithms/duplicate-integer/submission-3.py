class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        """
        Contains Duplicate (LC 217)

        Goal:
        Return True if any value appears at least twice.
        Otherwise, return False.

        Core idea:
        Maintain a hash set of values we've seen so far.
        - If a value is already in the set, it's a duplicate.
        - Otherwise, add it and continue.

        Why a set?
        - Average O(1) membership check and insertion.
        """

        seen = set()  # stores values already encountered

        for x in nums:
            # If x is already in 'seen', then we found a duplicate.
            if x in seen:
                return True

            # Otherwise, record that we've now seen x.
            seen.add(x)

        # If we finish scanning, no duplicates exist.
        return False

"""
[0. Problem Restatement]
Given an integer array nums, return true if any value appears at least twice.
Otherwise, return false.

[1. Brute Force]
Compare every pair (i, j). That takes O(n^2), which is too slow for large n.

[2. Key Insight]
We only need to know whether we've seen the current number before.
So we maintain a set of seen values.

[3. Data Structure Choice]
Use a hash set because it supports average O(1) membership checks and insertion.

[4. Algorithm]
Initialize an empty set seen.
For each number x in nums:
- If x is already in seen, we found a duplicate -> return True.
- Otherwise, add x to seen.
If we finish the loop, no duplicates -> return False.

[5. Complexity]
Time: O(n) average
Space: O(n)





Today we’ll solve “Contains Duplicate.”
We’re given an array of integers and we return true if any number appears at least twice.

The naive approach is to compare every pair of elements.
That is O(n^2), and it becomes too slow as n grows.

The key observation is that we don’t need positions or counts.
We only need a fast way to answer: “Have I seen this value before?”

That’s exactly what a hash set gives us: fast membership checks.
So we create an empty set called seen.

Then we iterate through the array:
- If the current number is already in seen, we have found a duplicate, so we return true immediately.
- Otherwise, we add the number to seen and continue.

If we reach the end without returning, it means no value repeated, so we return false.

This solution runs in O(n) average time because each set lookup and insertion is O(1) on average,
and it uses O(n) extra space in the worst case.

"""