#!C:\_Git\Blah_Blah\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pygments==1.6','console_scripts','pygmentize'
__requires__ = 'pygments==1.6'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pygments==1.6', 'console_scripts', 'pygmentize')()
    )
