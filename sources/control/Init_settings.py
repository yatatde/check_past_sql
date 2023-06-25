from enum import Enum
import os

def get_dbname(qid):
  class Qids_dbs_enum(Enum):
  # query ID | name of database
  # under customization on new query adding
    q1  = "gengrants"
    q1e = "gengrants"
    q2  = "overgroup"
    q3  = "followupgrants"
  try: 
    return(Qids_dbs_enum[qid].value)
  except KeyError as e:
    print("get_dbname for "+ qid)
    print_isettings_error(e)

def get_tabs(dbname):
  class Dbs_tabs_enum(Enum):
  # name of database | list of tables related to database
  # under customization on new query adding
    gengrants      = ['SYSDUMMY1','SYSTABLES','SYSTABAUTH']
    overgroup      = ['CUSTGOODS']
    followupgrants = ['SYSDUMMY1','SYSTABLES','SYSTABAUTH']
  try:
    return(Dbs_tabs_enum[dbname].value)
  except KeyError as e:
    print("get_tabs for "+ dbname)
    print_isettings_error(e)

# list of project's folders 
# NOT!!! under customization
def get_path(relative_path,svalue):  
  class Sid_suffixes_enum(Enum):
    dbs     = 'dbs\\'
    scripts = 'sources\\sqlscripts\\'
    work    = 'work\\'
    control = 'sources\\control\\'
  try:
    return(relative_path + Sid_suffixes_enum[svalue].value)
  except KeyError as e:
    print("get_path for "+ relative_path + svalue)
    print_isettings_error(e)

def print_isettings_error(err):
  print(f" Either wrong input parameter provided {err}")
  print(f" Or check missing settings for {err} in \n    {os.path.dirname(os.path.abspath(__file__))}")
  exit () 