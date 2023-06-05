import os
# import sys
from sources.Qproc import *
from sources.control.Qsettings import apath
def run_query(qname, rpath):
  qp = Qproc(qname, apath(rpath,'dbs'))
  # main processing: 
  if qp.dbconn is None:
    print("Connection to " + qp.dbname + " was not esteblished")
  else: 
    # Run test query
    outf = apath(rpath,'work') + qp.qname + "_result.txt"  
    qfile= apath(rpath,'work') + qp.qname + "_query.sql"
    sql_text = qp.read_file(qfile)
    result_data = qp.run_script(sql_text,"many")
    if os.path.exists(outf):
      os.remove(outf)
    qp.write_file(result_data,outf)
    print(f"\n ===>  An output report : \n{outf}\n ")
    print(f" ===>  had been generated for query : {qname} : \n{qfile} \n")
# run_query((sys.argv[1]), (os.getcwd()+"\\"))

    
