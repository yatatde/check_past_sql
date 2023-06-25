from sources.Dbproc import *
from sources.Fileproc import *
def run_query(dba):
  # Run test query
  # sql_text = read_file(dba.qfile)
  qreport_data = dba.run_script(read_file(dba.qfile),"many")
  write_file(qreport_data,dba.qrepfile)
  dba.conn.close()
  print(f"\n ===>  An output report : \n{dba.qrepfile}\n ")
  print(f" ===>  had been generated for query {dba.qid}_{dba.name} kept in file : \n{dba.qfile} \n")

    
