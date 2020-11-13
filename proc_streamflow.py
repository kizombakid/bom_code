# Set the base directory depending on which computer your are on and mport 
import os, sys
import csv
from pathlib import Path
home = str(Path.home())

loc = '410734'
infile = home+'/bom_nn/data/streamflow/raw/rainfall_runoff_'+loc+'.csv'

f=open(infile, 'rt')
    
reader = csv.reader(f)

date = []
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
    if dl[0] != '#' and dl[0] != 't' and line[1] !='' and line[9] !='' and float(line[9]) > 0:
        date.append(dl[0:4]+dl[5:7]+dl[8:10])
        evap.append(float(line[1]))
        ss.append(float(line[2]))
        tmax.append(float(line[3]))
        s0.append(float(line[4]))
        print (date[-1], line[5])
        tmin.append(float(line[5]))
        et.append(float(line[6]))
        rain.append(float(line[7]))
        runoff.append(float(line[8]))
        streamflow.append(float(line[9]))
f.close()

print (streamflow)

