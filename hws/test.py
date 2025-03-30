# add two linked lists

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

l1 = create_linked_list([2, 4, 3])
l2 = create_linked_list([5, 6, 4])


def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    carry = 0
    dummy = ListNode(0)
    current = dummy
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        sum = val1 + val2 + carry
        carry = sum // 10
        current.next = ListNode(sum % 10)
        current = current.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next
    
l3 = addTwoNumbers(l1, l2)
print("l3:")
while l3:
    print(l3.val)
    l3 = l3.next