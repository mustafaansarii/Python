from collections import deque

class q:
    def __init__(self):
        self.queue=deque()
        print(type(self.queue))
        print(self.queue.append(12))
        print(list(self.queue))

qu=q()
