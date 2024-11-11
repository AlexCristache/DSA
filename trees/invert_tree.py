class TreeNode:
    def __init__(self, val=0, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


def invert_tree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left


    invert_tree(root.left)
    invert_tree(root.right)

    return root

def print_tree(root):
    if root is None:
        return

    print(root.val)
    print_tree(root.left)
    print_tree(root.right)

if __name__ == "__main__":
    root = TreeNode(4)

    root.left = TreeNode(2)
    root.right = TreeNode(7)

    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("original")
    print_tree(root)

    invert_tree(root)

    print("inverted")
    print_tree(root)
