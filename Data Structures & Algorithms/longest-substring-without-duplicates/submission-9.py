class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Problem:
        Return the length of the longest substring (contiguous) with no repeating characters.

        Technique:
        Variable-size sliding window + hash map (last seen index).

        Why not brute force?
        - Brute force can be O(n^2) because you might re-scan many characters repeatedly.

        Core invariant we maintain:
        - The current window s[L..R] contains no duplicates.
        - L never moves backward; it only increases.
        """

        # last_seen[ch] = the most recent index where character ch appeared
        last_seen: Dict[str, int] = {}

        # L = left boundary of our current "unique characters" window
        L = 0

        # maxLen = best (maximum) length found so far
        maxLen = 0

        # R = right boundary, we expand the window by moving R forward
        for R, ch in enumerate(s):

            # If we've seen this character before, it might cause a duplicate.
            # Let prev be its last seen index.
            if ch in last_seen:
                prev = last_seen[ch]

                # If prev is inside our current window (prev >= L),
                # then ch duplicates an existing character in s[L..R].
                #
                # To remove the duplicate, we must move L to prev + 1,
                # so the old occurrence is excluded from the window.
                #
                # Critical rule:
                # L must NEVER move backward.
                # Example: "abba"
                # - When we see the last 'a', its prev index is 0,
                #   but L might already be 2. We must keep L at 2, not move it back to 1.
                L = max(L, prev + 1)

            # Update the last seen index of this character to the current index R.
            # This must happen AFTER the L update, because R is the newest occurrence.
            last_seen[ch] = R

            # Now the window s[L..R] is guaranteed to have no duplicates.
            # Update the answer with the current window length.
            window_len = R - L + 1
            maxLen = max(maxLen, window_len)

        return maxLen




"""
[0. Problem Restatement]
Given a string s, return the length of the longest substring that contains no repeating characters.
A substring must be contiguous.

[1. Why brute force is too slow]
Brute force would try every start index and expand until a repeat occurs.
That can take O(n^2) time in the worst case.

[2. Key insight]
We only care about contiguous windows with unique characters.
We can maintain a sliding window [L..R] that is always valid (no duplicates).
When a duplicate appears, we move L forward to remove the duplicate.

[3. Data structure choice]
We need to know where we last saw each character to jump L efficiently.
Use a hash map: last_seen[char] = most recent index of that char.

[4. Invariant]
Invariant 1: The current window s[L..R] contains no repeated characters.
Invariant 2: L never moves backward; it only moves forward.
Invariant 3: last_seen always stores the latest position of each character seen so far.

[5. Update rule (the critical line)]
When we see character ch at position R:
- If ch was previously seen at index prev:
  - If prev is inside the current window (prev >= L),
    then we must move L to prev + 1.
  - To prevent moving L backward, we do:
    L = max(L, prev + 1)

[6. Answer update]
After updating L and last_seen, the window is valid again.
Update the maximum length using:
maxLen = max(maxLen, R - L + 1)

[7. Complexity]
Each index R moves forward once.
L also moves forward at most n times total.
Thus total time is O(n), and space is O(min(n, alphabet_size)).









Today we’ll solve “Longest Substring Without Repeating Characters.”
We’re given a string s, and we need the maximum length of a contiguous substring with all unique characters.

First, why not brute force?
If we try every start index and expand to the right until we hit a repeated character, that can take O(n^2) time, especially for strings like “abcdef…”.

The key observation is that we’re looking for a contiguous window with no duplicates.
That suggests a sliding window with two pointers:
L is the left boundary, R is the right boundary.
We will maintain an invariant: the substring s[L..R] always has no repeating characters.

To do that efficiently, we need to quickly handle duplicates.
A set can tell us if a character exists, but it doesn’t tell us where it was.
To jump L directly, we store the most recent index of each character in a hash map:
last_seen[ch] = the latest position of ch.

Now, at each step R, we read character ch = s[R].
If ch has appeared before at index prev = last_seen[ch], there are two cases:
Case 1: prev is outside the current window, meaning prev < L.
Then it does not matter; our current window still has no duplicates, so we do nothing to L.
Case 2: prev is inside the current window, prev >= L.
Then ch would be duplicated in s[L..R], so we must move L to prev + 1 to exclude that older occurrence.

The critical part is: L must never move backward.
So we write:
L = max(L, prev + 1)
This single max fixes tricky cases like “abba.”

After adjusting L, we update last_seen[ch] = R.
Now the window is valid again.
We update the answer using the window length R - L + 1.

For complexity, each character index enters the window once as R increases.
And each index is removed at most once as L increases.
So both pointers move forward at most n steps, giving O(n) time.

That’s the full solution: a variable-size sliding window with a last-seen index map.

"""