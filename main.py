import os
import sys
from sources.create_load_tabs import create_load_tabs
from sources.run_query import *
from datetime import datetime
from sources.Dbproc import *
from sources.Explproc import *
from sources.run_explain_query_plan import *
# from flask import Flask; Flask(__name__)
# app = Flask(__name__)
# @app.route('/')
relative_path = os.getcwd()+"\\"


def main(parm):
    print("\nSTARTED at " + datetime.today().strftime("%D  %H:%M"))
    if parm[0:6] == 'explqp':
        dba = ExplDbproc(parm[6:8], relative_path)
        run_explain_query_plan(dba)
    else:
        dba = Dbproc(parm[0:2], relative_path)
        if not dba.name == "None":
            create_load_tabs(dba)
        run_query(dba)


if __name__ == "__main__":
    #    app.run(debug = True)
    main(sys.argv[1])
