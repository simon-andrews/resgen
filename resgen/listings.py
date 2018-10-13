import data
import skills
import tokenization

class Listing:
    def __init__(self, text):
        self.text = text
        self.tokens = tokenization.tokenize(self.text)
        self.languages = set()
        self.frameworks_and_tools = set()
    # TODO: handle multi-word skills
    def _update_skill(self, skill_structure, skill_set):
        detected_skills = skills.find_skills(self.tokens, skill_structure)
        for skill in detected_skills:
            skill_set.add(skill)
    def get_languages(self):
        self._update_skill(data.languages, self.languages)
        return self.languages
    def get_frameworks_and_tools(self):
        self._update_skill(data.frameworks_and_tools, self.frameworks_and_tools)
        return self.frameworks_and_tools
