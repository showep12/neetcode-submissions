from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        Goal:
        Find the minimal length of a contiguous subarray with sum >= target.
        If no such subarray exists, return 0.

        Key requirement for this sliding window approach:
        nums contains positive integers.
        This guarantees monotonic behavior:
        - Expanding the window (moving R) increases or keeps the sum.
        - Shrinking the window (moving L) decreases the sum.
        """

        # L is the left boundary of the sliding window.
        L = 0

        # curSum will always represent sum(nums[L .. R]) for the current R.
        curSum = 0

        # Initialize minLen with an impossible large value.
        # If we never update it, it means no valid window exists.
        minLen = len(nums) + 1

        # R is the right boundary; we expand the window by moving R forward.
        for R in range(len(nums)):

            # Step 1: Expand window by including nums[R]
            curSum += nums[R]

            # Step 2: If the window is valid (curSum >= target),
            # shrink it from the left as much as possible to minimize its length.
            #
            # Why while-loop?
            # Because for a fixed R, we want the smallest L such that sum >= target.
            while curSum >= target:
                # At this point, nums[L .. R] is a valid window.
                # Update the best answer using its length.
                minLen = min(minLen, R - L + 1)

                # Now try to shrink the window:
                # remove nums[L] (the outgoing element) and move L right.
                curSum -= nums[L]
                L += 1

                # After shrinking, either:
                # - The window is still valid → keep shrinking,
                # - Or it becomes invalid → stop shrinking and continue expanding with R.

        # If minLen was never updated, no valid subarray exists.
        return 0 if minLen == len(nums) + 1 else minLen


"""
[0. Restate the problem]
Given an array of positive integers nums and an integer target,
find the minimal length of a contiguous subarray whose sum is at least target.
If no such subarray exists, return 0.

[1. Why brute force is too slow]
Brute force checks all subarrays: O(n^2) possible ranges,
and summing them can be O(n) each unless optimized.
We want O(n).

[2. Key observation]
All numbers are positive.
That means:
- Expanding the window to the right can only increase the sum.
- Shrinking the window from the left can only decrease the sum.
This monotonic behavior is exactly what makes sliding window valid.

[3. Strategy: variable-size sliding window]
Maintain a window [L..R] and its running sum.
- Move R to expand until sum >= target.
- Then shrink from L as much as possible while still keeping sum >= target,
  because we want the minimal length.

[4. Invariants]
Invariant 1: curSum is always the sum of nums[L..R].
Invariant 2: When we enter the while loop, the window is valid (curSum >= target).
Invariant 3: After the while loop finishes, the window is minimal for that R
            (i.e., shrinking further would break validity).

[5. Correctness]
For each R, shrinking in the while-loop guarantees we consider the smallest valid window ending at R.
Taking the global minimum across all R yields the true minimal length.

[6. Complexity]
Each element enters the window once (when R moves),
and leaves the window at most once (when L moves).
So total pointer movement is O(n), and time is O(n).
Space is O(1).

"""

"""
We need the minimum length of a contiguous subarray whose sum is at least target.
If it doesn’t exist, return zero.

A brute-force approach would consider all subarrays, which is O(n^2),
so we need something faster.

The key property is that all numbers are positive.
Because of that, when we move the right pointer to the right, the sum never decreases.
And when we move the left pointer to the right, the sum never increases.
This monotonic behavior allows a variable-size sliding window.

I maintain two pointers L and R and a running sum curSum for the window nums[L..R].
I expand the window by moving R forward and adding nums[R] to curSum.
Once curSum becomes at least target, the window is valid,
but it might not be minimal, so I shrink it from the left.

While curSum is still at least target,
I update the answer with the current window length R - L + 1,
then I subtract nums[L] and increment L to make the window smaller.
That shrinking loop guarantees that for each fixed R,
I find the smallest valid window ending at R.

Across all R, I keep the global minimum length.
If I never find a valid window, I return 0.

In terms of complexity, each element is added once when R moves,
and removed at most once when L moves.
So both pointers move at most n times, making the total time O(n),
with O(1) extra space.

"""