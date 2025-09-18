from enum import Enum
import os


def get_dbname(qid):
    class Qids_dbs_enum(Enum):
        # query ID | name of database
        # under customization on new query adding
        q1 = "gengrants"
        q2 = "None"
        q3 = "followupgrants"
        q4 = "overgroup"
        q5 = "overgroup"
    try:
        return (Qids_dbs_enum[qid].value)
    except KeyError as e:
        print("get_dbname for " + qid)
        print_error(e)


def get_tabs(dbname):
    class Dbs_tabs_enum(Enum):
        # name of database | list of tables related to database
        # under customization on new query adding
        gengrants = ['SYSDUMMY1', 'SYSTABLES', 'SYSTABAUTH']
        overgroup = ['CUSTGOODS']
        followupgrants = ['SYSDUMMY1', 'SYSTABLES', 'SYSTABAUTH']
    try:
        return (Dbs_tabs_enum[dbname].value)
    except KeyError as e:
        print("get_tabs for " + dbname)
        print_error(e)

# list of project's folders
# NOT!!! under customization


def get_path(relative_path, svalue):
    class Sid_suffixes_enum(Enum):
        dbs = 'dbs\\'
        scripts = 'sources\\sqlscripts\\'
        work_in = 'work\\inputs\\'
        work_out = 'work\\outputs\\'
        work_temp = 'work\\temp\\'
        control = 'sources\\control\\'
        templates = 'templates\\'
    try:
        return (relative_path + Sid_suffixes_enum[svalue].value)
    except KeyError as e:
        print("get_path for " + relative_path + svalue)
        print_error(e)


def print_error(err):
    print(f" Either wrong input parameter provided {err}")
    print(
        f" Or check missing settings for {err} in \n    {os.path.abspath(__file__)}")
    exit()
