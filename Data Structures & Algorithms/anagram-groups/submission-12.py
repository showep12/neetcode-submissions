class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 

        #DS - hashmap O(1)
        #becuase we will directly access the data by key not finding value
        #
        anagram_group = {}

        for string in strs : 
            sorted_str = ''.join(sorted(string))

            if sorted_str not in anagram_group : 
                anagram_group[sorted_str] = [] #initialize new list
            
            anagram_group[sorted_str].append(string)
        
        anagram_list = []
        for key, value in anagram_group.items() : 
            anagram_list.append(value)
        
        return anagram_list



# 1. Restate the problem - small example
# 2. Clarify the input and output
# 3. Ask about edge cases
# 4. Build a small example
# 5. Start with brute force
# 6. Find the bottleneck
# 7. Choose a pattern
# 8. Explain the optimized approach
# 9. Code carefully
# 10. Dry run
# 11. Check edge cases
# 12. State time and space complexity

# 1. Restate the problem - small example
#- Okay I will figure out the problem first, let me briefly state the problem
#  and make some simple example.
# So, two strings are anagrams if they have the same character counts, right?
# If I make some exa
# act and cat are anagrams because they have same character counts
# one 'a', one 'c, and one 't right?  
# at that time we group these two strings into the same sublist...like [["act", "cat"]]

#So the question asks me to group all strings by character counts..

# 2. Clarify the input and output
#Before we approach.. I think we have to clarify the input and output
#So input is the array of strings... right?? So it is 1D list consists of strings...
#the output is a 2D list where each element is a sublist grouped by anagram
#the max e


# 3. Ask about edge cases


# 1. Restate the problem - small example
# 2. Clarify the input and output
# 3. Ask about edge cases
# 4. Build a small example
# 5. Start with brute force
# 6. Find the bottleneck
# 7. Choose a pattern
# 8. Explain the optimized approach
# 9. Code carefully
# 10. Dry run
# 11. Check edge cases
# 12. State time and space complexity