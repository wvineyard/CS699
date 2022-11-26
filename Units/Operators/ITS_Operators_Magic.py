from __future__ import print_function
from IPython.core.magic import Magics, magics_class, cell_magic
from program_parser import parse, add_to_json


@magics_class
class CSPMagic(Magics):
    @cell_magic
    def ITS(self, line, cell):
        "ITS Cell Magic"
        id = line
        add_to_json(id, cell)
        o = parse(id, cell, debug=True)
        print(o)
        try: 
            exec(cell)
        except Exception as e:
            return None

    @cell_magic
    def wow(self, line, cell):
        print(self)
        print(line)
        print(cell)
        return self


def load_ipython_extension(ipython):
    ipython.register_magics(CSPMagic)


def reload_ipython_extension(ipython):
    ipython.register_magics(CSPMagic)
