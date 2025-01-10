import functools


class PriorityQueue:

    def __init__(self, comparator):
        self.comparator = comparator
        self.items = []

    def add(self, item):
        self.items.append(item)
        # todo reverse=true???
        self.items.sort(key=functools.cmp_to_key(self.comparator), reverse=True)

    def poll(self):
        if len(self.items) == 0:
            return None
        else:
            item_to_return = self.items[0]
            self.items.remove(item_to_return)
            return item_to_return

