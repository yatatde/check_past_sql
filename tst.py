import os
# from sources.with_settings.qset1 import *
# print(__file__)
# print(os.getcwd()+"\\")
# print("===>" + __file__.replace(os.getcwd()+"\\" ,'').strip(".py"))

current_path = os.getcwd()+"\\"
#query_name = __file__.replace(os.getcwd()+"\\" ,'').strip(".py")
#db_exist =  os.path.isfile(current_path + "dbs\\" + query_name  + '.db')
#print(__dict__)
#print(current_path.__contains__('q'))

from enum import Enum
# class Qtabs(Enum):
#     findquater  = ["none"],
#     gengrants   = ["SYSDUMMY1","SYSTABLES","SYSTABAUTH"]
#     
# print(Qtabs('gengrants'))

def work_path(current_path,suf):  
    class Suffixs(Enum):
      dbspath     = 'dbs\\'
      scriptspath = ''
    return(current_path + Suffixs[suf].value)
#    print(current_path + Suffixs['dbspath'].value)
print(work_path(current_path,'dbspath'))

class Suffixs(Enum):
  dbspath     = 'dbs\\'
  scriptspath = ''
print(current_path,Suffixs['dbspath'].value)


# Enum classes have a custom metaclass:
#print(str(Menu['spam']))
#for element in Menu['spam']._value_:
#    print( element)
# <class 'enum.EnumMeta'>
# # EnumMeta defines __getitem__,
# # so __class_getitem__ is not called,
# # and the result is not a GenericAlias object:
# Menu['SPAM']
# <Menu.SPAM: 'spam'>
#print(Menu['spam'])
# <enum 'Menu'>