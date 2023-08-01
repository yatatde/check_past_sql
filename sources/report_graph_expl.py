from sources.Explproc import ExplTreeNodes
def report_graph_expl(etn : ExplTreeNodes , last_branch_node = True, prefix ='', content=''):
    new_line =  f"{prefix}{(etn.angle if last_branch_node else etn.juncT)}{content}"
    etn.exp_graphrepfile_data = f"{etn.exp_graphrepfile_data}\n{new_line}"
    if etn._not_processed_counter > 0: 
        etn.idx += 1 
        srch = (etn._nodes.__getitem__(etn.idx)).child
        gbs = etn.get_branch_set(srch, etn.idx)
        if not gbs==None:
            prefix = prefix + (etn.blank if last_branch_node else etn.vertical)
            for i in range(len(gbs)):
                row = etn._nodes.__getitem__(gbs[i])
                content=f"node {row.child} - {row.content} <-- step: {row.rrid}"
                last_branch_node = (i == len(gbs)-1 )
                report_graph_expl(etn, last_branch_node = last_branch_node, prefix = prefix, content = content) 