import numpy as np
from pathlib import Path
home = str(Path.home())
import csv
import os, sys
import sqlite3

sys.path.append(home+'/anal/anal_code')
from nn_stock_tools import *
from NNCodes import *

import matplotlib.pyplot as plt

market = 'ase'
code='p_asx'


v1 = np.load(home+'/bom_nn/exps/streamflow/test/410734/dataA_vali_v.npy')

print (np.shape(v1),np.size(v1))

