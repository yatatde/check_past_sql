import sqlite3
from sqlite3 import Error

class Qproc:
  # 1 init paratemets
  def __init__(qp, qid, qname, dbpath):
    qp.qid    = qid             # id of query used as enter parameter for process 
    qp.qname  = qname           # name of query 
    qp.qid_qname = qid + '_' + qname
    qp.dbname = qid + '_' + qname + '.db'   # name of DB of query
    qp.dbpath = dbpath          # path to DB of query
    qp.dbconn = Qproc.connect_db(qp) # dbconnection initialization 
    
  # 2 connect to qp  
  def connect_db(qp):
    conn = None
    conn = sqlite3.connect(qp.dbpath+qp.dbname)
    # print("OK! " + qp.dbpath+qp.dbname + "database connected.")
    if conn == None:
      print("Connection to " + qp.dbname + " was not esteblished")
    else:
      return conn
      
  # 3 files process
  def read_file(qp, inpfile):
    try:
      fd = open(inpfile, 'r')
      sql_script = fd.read()
      fd.close()
      return(sql_script)
    except Error as e:
      print(e)
  
  def write_file(qp, indata, outfile):
    try:
      with open(outfile,"w") as outf:
        for line in indata:
          line = str(line)
          outf.writelines(line.strip(",)" "'" " " "(") +"\n")
        outf.close()
    except Error as e:
      print(e)
    
  
  # 4 run sql script from text file
  def run_script(qp, sql_script, fetch_flag):
    cur = qp.dbconn.cursor()
    try:
      cur.execute(sql_script)
      qp.dbconn.commit()
      if fetch_flag == "one":
        return cur.fetchone()
      else: return cur.fetchall()
      cur.close()
    except Error as e:
      print(e)
      
  # 5 check connection status for test purpose
  def check_dbconn_status(qp):
    if qp.dbconn == None:
      print("Error! cannot connect to " + (qp.dbpath + qp.dbname))