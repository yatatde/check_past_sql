from enum import Enum

class Qsysargv_list(Enum):
# parameter | name of query
# under customization
  one   = "gengrants"
  two   = "overgroup"
  three = "followupgrants"

class Qtabs_list(Enum):
# name of query | list of tables accessing in query
# under customization
  gengrants      = ["SYSDUMMY1","SYSTABLES","SYSTABAUTH"]
  overgroup      = ["CUSTGOODS"]
  followupgrants = ["SYSDUMMY1","SYSTABLES","SYSTABAUTH"]

# list of project's folders 
# NOT!!! under customization   
def apath(root_path,active_suffix):  
  class Suffixs(Enum):
    dbs     = 'dbs\\'
    scripts = 'sources\\sqlscripts\\'
    work    = 'work\\'
  return(root_path + Suffixs[active_suffix].value)
    
  
  