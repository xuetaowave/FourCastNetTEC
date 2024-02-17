import numpy as np

import os
print(os.getcwd())
os.makedirs('train', exist_ok=True)
os.makedirs('test', exist_ok=True)
os.makedirs('out_of_sample', exist_ok=True)

train_list = [2005, 2006, 2007, 2009, 2010, 2011, 2013]
test_list = [2008, 2012]

import shutil
for year in test_list:
    shutil.copy('{}.h5'.format(year), 'out_of_sample')
    shutil.move('{}.h5'.format(year), 'test')

for year in train_list:
    shutil.move('{}.h5'.format(year), 'train')