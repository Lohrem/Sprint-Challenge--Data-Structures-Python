class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.curr_pos = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
        else:
            if self.curr_pos == self.capacity:
                self.curr_pos = 0

    def get(self):
        return self.storage