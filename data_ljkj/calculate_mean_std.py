import numpy as np
import h5py

data_load = h5py.File('train/2010.h5', 'r')
data_load.keys()

data =   data_load['fields']
global_mean = np.mean(data, axis=(0, 2, 3))[None, :, None, None]
print(global_mean.shape)
np.save('global_means.npy', global_mean)

global_stds = np.std(data, axis=(0, 2, 3))[None, :, None, None]
np.save('global_stds.npy', global_stds)

time_means = np.mean(data, axis=0)[None]
print(time_means.shape)
np.save('time_means.npy', time_means)

