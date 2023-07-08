class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class Merge:
    def merge_two_list(self, list1, list2):
        curr = ListNode()
        dummy = curr

        while list1 and list2:
            if list1.value < list2.value:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 if list1 else list2
        return dummy.next


# Example usage
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)
merge = Merge()
merged = merge.merge_two_list(list1, list2)
