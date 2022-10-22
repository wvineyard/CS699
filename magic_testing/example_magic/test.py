from __future__ import print_function
from IPython.core.magic import (Magics, magics_class, line_cell_magic, line_magic, cell_magic)

@magics_class
class MyMagics(Magics):
    @line_magic
    def lmagic(self, line):
        "my line magic"
        print("Full access to the main IPython object:", self.shell)
        print("Variables in the user namespace:", list(self.shell.user_ns.keys()))
        return line

    @cell_magic
    def cmagic(self, line, cell):
        "my cell magic"
        return exec(cell)

    @line_cell_magic
    def lcmagic(self, line, cell=None):
        "Magic that works both as %lcmagic and as %%lcmagic"
        if cell is None:
            print("Called as line magic")
            return line
        else:
            print("Called as cell magic")
            return line, cell
        

def load_ipython_extension(ipython): 
    ipython.register_magics(MyMagics)
