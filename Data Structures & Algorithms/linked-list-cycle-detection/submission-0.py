# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #hashMap

        #hashSet
        seen_set = set()
        # seen_set.add(head)

        node = head
        while node : 
            curr_len = len(seen_set)
            seen_set.add(node)
            next_len = len(seen_set)

            if curr_len == next_len : 
                return True
            node = node.next
        
        return False


        # print(seen_set, len(seen_set))
        # return False