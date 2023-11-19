class Topic:
    def __init__(self, *args):
        self.topic = [item for item in args]

    def __len__(self):
        return len(self.topic)
