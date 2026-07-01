class Solution:

    def encode(self, strs: List[str]) -> str:
    #So it concatenates each string into one long string.
        total_encoded = ""
        for string in strs : 
            encoded = str(len(string)) + '#' + string
            total_encoded += encoded
            # print(total_encoded)
        
        return total_encoded
        #remember each 
        #0:hello -> 6##hello5#world ..... 
        #1:1world ->10
        #2:2day
        #3:4qwrt
        #4:

        0#1#h


    def decode(self, s: str) -> List[str]:

        start = 0
        end = len(s)
        result = []
        while start < end : 
            num_start = start
            num_end = start            

            while s[num_end] != '#' : 
                num_end += 1
            str_length = int(s[num_start:num_end])
            # num_end is actually the index of '#' character so we should not include this idnex in the converting
            str_start = num_end +1 # 5#
            str_end = str_start + str_length - 1 #0 + 3    5 6 7 (8 - 1)
            result.append(s[str_start:str_end+1])

            start = str_end + 1
            # print(start, result)
        return result
        
        #if we meet 0.... for the first time??? 
    #We have to decode it
    
