import os
# import sys
from sources.Qproc import *
from sources.control.Qsettings import get_path
def run_query(qid, qname, relative_path):
  qp = Qproc(qid, qname, get_path(relative_path,'dbs'))
  # main processing: 
  if qp.dbconn is not None:
    # Run test query
    outf = get_path(relative_path,'work') + qp.qid_qname + "_result.txt"  
    qfile= get_path(relative_path,'work') + qp.qid_qname + "_query.sql"
    sql_text = qp.read_file(qfile)
    result_data = qp.run_script(sql_text,"many")
    if os.path.exists(outf):
      os.remove(outf)
    qp.write_file(result_data,outf)
    print(f"\n ===>  An output report : \n{outf}\n ")
    print(f" ===>  had been generated for query : {qname} : \n{qfile} \n")
# run_query((sys.argv[1]), (os.getcwd()+"\\"))

    
