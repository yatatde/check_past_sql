import csv
from sources.Dbproc import *
import collections
class ExplDbproc(Dbproc):
    def __init__(self, qid, rpath):
        super().__init__(qid, rpath)
        self.name = None
        self.exp_repfile = f"{self.qrepfile.rstrip('_result.txt')}_explrep.txt"
        self.exp_graphrepfile = f"{self.qrepfile.rstrip('_result.txt')}_explrep_graph.txt"
class ExplTreeNodes():
    def __init__(self, filename):
        self.filename = filename
        self.angle = "|__"
        self.vertical = "|  "
        self.juncT= "|--"
        self.blank = "   "
        self.idx= -1
        self.exp_graphrepfile_data = ''
        (self.rrid,self.child,self.parent,self.content) = ExplTreeNodes.get_file_data(self)
        self.Node = collections.namedtuple('Node',['rrid','child','parent','content'])
        self._nodes = [self.Node(self.rrid[i], self.child[i], (self.parent[i]), self.content[i]) 
                      for i in range(len(self.rrid))] 
        self._not_processed_counter = len(self.rrid)
    def get_file_data(self):
        fieldnames = ['child', 'parent', 'nonused', 'content']
        (rrid,child,parent,content) = ([],[],[],[])
        with open(self.filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile,fieldnames)
            for row in reader:
                child.append(row['child'].strip(' '))
                parent.append(row['parent'].strip(' '))
                content.append(row['content'].strip(' '))
                rrid.append(reader.line_num)
        return (rrid, child, parent, content)
    def __getitem__(self, position):
        return self[position]
    def get_branch_set(self, srch, position):
        branch_set = []
        try:
            for i in range(position, len(self._nodes) ,1):
                row = self._nodes.__getitem__(i)
                if row.parent == srch:
                    branch_set.append(i)
                    self._not_processed_counter -=1
            return(branch_set)
        except ValueError:
            print(f" ValueError")
           