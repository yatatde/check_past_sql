from enum import Enum
def get_subparts_message(qid,dba): 
    class subparts_enum(Enum):
        body_10 = f"\n===>  EXPLAIN PLAN reports : \n"
        plain_10 = f"\n(1) - plain - : \n{dba.exp_repfile_pdf}\n"
        graph_10 = f"\n(2) - graph - : \n{dba.exp_graphrepfile_pdf}\n"
        graph_11 = f"\n===>  generated for query : \n{dba.qfile}\n"
    try: 
        return(subparts_enum(qid[0:5]).value)
    except ValueError as ve:
        print(f"Missing / wrong explaine report enum settings\n{ve}")
        raise RuntimeError("unable to handle error")