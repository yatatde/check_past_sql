from enum import Enum

class Qsysargv_list(Enum):
  one  = "gengrants"
  two  = "overgroup"

class Qtabs_list(Enum):
  gengrants  = ["SYSDUMMY1","SYSTABLES","SYSTABAUTH"]
  overgroup  = ["CUSTGOODS"]
    
def apath(root_path,active_suffix):  
  class Suffixs(Enum):
    dbs     = 'dbs\\'
    scripts = 'sources\\sqlscripts\\'
    work    = 'work\\'
  return(root_path + Suffixs[active_suffix].value)
    
  
  