from sources.Explproc import *
from sources.Fileproc import *
from sources.report_graph_expl import *
def run_query_explain_plan(dba):
    ### 1 - sourse explain plan report is being generated
    expl_plan_query =f" {'EXPLAIN QUERY PLAN '}\n{read_file(dba.qfile)}"
    expl_plan_query_data = dba.run_script(expl_plan_query,"many")
    write_file(fdata = expl_plan_query_data,fname = dba.exp_repfile)
    dba.conn.close()
    ### 2 -graph explain plan report is being generated
    etn = ExplTreeNodes(dba.exp_repfile)
    etn.exp_graphrepfile_data += 'A graph report for EXPLAIN QUERY PLAN Command'  
    etn.exp_graphrepfile_data += '\nnode 0'
    row = etn._nodes.__getitem__(0)
    content = f"node {row.child} {row.content} <-- step: {row.rrid}"
    report_graph_expl(etn, content = content) ### recursive process
    write_file(fdata = etn.exp_graphrepfile_data, fname = dba.exp_graphrepfile, nonstr = 'yes')
    print(f"\n===>  EXPLAIN PLAN reports : \n")
    print(f"\n(1) - plain - : \n{dba.exp_repfile}\n")
    print(f"\n(2) - graph - : \n{dba.exp_graphrepfile}\n")
    print(f"\n===>  generated for query : \n{dba.qfile}\n")