import skills
import tokenization

class Listing:
    def __init__(self, text):
        self.text = text
        self.tokens = tokenization.tokenize(self.text)
    def get_languages(self):
        if hasattr(self, 'languages'):
            return self.languages
        self.languages = set()
        for token in self.tokens:
            if skills.is_language(token):
                self.languages.add(token)
        return self.languages
