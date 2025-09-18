import csv
from sources.FileProcess import FileProcess as FP
import collections


class GraphNodes(FP):
    def __init__(self, filename='', data=[]):
        super().__init__()
        self.filename = filename
        self.data = data
        self.angle = "|__"
        self.vertical = "|  "
        self.gorizontal = "__"
        self.juncT = "|--"
        self.blank = "   "
        self.idx = -1
        self.exp_graphrepfile_data = ''
        (self.rrid, self.eid, self.eparent,
         self.enotused, self.edetail) = ([], [], [], [], [])
        if not self.filename == '':
            with open(self.filename, newline='') as csvfile:
                self.data = csv.DictReader(csvfile, [0, 1, 2, 3])
                GraphNodes.read_nodes_data(self)
                self.rrid = list(range((self.data.line_num+1)))[1:]
        elif not str(self.data) == '':
            GraphNodes.read_nodes_data(self)
            self.rrid = list(range(len(self.data)+1))[1:]
        self.Node = collections.namedtuple(
            'Node', ['rrid', 'eid', 'eparent', 'enotused', 'edetail'])
        self._nodes = [self.Node(self.rrid[i], self.eid[i], self.eparent[i], self.enotused[i], self.edetail[i])
                       for i in range(len(self.rrid))]
        self._not_processed_counter = len(self.rrid)

    def read_nodes_data(self):
        reader = self.data
        for row in reader:
            self.eid.append(str(row[0]).strip(' '))
            self.eparent.append(str(row[1]).strip(' '))
            self.enotused.append(str(row[2]).strip(' '))
            self.edetail.append(str(row[3]).strip(' '))

    def __getitem__(self, position):
        return self[position]

    def retrive_set(self, srch, position):
        branch_set = []
        try:
            for i in range(position, len(self._nodes), 1):
                row = self._nodes.__getitem__(i)
                if row.eparent == srch:
                    branch_set.append(i)
                    self._not_processed_counter -= 1
            return (branch_set)
        except ValueError as e:
            print(f" ValueError - branch_set counter confuse\n{e}")
