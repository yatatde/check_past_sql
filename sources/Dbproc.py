import sqlite3
from sources.control.Init_settings import *
from sqlite3 import Error
from sources.Fileproc import *

class Dbproc:
  # 1 init paratemets
  def __init__(self, qid, rpath):
    self.qid   = qid   # id of query used as enter parameter for process 
    self.rpath = rpath
    self.name  = get_dbname(self.qid)
    self.path  = get_path(self.rpath,'dbs')   # path to DB used for query
    self.file  = f"{self.path}{self.name}.db" # DB file used for query
    self.tabs  = get_tabs(self.name)          # get list of tables of database
    self.conn  = Dbproc.get_conn_db(self)     # dbconnection initialization
    self.qfile = Dbproc.get_qfiles_names(self,'query.sql') 
    self.qrepfile = Dbproc.get_qfiles_names(self,'result.txt') 
    self.ctabfile = Dbproc.get_tfiles_names(self,'create')
    self.ltabfile = Dbproc.get_tfiles_names(self,'load')
  
  # 2 connect to self  
  def get_conn_db(self):
    conn = None
    conn = sqlite3.connect(self.file)
    if conn == None:
      print("Connection to " + self.file + " was not esteblished")
    else:
      return conn

  # 3 run sql script from text file
  def run_script(self, sql_script, fetch_flag):
    cur = self.conn.cursor()
    try:
      cur.execute(sql_script)
      self.conn.commit()
      if fetch_flag == "one":
        return cur.fetchone()
      else: 
        return cur.fetchall()
      cur.close()
    except Error as e:
      print(e)
      
  def get_qfiles_names(self, suffix):    
    return f"{get_path(self.rpath,'work')}{self.qid}_{self.name}_{suffix}"
    
  def get_tfiles_names(self, suffix): 
    return [(f"{get_path(self.rpath,'scripts')}{self.name}_{suffix}_tabs_{tab}.sql") for tab in self.tabs]