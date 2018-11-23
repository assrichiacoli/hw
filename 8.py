
class QueueNode(object):
    def __init__(self, elem, nextnode):
        self.value = elem
        self.next = nextnode


class QueueIterator(object):
    def __init__(self, node, count):
        self.out = node
        self.count = count

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        else:
            out = self.out.value
            self.out = self.out.next
            self.count -= 1
            return out
