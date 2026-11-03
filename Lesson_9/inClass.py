class NameManager:
    greeters = []

    def __init__(self):
        self.name = []

    def add_names(self, names):
        self.name.extend(names)

    @classmethod
    def add_greeter(cls, name):
        cls.greeters.append(name)

    @staticmethod
    def welcom_message():
        return "Welcome to the program"

name = NameManager()
name.add_greeter("Andy")
name.add_names("Sarah")