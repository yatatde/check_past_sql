from sources.Fileproc import *
def create_load_tabs(dba):
  sql_existing_tabs = """select ifnull(GROUP_CONCAT("'"||name||"'"),"ISNULL") from sqlite_master where 
      type = 'table' and name in (""" + str(dba.tabs).strip("[""]")+""')'""
  existing_tabs = dba.run_script(sql_existing_tabs,"one")[0]
  # if tables were not created & loaded before
  if not all(tab in str(dba.tabs) for tab in existing_tabs):
    for i in range(len(dba.tabs)):
      dba.run_script(read_file(dba.ctabfile[i]),"one") # create source tables for query
      dba.run_script(read_file(dba.ltabfile[i]),"one") # load source tables for query
  else:
    print(f"\n Note: Db had been created & loaded before:\n       {dba.file}")
# create_load_tabs((sys.argv[1]), (os.getcwd()+"\\"))

    
