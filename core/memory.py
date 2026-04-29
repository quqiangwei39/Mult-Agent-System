class Memory:

    def __init__(self):
        self.short_term = []
        self.long_term = {}

    def save_short(self, data):
        self.short_term.append(data)

    def save_long(self, key, value):
        self.long_term[key] = value

    def get_context(self):
        return {
            "short": self.short_term,
            "long": self.long_term
        }