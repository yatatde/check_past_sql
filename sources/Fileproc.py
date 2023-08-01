import os
from sqlite3 import Error
def read_file(fname = ''):
  try:
    fb = open(fname, 'r')
    fdata = fb.read()
    fb.close()
    return(fdata)
  except Error as e:
    print(e)
    exit()

def write_file(fdata = '', fname = '', nonstr = ''):
  try:
    if os.path.exists(fname):
      os.remove(fname)
    with open(fname,"w") as fb:
      for line in fdata:
        line = str(line)
        if nonstr == 'yes':
          fb.writelines(line)
        else:
          fb.writelines(line.strip(",)" "'" " " "(") +"\n")
    fb.close()
  except Error as e:
    print(e)
    exit()