import os
import pandas as pd
from sqlite3 import Error


class FileProcess():
    def read_file(self, fname: str ='', read_mode: str = 'r', by_line: bool = False):
        try:
            f = open(fname, read_mode)
            if by_line:
                return([line for line in f.readlines()])
            else:
                return(f.read())
        except Error as e:
            print(e)
            exit()
        finally:
            f.close()
            
    def format_file_by_lines(self, fname=''):
        try:
            fdata = []
            with open(fname, encoding='utf-8') as f:
                line = f.readline()
                while line:
                    fdata.append(line.replace(' ', "&nbsp;").replace(
                        "\t", "&emsp;").strip("\'" "'\n'"))
                    # fdata.append(line.replace("\n","<br/>").replace(' ',"&nbsp;").replace("\t","&emsp;"))
                    line = f.readline()
            tt = pd.DataFrame(data={'sql': fdata})
            return (fdata)
        except Error as e:
            print(e)
            exit()

    def write_file_txt(self, fdata: list, fname='', line_update='not'):
        try:
            if os.path.exists(fname):
                os.remove(fname)
            with open(fname, "w") as fb:
                if line_update == 'not':
                    for line in fdata:
                        line = line
                        fb.writelines(line)
                if line_update == 'for pdf_table':
                    row_sn:int = -1
                    for i in range(len(fdata)):
                        line = fdata[i]
                        if str(fdata[i][0]).startswith('SubTab'):
                            row_sn:int = -1
                            _line = f'"SubTab",'
                        else:
                            row_sn += 1
                            if row_sn ==0:
                                _line: str = f'"SN",'
                            else: 
                                _line: str = f'"{str(row_sn)}",'
                        for field in line:
                            _line = f'{_line} "{str(field).strip()}",'
                        fb.writelines(_line+'\n')
                if line_update == 'strip':
                    for line in fdata:
                        line = str(line)
                        fb.writelines(line.strip(",)" "'" " " "(") + "\n")
            fb.close()
        except Error as e:
            print(e)
            exit()

    def delete_file(self, fname):
        try:
            if os.path.exists(fname):
                os.remove(fname)
        except Error as e:
            print(e)
            exit()
