
class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.elem = elem
        self.nextnode = nextnode


class QueueIterator:
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, emptynode):
        """ Initializes new Iterator """
        self.node = node
        self.emptynode = emptynode

    def __next__(self):
        """ Returns next element of queue: next(iter) """
        if self.emptynode == 0:
            raise StopIteration
        else:
            nextnode = self.node.elem
            self.node = self.node.nextnode
            self.emptynode -= 1
            return nextnode


class LinkedQueue:
    """ LinkedQueue """

    def __init__(self):
        """ Initializes new queue """
        self.enter = None
        self.out = None
        self.count = 0

    def push(self, elem):
        """ Pushes 'elem' to queue """
        if self.count:
            new_node = QueueNode(elem, None)
            self.enter.next = new_node
            self.enter = new_node
            self.count += 1
        else:
            self.enter = QueueNode(elem, None)
            self.out = self.enter
            self.count = 1
    def pop(self):
        """ Removes front of queue and returns it """
        out = self.out.value
        self.out = self.out.next
        self.count -= 1
        return out

    def front(self):
        """ Returns front of queue """
        return self.out.value

    def empty(self):
        """ Checks whether queue is empty """
        if self.count == 0:
            return True
        else:
            return False

    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.out, self.count)

    def __len__(self):
        """ Returns size of queue: len(queue) """
        return self.count

    def clear(self):
        """ Makes queue empty """
        self.enter = None
        self.out = None
        self.count = 0
 
