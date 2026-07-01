class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        Problem:
        Count the number of contiguous subarrays of length k
        whose average is >= threshold.

        Key transformation (very important):
        average >= threshold
        ⇔ (sum / k) >= threshold
        ⇔ sum >= k * threshold

        So instead of computing averages repeatedly (floating-point),
        we compare window sums against an integer target = k * threshold.
        """

        # target is the minimum sum a window must have to satisfy average >= threshold
        target = k * threshold

        # --- Step 1: Build the initial window sum (first k elements) ---
        # This is the sum of subarray arr[0 : k].
        window_sum = sum(arr[:k])

        # If the first window meets the condition, start count at 1; otherwise 0.
        count = 1 if window_sum >= target else 0

        # --- Step 2: Slide the window across the array ---
        # We move the window one position at a time:
        # - add the new element entering the window: arr[r]
        # - remove the old element leaving the window: arr[r - k]
        #
        # After the update, window_sum always represents the sum of:
        # arr[r - k + 1 : r + 1] (length k)
        for r in range(k, len(arr)):
            # Add the new rightmost element and subtract the element that leaves the window
            window_sum += arr[r] - arr[r - k]

            # Check the condition using the integer target
            if window_sum >= target:
                count += 1

        # count is the number of windows whose average >= threshold
        return count


# [0. Restate the problem]
# We are given an integer array arr, an integer k, and an integer threshold.
# We need to count how many contiguous subarrays of length k
# have an average that is greater than or equal to threshold.

# [1. Key observation / algebraic transformation]
# Computing averages directly would be inefficient and also introduces floating-point concerns.
# Instead, I convert the condition:

# average >= threshold
# ⇔ (sum / k) >= threshold
# ⇔ sum >= k * threshold

# So the problem reduces to:
# Count how many windows of length k have sum at least target,
# where target equals k times threshold.

# [2. Why sliding window]
# We need to evaluate every length-k subarray.
# There are O(n) such windows, and each window differs from the previous one by exactly:
# - one outgoing element
# - one incoming element

# Sliding window allows updating the sum in O(1) per move,
# which yields a linear-time solution.

# [3. Algorithm steps]
# Step A: Compute the sum of the first window arr[0 : k].
# If it is >= target, initialize the count to 1.

# Step B: Slide the window from left to right.
# For each new right index r:
# - add arr[r] to the running sum
# - subtract arr[r - k] (the element that leaves the window)

# After updating, window_sum represents the current window sum,
# so I compare it to target and increment count if it meets the condition.

# [4. Correctness argument]
# At every iteration, window_sum equals the sum of exactly k consecutive elements.
# Because the condition sum >= k * threshold is equivalent to average >= threshold,
# each time we increment the count we are counting a valid subarray,
# and we count all such windows exactly once.

# [5. Complexity]
# Time complexity is O(n):
# - we compute the first sum in O(k),
# - and then perform O(1) updates for each of the remaining n-k windows.

# Space complexity is O(1),
# since we only store a few integers regardless of input size.

# [6. Closing]
# This is optimal because any solution must at least inspect each element,
# and the sliding window gives the minimum overhead per window.


