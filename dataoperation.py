import xlio
class data:
    def __init__(self,address):
        self.dataset=xlio.fileinput(address)
        self.datavars=self.dataset[0].keys()
print data("practicedataset.xlsx").datavars