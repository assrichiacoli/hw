
class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.elem = elem
        self.next = nextnode


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
        self.rear = None
        self.front = None
        self.len = 0

    def push(self, elem):
        """ Pushes 'elem' to queue """
        if self.len:
            new_node = QueueNode(elem, None)
            self.rear.next = new_node
            self.rear = new_node
            self.len += 1
        else:
            self.rear = QueueNode(elem, None)
            self.front = self.rear
            self.len = 1
    
    def pop(self):
        """ Removes front of queue and returns it """
        out = self.front.elem
        self.front = self.front.next
        self.len -= 1
        return out

    def front(self):
        """ Returns front of queue """
        return self.front.value

    def empty(self):
        """ Checks whether queue is empty """
        if self.len == 0:
            return True
        else:
            return False

    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.front, self.len)

    def __len__(self):
        """ Returns size of queue: len(queue) """
        return self.len

    def clear(self):
        """ Makes queue empty """
        self.rear = None
        self.front = None
        self.len = 0
 
