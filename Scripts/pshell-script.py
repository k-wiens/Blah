#!C:\_Git\Blah_Blah\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pyramid==1.5b1','console_scripts','pshell'
__requires__ = 'pyramid==1.5b1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pyramid==1.5b1', 'console_scripts', 'pshell')()
    )
