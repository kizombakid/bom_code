
from pathlib import Path
import numpy as np


# *********  Can't put print statements in here cause messes up nn_run.sh with inline run ********

class NN_Def():

    def __init__(self, field, name, basedir=""):

        self.exp = name

        home = str(Path.home())
        dir = home + '/bom_nn/exps'

        file = open(dir + '/'+field+'/'+name+"/def.ctl", "r")

        self._defaults()
        self.basedir = dir

        for line in file:

            if '==' in line:

                line = line.replace(" ", "").split("==")

                if 'network' in line[0]:
                    exec("self." + line[0] + ".append(" + str(line[1]) + ")")
                elif 'series' in line[0] or 'varsi' in line[0] or 'varso' in line[0] or 'process' in line[0]:
                    exec("self."+line[0]+" = np.append(self." +line[0]+","+ str(line[1]) + ")")
                else:
                    exec("self." + line[0] + "=" + str(line[1]))

    def _defaults(self):

        self.network1A = []
        self.network1B = []
        self.network2 = []
        self.epochs = 1
        self.lookback = 1
        self.batchsize = 1
        self.rmsprop = 0
        self.patience = 1
        self.optimizer = 'rmsprop'

        self.series = []
        self.varsiA = []
        self.varsiB = []
        self.varsiC = []
        self.process = []
        self.varso = []





