# Set the base directory depending on which computer your are on and mport 
import os, sys
import csv
import numpy as np
from pathlib import Path
home = str(Path.home())

loc = '410734'
type = 'streamflow'
infile = home+'/bom_nn/data/'+type+'/raw/rainfall_runoff_'+loc+'.csv'

f=open(infile, 'rt')
    
reader = csv.reader(f)

dates = []
evap = []
ss = []
tmax = []
s0 = []
tmin = []
et = []
rain = []
runoff = []
streamflow = []
for line in reader:
    dl=line[0]
    if dl[0] != '#' and dl[0] != 't' and line[1] !='' and line[9] !='' and line[5] !='':
        dates.append(int(dl[0:4]+dl[5:7]+dl[8:10]))
        evap.append(float(line[1]))
        ss.append(float(line[2]))
        tmax.append(float(line[3]))
        s0.append(float(line[4]))
        #print (line)
        tmin.append(float(line[5]))
        et.append(float(line[6]))
        rain.append(float(line[7]))
        runoff.append(float(line[8]))
        streamflow.append(float(line[9]))
f.close()

outdir=home+'/bom_nn/nn_data/'+type+'/'+loc
np.save(outdir+'/dates.npy',dates)
np.save(outdir+'/evap.npy',evap)
np.save(outdir+'/ss.npy',ss)
np.save(outdir+'/tmax.npy',tmax)
np.save(outdir+'/s0.npy',s0)
np.save(outdir+'/tmin.npy',tmin)
np.save(outdir+'/et.npy',et)
np.save(outdir+'/rain.npy',rain)
np.save(outdir+'/runoff.npy',runoff)
np.save(outdir+'/streamflow.npy',streamflow)

