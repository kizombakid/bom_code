epochs == 500
run_nn == True

field == 'streamflow'

n_ensembles == 4
ens_start == 0

n_nets == 1

dates_train == [19700101, 19950101]
dates_val == [19950101, 201001010]
dates_ind == [20100101, 20200101]
step_t == 1
shift_t == 0
step_v == 1
shift_v == 0
step_i == 1
shift_i == 0

sets == ['410734']

batchsize == 128

optimizer == 'adam'
patience == 15
                   

codesA == []
lookbackA == 10


network1A == ['LSTM',10,{'return_sequences':True}]
network1A == ['LSTM',10,{'return_sequences':False}]

network1A == ['Dense',1]

codesB == []
codesC == []

series == ['streamflow']
series == ['rain']

process == ['']

varsiA == ['self.streamflow[ipt-1-k]']
varsiA == ['self.rain[ipt-1-k]']


varso == 'self.streamflow[ipt]'
