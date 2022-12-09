# Given the head pointers of two linked lists 
# where each linked list represents an integer 
# number (each node is a digit), 
# add them and return the resulting linked list. 
# Here, the first node in a list 
# represents the least significant digit.

# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None

def addTwoLists(self, first, second):
    prev = None
    temp = None
    carry = 0
    while first is not None or second is not None:
        if first is None:
            firstData = 0
        else:
            firstData = first.data
        if second is None:
            secondData = 0
        else:
            secondData = second.data
        Sum = carry
        Sum += firstData
        Sum += secondData
        if Sum >= 10:
            carry = 1
        else:
            carry = 0
        Sum %= 10
        temp = Node(Sum)
        if self.head is None:
            self.head = temp
        else:
            prev.next = temp
        prev = temp
        if first is not None:
            first = first.next
        if second is not None:
            second = second.next
    if carry > 0:
        temp.next = Node(carry)