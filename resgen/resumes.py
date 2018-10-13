from jinja2 import Environment, FileSystemLoader
import json

env = Environment(
    loader=FileSystemLoader('templates/resume'),

    block_start_string='(@', # replaces {%
    block_end_string='@)', # replaces %}
    variable_start_string='((', # replaces {{
    variable_end_string='))', # replaces }}
)
resume_template = env.get_template('resume.tex')

class ResumeManager:
    def __init__(self, json_path):
        with open(json_path, 'r') as f:
            text = f.read()
            self.data = json.loads(text)
    def get_sections(self):
        return list(self.data['sections'].keys())
    def render(self):
        return resume_template.render(data=self.data)

if __name__ == '__main__':
    r = ResumeManager('sample_data/resume.json')
    import pprint
    pprint.pprint(r.get_sections())
    with open('/tmp/test/test.tex', 'w') as f:
        f.write(r.render())
