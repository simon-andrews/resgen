# stuff for managing the "tmp" temporary directory

import os
import shutil

def reset():
    if os.path.exists('tmp'):
        shutil.rmtree('tmp')
    os.makedirs('tmp')
