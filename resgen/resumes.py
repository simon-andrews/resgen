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

def intersection(list1, list2):
    ret = set()
    for i in list1:
        for j in list2:
            if i == j:
                ret.add(i)
    return ret

def get_n_bullets(bullets, n):
    ret = list()
    for i in range(n):
        for bullet in bullets:
            good = True
            for accepted_bullet in ret:
                if bullet['text'].startswith(accepted_bullet['text'][:3]):
                    good = False
                    break
            if good == True:
                ret.append(bullet)
                break
    return ret

def rank_resume(resume, things_to_look_for):
    assert type(resume) is dict
    def bullet_score(bullet):
        if 'tags' in bullet.keys():
            return -len(intersection(bullet['tags'], things_to_look_for))
        return 0
    for key in resume.keys():
        if type(resume[key]) is list:
            if key == 'entries':
                for entry in resume['entries']:
                    entry['bullets'].sort(key=bullet_score)
                    entry['bullets'] = get_n_bullets(entry['bullets'], 4)
        if type(resume[key]) is dict:
            rank_resume(resume[key], things_to_look_for)
    return resume


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
        output_filename = 'output/resume.pdf' #'output/resume-' + str(datetime.datetime.now()) + '.pdf'
        shutil.copyfile('tmp/resume.pdf', output_filename)
        return output_filename

if __name__ == '__main__':
    import pprint
    p = pprint.PrettyPrinter(width=200)
    r = ResumeManager('sample_data/resume.json')
    import listings
    import data
    l = listings.Listing(data.google_listing)
    things_to_look_for = l.get_skills()
    print('highlighting' + str(things_to_look_for))
    rank_resume(r.data, things_to_look_for)
    r.render_pdf()
    #print(intersection([2,3,4], [1,2,3]))
    #r = rank_resume(r.data, ['c++', 'python'])
    #p.pprint(r)
