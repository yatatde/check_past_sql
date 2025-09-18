from sources.GraphNodes import GraphNodes as GNs


class GraphExplReport(GNs):
    def __init__(self, filename='', data=[]):
        super().__init__(filename=filename, data=data)
        self.exp_graphrepfile_data += f'\n{10*(' ')}EXPLAINE QUERY PLAN'
        row = self._nodes.__getitem__(0)
        step_id = f'step {str(row.rrid).ljust(5,'.')}  '
        # content = f"node {row.eid}{GraphExplReport.get_subcontent(self, row.enotused)}.......{row.edetail}"
        content = f"{row.edetail}...node(id: {row.eid}{GraphExplReport.get_subcontent(self, row.enotused)})"
        GraphExplReport.generate_data(
            self, GNs(filename=filename, data=data), content=content, step_id=step_id)

    def generate_data(self, GNs: GNs, last_branch_node=True, step_id='', prefix='', content=''):
        new_line = f"{step_id}{prefix}{(self.angle if last_branch_node else self.juncT)}{content}"
        self.exp_graphrepfile_data = f"{self.exp_graphrepfile_data}\n{new_line}"
        #self.exp_graphrepfile_data = f"{self.exp_graphrepfile_data}{new_line}"
        if self._not_processed_counter > 0:
            self.idx += 1
            srch = (self._nodes.__getitem__(self.idx)).eid
            gbs = self.retrive_set(srch, self.idx)
            if not gbs == None:
                prefix = prefix + (self.blank if last_branch_node else self.vertical)
                for i in range(len(gbs)):
                    row = self._nodes.__getitem__(gbs[i])
                    step_id = f'step {str(row.rrid).ljust(5,'.')}  '
                    content = f"{row.edetail}...node(id: {row.eid}{GraphExplReport.get_subcontent(self, row.enotused)})"
                    last_branch_node = (i == len(gbs)-1)
                    GraphExplReport.generate_data(
                        self, GNs, last_branch_node=last_branch_node, step_id=step_id, prefix=prefix, content=content)

    def get_subcontent(self, enotused):
        val = ''
        if not (enotused == '0'):
        #    val = f"{self.gorizontal}, notused: {enotused}"
            val = f", notused: {enotused}"
        return (val)
