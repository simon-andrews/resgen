import datetime
from jinja2 import Environment, FileSystemLoader
import json
import tmpdir
import os
import shutil

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
    def render_tex(self):
        return resume_template.render(data=self.data)
    def render_pdf(self):
        tmpdir.reset()
        with open('tmp/resume.tex', 'w') as f:
            f.write(self.render_tex())
        old_cwd = os.getcwd()
        os.chdir('tmp')
        os.system('pdflatex resume.tex')
        os.chdir(old_cwd)
        shutil.copyfile('tmp/resume.pdf', 'output/resume-' + str(datetime.datetime.now()) + '.pdf')

if __name__ == '__main__':
    r = ResumeManager('sample_data/resume.json')
    import pprint
    pprint.pprint(r.get_sections())
    #with open('/tmp/test/test.tex', 'w') as f:
    #    f.write(r.render_tex())
    r.render_pdf()
