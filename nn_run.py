
import sys, os
from pathlib import Path
home = str(Path.home())

sys.path.append(home+'/bom_nn/nn_code')
from nn_main import *
from nn_diagnostics import *
from NNCodes import *


field = sys.argv[1]
exp = sys.argv[2]

expdir = home+'/bom_nn/exps/'+field+'/'+exp

# create experiment directory if it doesnt exist
if not os.path.exists(expdir):
    os.mkdir(expdir)

# read the control file
ndef = NN_Def(field,exp)

'''
if isinstance(ndef.sets, str):
    ndef.sets = NNCodes(field,ndef.sets).codes

print (ndef.sets)

if len(ndef.codesA) == 0:
    fcodesA = True
else:
    fcodesA = False
if len(ndef.codesB) == 0:
    fcodesB = True
else:
    fcodesB = False
if len(ndef.codesC) == 0:
    fcodesC = True
else:
    fcodesC = False

ndef.set=ndef.sets[int(setno)-1]
if fcodesA: ndef.codesA=[str(set)]
if fcodesB: ndef.codesB=[str(set)]
if fcodesC: ndef.codesC=[str(set)]
'''

code = ndef.sets[0]
ndef.codesA = code
ndef.set = code
expdir = home + '/bom_nn/exps/' + field + '/' + exp +'/' +code
for n in range(ndef.ens_start,ndef.n_ensembles):
    print ('Doing ', ndef.codesA, n)

    nn_main(n,ndef,update_data=False,run_nn=ndef.run_nn)

xx = NN_Diagnostics(ndef)
xx.summary()
xx.plot_history()
xx.plot_scatter()
xx.plot_scatter_all()
xx.plot_scatter(type='end')
xx.plot_scatter_all(type='end')
xx.plot_scatter_max(type='best')
xx.plot_scatter_max(type='end')

print ('Completed ',exp, ndef.set)


