import skills
import tokenization

class Listing:
    def __init__(self, text):
        self.text = text
        self.tokens = tokenization.tokenize(self.text)
        self.languages = set()
        self.frameworks_and_tools = set()
    # TODO: handle multi-word skills
    def _update_skill(self, predicate, skill_set):
        for token in self.tokens:
            if predicate(token):
                skill_set.add(token)
    def get_languages(self):
        _update_skill(skills.is_language, self.languages)
        return self.languages
    def get_frameworks_and_tools(self):
        _update_skill(skills.is_framework_or_tool, self.frameworks_and_tools)
        return self.frameworks_and_tools
