import numpy as np
import h5py
import os

data = []
def load_data(filepath):
    data_temp = h5py.File(filepath)['fields'][::10]
    return data_temp

filepath = 'train'
file_list = os.listdir(filepath)
for file in file_list:
    data_temp = load_data(os.path.join(filepath, file))
    print(file)
    data.append(data_temp)
data = np.vstack(data)

global_mean = np.mean(data, axis=(0, 2, 3))[None, :, None, None]
print(global_mean.shape)
np.save('global_means.npy', global_mean)

global_stds = np.std(data, axis=(0, 2, 3))[None, :, None, None]
np.save('global_stds.npy', global_stds)

time_means = np.mean(data, axis=0)[None]
print(time_means.shape)
np.save('time_means.npy', time_means)