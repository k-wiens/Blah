#!C:\_Git\Blah_Blah\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'repoze.sendmail==4.2','console_scripts','qp'
__requires__ = 'repoze.sendmail==4.2'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('repoze.sendmail==4.2', 'console_scripts', 'qp')()
    )
