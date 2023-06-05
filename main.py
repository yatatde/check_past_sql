import os
import sys
from sources.create_load_tabs import create_load_tabs  
from sources.run_query import run_query
from sources.control.Qsettings import Qsysargv_list
from datetime import datetime

# init parameters
rpath = os.getcwd()+"\\"
qname = ''

def main(inparam):
    try:
        print("\nSTARTED at " + datetime.today().strftime("%D  %H:%M"))
        qname = Qsysargv_list[inparam].value
        create_load_tabs(qname, rpath)
        # run_query(qname, rpath)
    except: 
        raise KeyError()
if __name__ == "__main__":
     main(sys.argv[1])