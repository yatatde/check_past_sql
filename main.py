import os
import sys
from sources.create_load_tabs import create_load_tabs 
from sources.run_query import *
from datetime import datetime
from sources.Dbproc import *
# from flask import Flask; Flask(__name__)

# app = Flask(__name__)
# @app.route('/')
relative_path = os.getcwd()+"\\"
def main(inparam):
  print("\nSTARTED at " + datetime.today().strftime("%D  %H:%M"))
  dba = Dbproc(inparam, relative_path)
  create_load_tabs(dba)
  run_query(dba)
if __name__ == "__main__":
#    app.run(debug = True)
    main(sys.argv[1])