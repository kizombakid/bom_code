#!/usr/bin/env python
#from __future__ import absolute_import, division, print_function

import numpy as np
from pathlib import Path


import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

from pathlib import Path

class NNDCube():

    def __init__(self, ndef, sdates, lookback, loc, type, dname, varsi, varso, update_open=None, update_pasx_open=None):

        #self.set = ndef.set
        #self.field = ndef.field
        #self.exp = ndef.
        #self.lookback = lookback
        #self.type = type
        #self.dname = dname

        buffer=60

        home = str(Path.home())
        if type == 'r' or type == 's':
            indir = home + '/rt/nn_data/'+ndef.field+'/'+ndef.set
        else:
            indir = home + '/'+loc+'/nn_data/'+ndef.field+'/'+ndef.set
        outdir = home + '/'+loc+'/exps/'+ndef.field+'/'+ndef.exp+'/'+ndef.set

        dates = np.load(indir+'/dates.npy')
        for ser in ndef.series:
            vvv = "self."+ser+" = np.load('"+indir+"/"+ser+".npy')"
            exec(vvv)

        #print ('open', min(self.open))
        #print ('volume',min(self.volume))
        #print ('pasx open',min(self.pasx_open))
        #print ('DJI',min(self.DJI_close))


        for proc in ndef.process:
            exec(proc)

        if update_open != None:
            self.open[-1] = update_open

        if type == 't':
            nshift = ndef.shift_t
            nstep = ndef.step_t
        elif type == 'v':
            nshift = ndef.shift_v
            nstep = ndef.step_v
        else:
            nshift = ndef.shift_i
            nstep = ndef.step_i



        if int(dates[0]) > int(sdates[0]):
            if type == 't':
                ipt1 = buffer
            else:
                ipt1 = 0
        if int(dates[-1]) < int(sdates[1]): ipt2 = len(dates)-1

        for n in range(1,len(dates)):
            if int(dates[n]) >= int(sdates[0]) and int(dates[n-1]) < int(sdates[0]): ipt1 = n
            if int(dates[n]) >= int(sdates[1]) and int(dates[n-1]) < int(sdates[1]): ipt2 = n

        # - ---- Need write out dates   ---------------------------------------------
        fdates = dates[ipt1+nshift:ipt2+1:nstep]

        if not os.path.exists(outdir): os.makedirs(outdir)
        np.save(outdir+'/data'+dname+'_dates_'+type+'.npy',np.int32(fdates))

        # Input values
        for nn,var in enumerate(varsi):

            value = np.zeros((len(fdates), lookback))
            for i, ipt in enumerate(range(ipt1+nshift,ipt2+1,nstep)):
                for k in range(0,lookback):
                    exec("value[i,k] = "+var)
            sub_mean = np.mean(value[:,:])
            div_std = np.std(value[:,:])

            if nn == 0:
                vali = np.zeros((len(fdates), lookback, len(varsi)))
                sub = np.zeros(len(varsi))
                div = np.zeros(len(varsi))
            vali[:,:,nn] = value
            sub[nn] = sub_mean
            div[nn] = div_std
            #if nn == 0: print (self.vali[0,0,0])

        if type == 't':
            np.save(outdir+'/data'+dname+'_vali_mean.npy',np.float32(sub))
            np.save(outdir+'/data'+dname+'_vali_std.npy',np.float32(div))
        else:
            sub = np.load(outdir+'/data'+dname+'_vali_mean.npy')
            div = np.load(outdir+'/data'+dname+'_vali_std.npy')

        for nn,var in enumerate(varsi):
            #print (type, var, sub[nn])
            vali[:,:,nn] = (vali[:,:,nn]-sub[nn])/div[nn]
 

        #line=' '
        #for i in range(11):
        #    line = line + str(round(self.vali[0,0,i],5))+'   '
        #print (line)



        np.save(outdir+'/data'+dname+'_vali_'+type+'.npy',np.float32(vali))

        if varso != None:
            for nn,var in enumerate(varso):
                value = np.zeros(len(fdates))
                for i, ipt in enumerate(range(ipt1+nshift,ipt2+1,nstep)):
                    exec("value[i] = "+var)
                sub_mean = np.mean(value)
                div_std = np.std(value)

                if nn == 0:
                    valo = np.zeros((len(fdates), len(varso)))
                    sub = np.zeros(len(varso))
                    div = np.zeros(len(varso))

                valo[:,nn] = value
                sub[nn] = sub_mean
                div[nn] = div_std

            if type == 't':
                np.save(outdir+'/data_valo_mean.npy',np.float32(sub))
                np.save(outdir+'/data_valo_std.npy',np.float32(div))
            else:
                sub = np.load(outdir+'/data_valo_mean.npy')
                div = np.load(outdir+'/data_valo_std.npy')

            for nn,var in enumerate(varso):
                valo[:,nn] = (valo[:,nn]-sub[nn])/div[nn]

            np.save(outdir+'/data_valo_'+type+'.npy',np.float32(valo))

 
