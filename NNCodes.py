import sys

class NNCodes():
    def __init__(self,field, name):
        exec('self.'+field+'()')
        exec('self.codes = self.'+name)

    def streamflow(self):
    

        self.all = ['410734']

 

if __name__ == "__main__":
    field = sys.argv[1]
    name = sys.argv[2]
    xx = NNCodes(field, name)
    for n,x in enumerate(xx.codes):
        if n == 0 :
            line = x
        else:
            line = line +' '+x
    print (line)




