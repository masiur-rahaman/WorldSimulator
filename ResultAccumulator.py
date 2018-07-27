import Queue


class ResultAccumulator:

    def __init__(self):
        self._activities = Queue.Queue()

    def add(self, message):
        self._activities.put(message)

    def get(self):
        return self._activities.get()
