# from generics.createDbConnection import create_connection
import os
from sources.Qproc import *
from sources.control.Qsettings import (Qtabs_list, get_path)
def create_load_tabs(qid, qname, relative_path):
  db_file = get_path(relative_path,'dbs') + qid + '_' + qname + '.db'
  # if db does not exist - the db for processing query is being created
  if os.path.isfile(db_file) == False:
    qp = Qproc(qid, qname, get_path(relative_path,'dbs'))
    # if db connection was not esteblished
    if qp.dbconn is not None:
      # create / load tables
      for tab in Qtabs_list[qname].value:
        ctab = qp.read_file(get_path(relative_path,'scripts') + qp.qid_qname + "_create_tabs_" + tab + ".sql")
        ltab = qp.read_file(get_path(relative_path,'scripts') + qp.qid_qname + "_load_tabs_" + tab + ".sql")
        qp.run_script(ctab,"one") # create source tables for query
        qp.run_script(ltab,"one") # load source t]ables for query
  else:
    print(f"\nDb had been created & loaded before :{db_file}")
# create_load_tabs((sys.argv[1]), (os.getcwd()+"\\"))

    
