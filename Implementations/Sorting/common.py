class Element:
    """
    Class describing an element in a priority queue.
    """
    def __init__(self, value: int, key: int):
        """
        Instantiates a new element to be used inside a priority queue.
        :param value:
        :param key:
        """
        self.value: int = value
        self.key: int = key

    def set_value(self, value: int):
        self.value = value

    def set_key(self, key: int):
        self.key = key

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key
