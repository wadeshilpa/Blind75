# Easy 
# Merge Two Sorted Lists
# Singly linked list - Two-pointer merge

# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.

# list1 = [1,2,4], list2 = [1,3,4]                   Output: [1,1,2,3,4,4]
# list1 = [], list2 = []                             Output: []
# list1 = [], list2 = [0]                            Output: [0]
# list1 = [], list2 = []                                    Output = []
# list1 = [], list2 = [1,2,3]                               Output = [1,2,3]

# Edge cases        : either or both blank, negative numbers, equal/duplicate elements
# Time Complexity   : 
# Space complexity  : 
# Best case         : 
# Worst Case        : 
########################################################################
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(init, l1:ListNode, l2:ListNode)->ListNode:
        head = ListNode()
        dummy = head
        
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 = l2.next
            head = head.next

        if l1:
            head.next = l1 
        elif l2:
            head.next = l2 

        return dummy.next
    
    def printLL(self, head):
        while head:
            print(head.val, end="->")
            head = head.next
        print()
    
if __name__ == '__main__':
    l1 = ListNode(1, ListNode(3, ListNode(8)))
    l2 = ListNode(2, ListNode(3, ListNode(9, ListNode(100))))
    Solution().printLL(l1)
    Solution().printLL(l2)
    result = Solution().mergeTwoLists(l1, l2)
    Solution().printLL(result)




