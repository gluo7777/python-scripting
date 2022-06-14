# merge two sorted linked list
# numbers
# lengths can be different
# no cycles
# no null value
# non-decreasing order
# has duplicates
# range -100 to 100
# return new head of merged list

from typing import Optional

class ListNode:
    def __init__(self,val: int) -> None:
        self.val = val
        self.next = None
    
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    list3 = prev = None

    while list1 and list2:
        if list1.val <= list2.val:
            temp = list1
            list1 = list1.next
        else:
            temp = list2
            list2 = list2.next
        if not prev:
            prev = temp
            list3 = prev
        else:
            prev.next = temp
            prev = temp
    
    temp = list1 if list1 else list2
    while temp:
        if not prev:
            prev = temp
            list3 = prev
        else:
            prev.next = temp
            prev = temp
        temp = temp.next

    return list3

