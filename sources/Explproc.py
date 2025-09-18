from sources.Dbproc import *
from sources.control.DbSettings import *


class ExplDbproc(Dbproc):
    def __init__(self, qid, rpath):
        super().__init__(qid, rpath)
        self.name = None
        self.exp_repfile = f"{self.qrepfile.replace('_result.txt', '_explrep.txt')}"
        self.exp_graphrepfile = f"{self.qrepfile.replace('_result.txt', '_explrep_graph.txt')}"
        self.exp_repfile_pdf = f"{self.qrep_pdf.replace('rep.pdf', 'explrep.pdf')}"
        self.explain_report_html_template = f"{get_path(self.rpath, 'templates')}EXPLAIN_REPORT.html"
