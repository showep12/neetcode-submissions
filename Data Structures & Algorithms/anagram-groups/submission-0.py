class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # For each string, compute its anagram key by sorting the characters.
        # Strings that are anagrams will produce the same sorted key.
        # Use this key as a hash map key and store all corresponding strings together.
        # After processing all strings, the values of the hash map form the grouped anagrams.

        dicAnagram = dict()

        for string in strs : #takes O(n)
            
            sortStr = "".join(sorted(string)) #empty string dot join of sorted string
            #dicAnagram[sortStr].append(string)
            if (not dicAnagram.get(sortStr)) : 
                dicAnagram[sortStr] = [string]
            else :
                dicAnagram[sortStr].append(string)
        answer = []
        for key in dicAnagram.keys() : 
            answer.append(dicAnagram[key])


        print(dicAnagram)
        print(answer)
        return answer

        


# ============================================================
# Problem-Solving Checklist (LeetCode Template)
# ============================================================
# 0) Restate the problem (1 sentence):
# - Input: List of String
# - Output: Return a list of lists where each sublist groups anagrams.
# - Return exactly: Return a list of lists where each sublist groups anagrams.
#
# 1) Constraints & target complexity:
# - N (max size): 
# - Value range: 1
# - Target time: O(m)
# - Target space: O(m)
#
# 2) Clarify assumptions (if needed):
# - Duplicates? (yes/no)
# - Sorted input? (yes/no)
# - Always valid input? (yes/no)
# - 1-indexed or 0-indexed?
#
# 3) Example sanity check (quick mental run):
# - Example input:
# - Expected output:
# - Why:
#
# 4) Brute force baseline:
# - Idea:
# - Time:
# - Space:
# - Why it’s too slow:
#
# 5) Pattern selection:
# - Pattern: (Two Pointers / Sliding Window / DFS / BFS / Binary Search / DP / Heap / Stack / Union-Find / ...)
# - Why this pattern fits:
#
# 6) Core idea (the "aha" in 1–2 sentences):
# - Idea:
#
# 7) Invariant / state (what I maintain):
# - Invariant / state definition:
#
# 8) Data structures used:
# - e.g., hash map, set, deque, heap, stack
#
# 9) Algorithm steps (high level):
# 1)
# 2)
# 3)
#
# 10) Edge cases (max 3):
# - Empty / size 1:
# - Duplicates / all equal:
# - Extreme / skewed / None children / disconnected:
#
# 11) Dry run (5–10 steps):
# - Track the key variables:
#
# 12) Complexity:
# - Time: O(...) because ...
# - Space: O(...) because ...
#
# 13) Common bugs to watch:
# - Off-by-one (boundaries, mid update)
# - None checks (node.left is None, etc.)
# - Visited marking timing (BFS/DFS)
# - Wrong base case / missing return
# - Mutating shared list without backtracking
#
# ============================================================

