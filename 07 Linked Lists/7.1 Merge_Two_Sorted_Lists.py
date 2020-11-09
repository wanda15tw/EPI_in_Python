class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def search_list(L, key):
    while L and L.data != key:
        L = L.next


def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node

def delete_after(node):
    node.next = node.next.next

def merge_two_sorted_lists(L1, L2):
    # create a placeholder for the result
    dummy_head = tail = ListNode()

    # traverse L1, L2 and choose the node has smaller key to continue
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L1.next
        else:
            tail.next, L2 = L2, L2.next
        tail = tail.next

    # Append the remaining nodes of L1 or L2
    tail.next = L1 or L2
    return dummy_head

# create ListNodes L1, L2
L1_data = [2, 5, 7]
L2_data = [3, 11]
L1 = L1_tail = L1_head = ListNode(L1_data[0])
L2 = L2_tail = L2_head = ListNode(L2_data[0])

for x in L1_data[1:]:
    L1_tail.next = ListNode(x) # Create and add another node
    L1_tail = L1_tail.next # Move the tail pointer

for x in L2_data[1:]:
    L2_tail.next = ListNode(x) # Create and add another node
    L2_tail = L2_tail.next # Move the tail pointer


# merge L1 & L2 and print resulted ListNode
tail = merge_two_sorted_lists(L1, L2)

while tail:
    print(tail.data)
    tail = tail.next