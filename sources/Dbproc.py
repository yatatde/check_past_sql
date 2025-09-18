import sqlite3
from sources.control.DbSettings import *
from sqlite3 import Error


class Dbproc:
    # 1 init paratemets
    def __init__(self, qid, rpath):
        self.qid = qid   # id of query used as enter parameter for process
        self.rpath = rpath
        self.name = get_dbname(self.qid)
        self.path = get_path(self.rpath, 'dbs')   # path to DB used for query
        self.file = f"{self.path}{self.name}.db"  # DB file used for query
        self.conn = Dbproc.get_conn_db(self)     # dbconnection initialization
        self.qfile = Dbproc.get_qfiles_names(self, 'query.sql')
        self.qrepfile = Dbproc.get_qrfiles_names(self, 'result.txt')
        self.qrep_pdf = Dbproc.get_qrpdf_names(self, 'rep.pdf')
        if self.name != "None":
            # get list of tables of database
            self.tabs = get_tabs(self.name)
            self.ctabfile = Dbproc.get_tfiles_names(
                self, 'create')  # scripts on tables creation
            self.ltabfile = Dbproc.get_tfiles_names(
                self, 'load')  # scripts on tables loading
        

    def get_conn_db(self):
        conn = None
        conn = sqlite3.connect(self.file)
        if conn == None:
            print("Connection to " + self.file + " was not esteblished")
        else:
            return conn

    def get_qfiles_names(self, suffix):
        return f"{get_path(self.rpath, 'work_in')}{self.qid}_{self.name}_{suffix}"

    def get_qrfiles_names(self, suffix):
        return f"{get_path(self.rpath, 'work_temp')}{self.qid}_{self.name}_{suffix}"

    def get_qrpdf_names(self, suffix):
        return f"{get_path(self.rpath, 'work_out')}{self.qid}_{self.name}_{suffix}"

    def get_tfiles_names(self, suffix):
        return [(f"{get_path(self.rpath, 'scripts')}{self.name}_{suffix}_tabs_{tab}.sql") for tab in self.tabs]

    def set_qrepfile(self, fname):
        self.qrepfile = fname
