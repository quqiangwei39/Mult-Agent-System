class Task:
    def __init__(self, description):
        self.description = description
        self.steps = []

    def add_step(self, step):
        self.steps.append(step)


class Step:
    def __init__(self, description):
        self.description = description
        self.result = None