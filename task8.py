
class QueueNode:
    """ Node: Class for single node of LinkedQueue """

    def __init__(self, elem, nextnode):
        """ Initializes new node """
        self.elem = elem
        self.next = nextnode


class QueueIterator:
    """ QueueIterator: Iterator for LinkedQueue """

    def __init__(self, node, lengthgth):
        """ Initializes new Iterator """
        self.node = node
        self.length = lengthgth

    def __next__(self):
        """ Returns next element of queue: next(iter) """
        if self.length == 0:
            raise StopIteration
        else:
            out = self.node.elem
            self.node = self.node.next
            self.length -= 1
            return out


class LinkedQueue:
    """ LinkedQueue """

    def __init__(self):
        """ Initializes new queue """
        self.rear = None
        self.frontelem = None
        self.length = 0

    def push(self, elem):
        """ Pushes 'elem' to queue """
        if not self.length:
            self.rear = QueueNode(elem, None)
            self.frontelem = self.rear
            self.length = 1
        else:
            new_node = QueueNode(elem, None)
            self.rear.next = new_node
            self.rear = new_node
            self.length += 1
    
    def pop(self):
        """ Removes front of queue and returns it """
        out = self.frontelem.elem
        self.frontelem = self.frontelem.next
        self.length -= 1
        return out

    def front(self):
        """ Returns front of queue """
        return self.frontelem.elem

    def empty(self):
        """ Checks whether queue is empty """
        if self.length == 0:
            return True
        else:
            return False

    def __iter__(self):
        """ Returns Iterator for queue: iter(queue) """
        return QueueIterator(self.frontelem, self.length)

    def __len__(self):
        """ Returns size of queue: length(queue) """
        return self.length

    def clear(self):
        """ Makes queue empty """
        self.rear = None
        self.frontelem = None
        self.length = 0
 
