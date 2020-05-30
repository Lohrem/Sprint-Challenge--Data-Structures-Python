from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        if self.capacity > self.storage.length: # check to make sure that the list is within capacity
            self.storage.add_to_tail(item) # go ahead and add the item to the end
        else:
            self.storage.remove_from_head()
            self.storage.add_to_tail(item)

    def get(self):
        theList = []
        for i in range(len(self.storage)):
            theList.append(self.current.value)
            self.current = self.current.next
        return theList