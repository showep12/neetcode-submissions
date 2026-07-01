#encode A to B

#Understand / Exmaple
"""
In encode function... We concatenate each string element in the List into one large string
#["act","eat"] -> "acteat" encoding 

In decode function... We decode the long input string into the original List[string]
which was input parameter value of encode function.. 
"""

#Input / Output / EdgeCase
"""
[Encode]
Input : there could be not only character or string... but also # , . all valid ASCII characters
could be in the element of Input List 
Hell#o  / app,le / 'chicken '

Output : 'Hell#oapp,lechicken '
1) can we manipulate or modify output string??? not only using the original each strings...
but also adding some delimeter.. or other things to help decode?? yest
-> input: apple banana ->  output apple#banana

[decode]
Input : encoded string in encode function (apple#banana d
Output : List[str] exactly same as input value of encode function

In worst case... total size of characters can be 20000 (100x200)
"""

#Simple bruteforce approach
"""
we concatenate all the strings using delimiter just like # or , or otherthings..
but here is a problem... what if each string itself contain the delimiter as a part of string??
For example... if we use ' ' as delimiter... and some string is 'hello world'....
if we decode... it will be considered as seperate string likt ['hello', 'world']


so we can not just use this approach... we have to think of other delimiter avoiding such cases..
"""

#Optimization
"""
How about attaching length of each string's size before each string??
like 5hello 4list?? -> If we meet some number?? we can get the next characters
calculating the number.. 
for example 48abceddddd... -> we iterate 48 characters after 48....

but ther is still some problem... what if the string contains number????
4abc -> 44abc the decoder will iterate 44 characters not 4 characters..

So we have to add another delimiter... how about #??? 

4#4abc 3#car.....
if we encode like this... we know that the first character would definitely be number character..
even if first string is empty... just like ['','car']
-> we make it as 0#3#car.... 
-> we can assume that the first character of the encoded string is always number character...
4#4abc 3#car..... -> ['4abc', 'car']

O(n*m) time / space
n is the maximum length of List
m is the maximum length of string in the List elements..

"""




#okay now is the time to implement
class Solution:

    

    def encode(self, strs: List[str]) -> str:
        # We iterate through the list of strings.
        # For each string:
        # 1. Calculate the length of the string.
        # 2. Convert the length to a string.
        # 3. Add a delimiter, such as "#", after the length.
        # 4. Append the original string after the delimiter.
        # 5. Add this encoded part to the final encoded string.

        encoded = ""
        for string in strs : 
            delimiter = str(len(string)) + "#"

            encoded += (delimiter +  string)
        # print(encoded)
        return encoded

        # [""] -> 0#
        # ["4abc"] ->4#4abc
 


    def decode(self, s: str) -> List[str]:

        #iterate the string
        #check the start and end point of number
        #   go through each character until we meet '#'
        #   check the number string from start point to the endpoint before #
        #   it indicates the length of string comes after the '#'
        #      Read the number before `#` as the length.
        #      Then read the next `length` characters after `#`.
        #      Add that substring to the result list.
        #   move the start pointer after the end of the string

        #iterate until we meet end of the string ()
        start = 0
        result = []
        #what if the last string is 0#??
        while start < len(s) : 
            curr = start 
            
            while s[curr] != '#' : 
                curr += 1

            #if we meet #... get the length
            length = int(s[start:curr])
            start_string = curr + 1 #after the #
            end_string = start_string + length - 1
            string = s[start_string:end_string+1] #the last index is not included

            result.append(string)
            start = end_string + 1


        return result
            
            
            
            


        return 
