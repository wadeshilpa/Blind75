# Easy 
# Merge Two Sorted Lists

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
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_linked_list(nums):
    dummy = curr =  ListNode()
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def mergeTwoLists(self, list1:ListNode, list2:ListNode)-> ListNode:
        dummy = result = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                result.next = list1
                list1 = list1.next
            else:
                result.next = list2
                list2 = list2.next
            result = result.next
        if list1:
            result.next = list1
        else:
            result.next = list2
        return dummy.next

if __name__ == "__main__":
    raw1 = input("Enter list1 = ").strip()
    raw2 = input("Enter list2 = ").strip()

    list1 = list(map(int, raw1.split(","))) if raw1 else []
    list2 = list(map(int, raw2.split(","))) if raw2 else []
   
    l1 = to_linked_list(list1)
    l2 = to_linked_list(list2)

    result_head = Solution().mergeTwoLists(l1, l2)
    print("merged list: ", to_list(result_head))
