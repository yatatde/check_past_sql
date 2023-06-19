import os
import sys
from sources.create_load_tabs import create_load_tabs  
from sources.run_query import run_query
from sources.control.Qsettings import *
from datetime import datetime
# from flask import Flask; Flask(__name__)

# init parameters
relative_path = os.getcwd()+"\\"

# app = Flask(__name__)
# @app.route('/')

def main(inparam):
  print("\nSTARTED at " + datetime.today().strftime("%D  %H:%M"))
  qid = inparam
  qname = ''
  try:
    qname = Qsysargv_list[qid].value
  except KeyError as e:
    print(f" Either wrong input parameter provided {e}")
    print(f" Or check missing settings for {e} in \n    {get_path(relative_path,'control')}Qsettings.py")
  if not qname == "":
    create_load_tabs(qid, qname, relative_path)
    run_query(qid, qname, relative_path)
if __name__ == "__main__":
#    app.run(debug = True)
    main(sys.argv[1])