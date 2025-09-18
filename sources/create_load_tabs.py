from sources.QueryProcess import *


def create_load_tabs(dba):
    qp = QueryProcess(dba.conn)
    sql_existing_tabs = """select ifnull(GROUP_CONCAT("'"||name||"'"),"ISNULL") from sqlite_master where 
      type = 'table' and name in (""" + str(dba.tabs).strip("[""]")+""')'""
    existing_tabs = qp.run_sql_script(
        sql_in=sql_existing_tabs, fetch_flag="one", dynamic='no')[0]
    # if tables were not created & loaded before
    if not all(tab in str(dba.tabs) for tab in existing_tabs):
        for i in range(len(dba.tabs)):
            # create source tables for query
            qp.run_sql_script(sql_in=dba.ctabfile[i], fetch_flag="one")
            # load source tables for query
            qp.run_sql_script(sql_in=dba.ltabfile[i], fetch_flag="one")
    else:
        print(
            f"\n Note: Db had been created & loaded before:\n       {dba.file}")
