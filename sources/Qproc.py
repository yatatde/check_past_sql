import sqlite3
from sqlite3 import Error

class Qproc:
  # 1 init paratemets
  def __init__(qp, qname, dbpath):
    qp.qname  = qname
    qp.dbname = qname + '.db'
    qp.dbpath = dbpath
    qp.dbconn = Qproc.connect_db(qp)
    
  # 2 connect to qp  
  def connect_db(qp):
    conn = None
    try:
      conn = sqlite3.connect(qp.dbpath+qp.dbname)
      # print("OK! " + qp.dbpath+qp.dbname + "database connected.")
      return conn
    except Error as e:
      print(e)
      
  # 3 files process
  def read_file(qp, inpfile):
    fd = open(inpfile, 'r')
    sql_script = fd.read()
    fd.close()
    return(sql_script)
  
  def write_file(qp, indata, outfile):
    with open(outfile,"w") as outf:
      for line in indata:
        line = str(line)
        outf.writelines(line.strip(",)" "'" " " "(") +"\n")
      outf.close()
  
  # 4 run sql script from text file
  def run_script(qp, sql_script, fetch_flag):
      cur = qp.dbconn.cursor()
      cur.execute(sql_script)
      qp.dbconn.commit()
      if fetch_flag == "one":
        return cur.fetchone()
      else: return cur.fetchall()
      cur.close()
      
  # 5 check connection status for test purpose
  def check_dbconn_status(qp):
    if qp.dbconn == None:
      print("Error! cannot connect to " + (qp.dbpath+qp.dbname))