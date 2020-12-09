class Node:

    def __init__ (self, data):

        self.left = None
        self.right = None
        self.data = data


    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def insert(self, data, left=True):
        if left:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)

# Function to insert nodes in level order
def insertFromList(arr, root, i, n):
    """
    :param arr:
    :param root:
    :param i: current level
    :param n: tree depth
    :return: root
    """
    # base case for recursion
    if i < n:
        temp = Node(arr[i])
        root = temp

        # insert left child
        root.left = insertFromList(arr, root.left, 2 * i + 1, n)

        # insert right child
        root.right = insertFromList(arr, root.right, 2 * i + 2, n)

    return root

def tree_traversal(root):
    if root:
        # Preorder: Processes the root before the traversals of left and right child
        print("Preorder:", root.data)
        tree_traversal(root.left)

        # Inorder: Processes the root after the traversals of left child and before the traversal of right child
        print("Inorder", root.data)
        tree_traversal(root.right)

        # Postorder: Processes the root after the traversals of left and right children
        print("Postorder", root.data)

def tree_traversal_type(root, traversal_type):
    if root:
        if traversal_type == "Preorder":
            print(root.data) # root first
            tree_traversal_type(root.left, traversal_type) # left next
            tree_traversal_type(root.right, traversal_type) # right final
        elif traversal_type == "Inorder":
            tree_traversal_type(root.left, traversal_type) # left first
            print(root.data) # root next
            tree_traversal_type(root.right, traversal_type) # right final
        elif traversal_type == "Postorder":
            tree_traversal_type(root.left, traversal_type) # left first
            tree_traversal_type(root.right, traversal_type) # right next
            print(root.data) # root final

def is_BT(tree, low_range=float('-inf'), high_range=float('inf')):
    if not tree:
        return True
    elif not low_range <= tree.data <= high_range:
        return False
    return (is_BT(tree.left, low_range, tree.data) and \
            is_BT(tree.right, tree.data, high_range))

def is_BT_BST(tree):
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))

    bfs_queue = collections.deque([QueueEntry(tree, float('-inf'), float('inf'))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [\
                QueueEntry(front.node.left, front.lower, front.node.data),
                QueueEntry(front.node.right, front.node.data, front.upper)
            ]
    return True

if __name__ == "__main__":
    tree = insertFromList([1, 2, 3, 4, 5, 6, 7], None, 0, 7)
