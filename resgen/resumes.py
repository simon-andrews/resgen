import json

class ResumeManager:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            text = f.read()
            self.data = json.loads(text)
    def get_sections(self):
        return list(self.data['sections'].keys())

if __name__ == '__main__':
    r = ResumeManager('sample_data/resume.json')
    import pprint
    pprint.pprint(r.get_sections())
