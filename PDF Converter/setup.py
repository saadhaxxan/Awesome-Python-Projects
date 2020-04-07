from cx_Freeze import setup, Executable
import sys

base = None

if sys.platform == 'win32':
    base = None


executables = [Executable("PDF Converter.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {

        'packages':packages,
    },

}

setup(
    name = "PDF Converter",
    options = options,
    version = "1.0",
    description = 'any description',
    executables = executables
)
