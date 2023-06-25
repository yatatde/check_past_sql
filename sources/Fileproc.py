# from sources.control.Init_settings im port *
import os
from sqlite3 import Error
def read_file(inpfile):
  try:
    fb = open(inpfile, 'r')
    outdata = fb.read()
    fb.close()
    return(outdata)
  except Error as e:
    print(e)
    exit()

def write_file(inpdata, outfile):
  try:
    if os.path.exists(outfile):
      os.remove(outfile)
    with open(outfile,"w") as fb:
      for line in inpdata:
        line = str(line)
        fb.writelines(line.strip(",)" "'" " " "(") +"\n")
      fb.close()
  except Error as e:
    print(e)
    exit()