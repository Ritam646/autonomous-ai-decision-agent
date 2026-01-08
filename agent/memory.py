class Memory:
    def __init__(self):
        self.history = []

    def store(self, data):
        self.history.append(data)

    def retrieve(self):
        return self.history
