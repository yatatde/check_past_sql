from sources.FileProcess import FileProcess as fp
from sqlite3 import Error


class QueryProcess(fp):
    def __init__(self, conn):
        super().__init__()
        self.conn = conn
    # run sql script read from file which name passed in sql_input - dynamic SQL
    # run sql script passed in sql_input - non dynamic SQL

    def run_sql_script(self, prefix='', sql_in='', fetch_flag='', dynamic='yes'):
        cur = self.conn.cursor()
        try:
            if dynamic == 'yes':
                sql_script = prefix + fp().read_file(fname=sql_in, read_mode = 'r', by_line = False).__str__()
            else:
                sql_script = sql_in
            cur.execute(sql_script)
            self.conn.commit()
            if fetch_flag == "one":
                return cur.fetchone()
            else:
                return cur.fetchall()
            cur.close()
            self.conn.close()
        except OSError:
            raise RuntimeError("unable to handle error")
