class ApiKey:

    def __init__(self, key):
        self.key:str = key

    def __str__(self):
        return self.key

    def __repr__(self):
        return str(self)