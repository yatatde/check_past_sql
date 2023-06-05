# from generics.createDbConnection import create_connection
import os
from sources.Qproc import *
from sources.control.Qsettings import (Qtabs_list, apath)
def create_load_tabs(qname, rpath):
  # if db does not exist
  if os.path.isfile(apath(rpath,'dbs') + qname + '.db') == False:
    qp = Qproc(qname, apath(rpath,'dbs'))
    # if db connection was not esteblishwd
    if qp.dbconn is None:
        print("Connection to " + qp.dbname + " was not esteblished")
    else: 
      # create / load tables
      for tab in Qtabs_list[qname].value:
        ctab = qp.read_file(apath(rpath,'scripts') + qp.qname + "_create_tabs_" + tab + ".sql")
        ltab = qp.read_file(apath(rpath,'scripts') + qp.qname + "_load_tabs_" + tab + ".sql")
        qp.run_script(ctab,"one") # create source tables for query
        qp.run_script(ltab,"one") # load source t]ables for query
  else:
    print(f"\nDb {qname}.db had been created & loaded before in folder \n{apath(rpath,'dbs')}")
# create_load_tabs((sys.argv[1]), (os.getcwd()+"\\"))

    
