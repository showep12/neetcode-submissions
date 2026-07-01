from typing import Dict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Longest Repeating Character Replacement (LC 424)

        We want the largest window [L..R] such that we can turn ALL characters in the window
        into the same character using at most k replacements.

        For a window:
          window_len = R - L + 1
          maxCount = max frequency of any single character in the window
          replacements_needed = window_len - maxCount

        Valid condition:
          (R - L + 1) - maxCount <= k

        Approach:
          Sliding window + frequency map + maxCount integer.

        Time Complexity: O(n)
        Space Complexity: O(1) for fixed alphabet (A-Z), otherwise O(min(n, alphabet))
        """

        # Edge case: empty string
        if not s:
            return 0

        # count[ch] = how many times ch appears in the current window
        count: Dict[str, int] = {}

        L = 0
        maxCount = 0  # highest frequency of ANY character we've seen in the window while expanding
        maxLen = 0

        for R, ch in enumerate(s):
            # --- 1) Expand window: include s[R] ---
            count[ch] = count.get(ch, 0) + 1

            # Update maxCount based on the new character's count
            # maxCount is an integer, not a character.
            maxCount = max(maxCount, count[ch])

            # --- 2) If window is invalid, shrink from the left ---
            # If we need more than k replacements, window is too "diverse"
            while (R - L + 1) - maxCount > k:
                leftChar = s[L]
                count[leftChar] -= 1
                L += 1

                # Important note:
                # We do NOT recompute maxCount here.
                # It may become stale, but correctness still holds with this standard technique.

            # --- 3) Update the answer (window is valid here) ---
            maxLen = max(maxLen, R - L + 1)

        return maxLen

"""
[0. Problem Restatement]
Given a string s and an integer k, return the length of the longest substring
that can be transformed into a string of the same repeating character by replacing
at most k characters.

[1. Brute Force is too slow]
Brute force would check every substring and count how many replacements are needed.
That leads to O(n^2) substrings, and each check can cost O(n), which is too slow.

[2. Key Insight]
For a window s[L..R], suppose the most frequent character in that window appears maxCount times.
To make all characters the same, we keep that most frequent character and replace the rest.
So replacements_needed = window_len - maxCount.

The window is valid if:
  (R - L + 1) - maxCount <= k

[3. Technique]
Use a variable-size sliding window with two pointers L and R.
Maintain a frequency map for characters inside the window.
Track maxCount = the maximum frequency of any single character encountered while expanding.

[4. Invariant]
We maintain a window that is "valid enough" according to:
  window_len - maxCount <= k
If it becomes invalid, we shrink from the left until it becomes valid again.

[5. Why maxCount can be an integer only (no need to track the character)]
We only need the count of the most frequent character, not which character it is.

[6. The famous trick: we do not recompute maxCount when shrinking]
maxCount may become stale (too large) after shrinking.
However, this does not break correctness:
- A stale (larger) maxCount makes the window look more valid than it truly is,
  which only delays shrinking.
- Since R only moves forward and we record maxLen from windows that pass the check,
  the final maximum length remains correct under this standard pattern.

[7. Complexity]
Each pointer moves forward at most n times.
Time: O(n)
Space: O(1) if alphabet is fixed (e.g., uppercase A-Z), otherwise O(min(n, alphabet)).






Today we’ll solve “Longest Repeating Character Replacement.”

We’re given a string s and an integer k.
We want the maximum length of a substring that can be transformed into a string where
all characters are identical, by replacing at most k characters.

The key idea is to look at a sliding window [L..R].
Inside this window, suppose the most frequent character appears maxCount times.
If we choose that character as the final repeating character,
we can keep those maxCount occurrences and replace every other character.
So the minimum replacements needed is:

replacements_needed = window_len - maxCount

Therefore, the window is valid if:
window_len - maxCount <= k

Now we implement a variable-size sliding window:
- Expand R to include new characters.
- Update a frequency map.
- Update maxCount, the highest frequency we have seen for any character while expanding.
- If the window becomes invalid, shrink from the left by moving L and decreasing counts
  until the condition holds again.

We also track maxLen = max(maxLen, R-L+1).

A common question is: why don’t we recompute maxCount when we shrink?
maxCount might become stale, meaning it could be larger than the true maximum frequency
in the current window.
But a stale maxCount only makes the window appear more valid, which can delay shrinking.
It never causes us to miss the true maximum length.
This is a standard accepted pattern for this problem and keeps the runtime O(n).

Finally, since each pointer moves forward at most n times, the total runtime is O(n).

"""