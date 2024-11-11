class Node:

    def __init__(self, val: int, next):
        self.val = val
        self.next = next


if __name__ == "__main__":
    """
        node1(1) -> node2(2)
    """
    node1 = Node(1, None)
    node3 = Node(3, node1)
    node2 = Node(2, node3)
    node1.next = node2
    print(f" node 1 val: {node1.val}")
    print(f" node 2 val: {node1.next.val}")
    print(f" node 3 val: {node1.next.next.val}")
    print(f" node 1 val: {node1.next.next.next.val}")
