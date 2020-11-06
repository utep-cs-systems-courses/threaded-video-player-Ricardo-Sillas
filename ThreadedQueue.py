import threading

class ThreadedQueue:

    def __init__(self):
        self.q = []
        self.full = threading.Semaphore(0)
        self.empty = threading.Semaphore(10)
        self.lock = threading.Lock()

    def put(self, item):
        self.empty.acquire()
        self.lock.acquire()
        self.q.append(item)
        self.lock.release()
        self.full.release()

    def get(self):
        self.full.acquire()
        self.lock.acquire()
        val = self.q.pop(0)
        self.lock.release()
        self.empty.release()
        return val
