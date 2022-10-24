from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_cell_magic, line_magic, cell_magic)
import json
import time
from os.path import exists
@magics_class
class CSPMagic(Magics):
    @cell_magic
    def cmagic(self, line, cell):
        "ITS Cell Magic"
        add_to_json(cell)
        return exec(cell)

def load_ipython_extension(ipython): 
    ipython.register_magics(CSPMagic)


def add_to_json(input):
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    # check to see if data.json exists
    if not exists("./data.json"):
        data = {}
        data[current_time] = input
        json_out = json.dumps(data, indent=4)
        with open("data.json", "w") as outfile:
            outfile.write(json_out)
    else:
        with open('data.json', 'r+') as outfile: 
            file_data = json.load(outfile)
            file_data[current_time] = input
            outfile.seek(0)
            json.dump(file_data, outfile, indent=4)
        