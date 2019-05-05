import sys
import os
from cx_Freeze import setup, Executable
import numpy

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
dir_path = os.path.dirname(os.path.realpath(__file__))

sys.argv.append("build")  # replaces commandline arg 'build'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "Text genetic",
    version = "1.0",
    description = "Tkinter to exe",
    options = {"build_exe": {"packages":["tkinter"], "include_files":[
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
            os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
            dir_path+'\FormBox.py',
            dir_path+'\Genetic.py']}},
    executables = [Executable("main.py", base=base, icon=None)])