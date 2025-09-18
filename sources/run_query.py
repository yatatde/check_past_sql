from sources.QueryProcess import *
from sources.PdfForm import *
from sources.control.PdfSettings import *


def run_query(dba):
    qp = QueryProcess(dba.conn)
    qreport_data = qp.run_sql_script(sql_in=dba.qfile, fetch_flag="many")
    if dba.qid in ('q1','q2','q3','q4'):
        qp.write_file_txt(fdata=qreport_data, fname=dba.qrepfile,line_update='for pdf_table')
    else:qp.write_file_txt(fdata=qreport_data, fname=dba.qrepfile,line_update='strip')
    # print(f"\n ===>  An output report : \n{dba.qrepfile}\n ")
    # print(f" ===>  had been generated for statement {dba.qid}_{dba.name} kept in file : \n{dba.qfile} \n")
    # SQL RESULTS REPORT IN PDF FORMAT
    title = f"SQL results report on {(dba.qfile[dba.qfile.find(dba.qid):]).strip('_query.sql')} "

    # portrait / milimeters / A4 size Note: A4 page width/height - 210:297
    pdf = PDF('P', 'pt', 'A4')
    pdf.compress = True
    pdf.alias_nb_pages()
    pdf.header_type = 'h_01'
    pdf.doc_title(title)
    pdf.add_page()
    pdf.insert_toc_placeholder(render_toc)
    pf = PdfForm
    pdf.start_section(f"1. SQL statment {(dba.qfile[dba.qfile.find(dba.qid):]).strip('_query.sql')} content", level=0, strict=True)
    pf(pdf, unit_name=dba.qfile,unit_id='sql').form_section()
    pdf.add_page(orientation='landscape')
    pdf.start_section(f"2. SQL results", level=0, strict=True)
    if dba.qid in ('q1','q2','q3','q4'):
        pf(pdf, unit_name=dba.qrepfile, unit_id = f'{dba.qid}_txt').form_table()
    else: pf(pdf, unit_name=dba.qrepfile, unit_id = 'text').form_section()
    qp.delete_file(dba.qrepfile)
    pf(pdf, unit_name=dba.qrep_pdf).print_report()
