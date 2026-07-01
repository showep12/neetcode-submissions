# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #0 -> 1 -> 2 -> 3 -> None
        #None <- 0 <- 1 <- 2 <- 3
        #None

        #The end of linked list is None
        #The Node(0) have to point out the last node None
        #The Node(1) have to point out the Node(0)
        #The Node(2) have to point out the Node(1)
        #The Node(3) have to point out the Node(2)
        #The Next node is None nothing to reverse


        #Curr Linked List
        #0 -> 1 -> 2 -> 3 -> None
        #Reversed Linked List
        #None

        #Curr Linked List
        #    1 -> 2 -> 3 -> None
        #Reversed Linked List
        #0 -> None

        #Curr Linked List
        #    1 -> 2 -> 3 -> None
        #Reversed Linked List
        #0 -> None

        # Take the current first node of the remaining list, 
        # and attach it to the front of the reversed list.

        #take current node
        #save the next node in the current linked list to proceed next step
        #set prev as the next node in th reversed linked list
        #move to the next node in the current linked list

        reverse_head = None
        curr = head
        while curr is not None : 
            curr_next = curr.next #1 2 
            curr.next = reverse_head #0-> None
            reverse_head = curr #0
            curr = curr_next #1 
        
        #
        # prev = None
        # curr = head

        # while curr:
        #     next_node = curr.next
        #     curr.next = prev
        #     prev = curr
        #     curr = next_node

        # return prev



        return reverse_head

