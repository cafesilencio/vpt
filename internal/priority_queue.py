import functools


class PriorityQueue:

    def __init__(self, comparator):
        self.comparator = comparator
        self.items = []

    def add(self, item):
        self.items.append(item)
        self.items.sort(key=functools.cmp_to_key(self.comparator), reverse=True)

    def poll(self):
        return None if len(self.items) == 0 else self.items.pop(0)

    def peek(self):
        return None if len(self.items) == 0 else self.items[0]

    def size(self):
        return len(self.items)
