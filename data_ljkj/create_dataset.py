import numpy as np
import h5py 

data_load_D = np.load('Density.npz')
D = data_load_D['fields']

data_load_P = np.load('P.npz')
P = data_load_P['fields']

data_load_T = np.load('T.npz')
T = data_load_T['fields']

data_load_U = np.load('U.npz')
U = data_load_U['fields']

data_load_V = np.load('V.npz')
V = data_load_V['fields']

list(data_load_D.keys()), D.shape, P.shape, T.shape, U.shape, V.shape

data = np.hstack((D.reshape((-1, 6)+D.shape[1:]), P.reshape((-1, 6)+P.shape[1:]), T.reshape((-1, 6)+T.shape[1:]), U.reshape((-1, 6)+U.shape[1:]), V.reshape((-1, 6)+V.shape[1:])))
train_mask = data.shape[0]//6*5

import os
print(os.getcwd())
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)
os.makedirs('out_of_sample', exist_ok=True)

import h5py
with h5py.File('train/2010.h5', 'w') as f:
    f.create_dataset("fields", data=data[:train_mask])
    
with h5py.File('test/2010.h5', 'w') as f:
    f.create_dataset("fields", data=data[train_mask:])
    
with h5py.File('out_of_sample/2010.h5', 'w') as f:
    f.create_dataset("fields", data=data[train_mask:])



