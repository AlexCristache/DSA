from typing import Optional
from common import TreeNode


def search(root: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return None
    else:
        return root.right


if __name__ == "__main__":
    node1 = TreeNode(None, None, 1)
    node2 = TreeNode(None, None, 2)
    root = TreeNode(node1, node2, 0)

    res = search(root)
    print(res.val)
