from __future__ import print_function
from IPython.core.magic import Magics, magics_class, cell_magic, needs_local_scope
from program_parser import parse, add_to_json


@magics_class

class CSPMagic(Magics):
    @cell_magic
    @needs_local_scope
    def ITS(self, line, cell, local_ns):
        "ITS Cell Magic"
        try:
            name = local_ns['name']
            email = local_ns['email']
        except KeyError:
            return "Please define name and email variables at the top of your notebook, or rerun the cell with the name and email"
        id = line
        add_to_json(id, cell, name, email)
        o = parse(id, cell, debug=True)
        print(o)
        try: 
            exec(cell, globals(), local_ns)
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
