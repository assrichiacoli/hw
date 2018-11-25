
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
 
