class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.curr_pos = 0

    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.append(item)
            self.curr_pos += 1
        else:
            if self.curr_pos == self.capacity:
                self.curr_pos = 0
                self.storage[self.curr_pos] = item

    def get(self):
        return self.storage