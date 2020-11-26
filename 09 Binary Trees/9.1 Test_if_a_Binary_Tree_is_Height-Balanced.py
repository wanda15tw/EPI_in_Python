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

# Function to print tree nodes in inorder fashion
def inOrder(root):
    if root != None:
        inOrder(root.left)
        print(root.data, end=' ')
        inOrder(root.right)

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

def is_balanced_binary_tree(tree):
    import collections
    BalancedStatusWithHeight = collections.namedtuple('BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        if not tree:
            return BalancedStatusWithHeight(True, -1) # base case

        left_result = check_balanced(tree.left) # recursion for left child
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right) # recursion for right child
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree.balanced)


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    n = len(arr)
    root = None
    root = insertFromList(arr, root, 0, n)
    # inOrder(root)

    # tree_traversal(root)
    tree_traversal_type(root, "Preorder")
    tree_traversal_type(root, "Inorder")
    tree_traversal_type(root, "Postorder")