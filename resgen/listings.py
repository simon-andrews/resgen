import tokenization

class Listing:
    def __init__(self, text):
        self.text = text
        self.tokens = tokenization.tokenize(self.text)
