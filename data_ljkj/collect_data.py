import numpy as np
from datetime import datetime, timedelta
from time import time
import os 
os.getcwd()
start_date = datetime(2010, 1, 11)
end_date = datetime(2010, 12, 31)

kind = 'Density'
value = []
date_list = []
for i in range((end_date-start_date).days):
    t0 = time()
    c_date = start_date+timedelta(i)
    filename = '/home/ess/cxt/work/data/WACCM/{}/{}/FWSD_2010.cam.h1.{}-00000.{}.2-5km.npz'.format(c_date.year, kind, c_date.strftime('%Y-%m-%d'), kind)

    seconds = np.arange(0, 24*60*60, 60*30)
    date_i = np.array([c_date+timedelta(0, int(seconds[i])) for i in range(seconds.size)])

    if os.path.exists(filename) is True:
        with np.load(filename) as data_load:
            value.append(np.array(data_load['value'][:, -1].astype('float32')))      
        date_list.append(date_i)
        t1 = time()
        print('time usage:{}   finish:{}'.format(t1-t0, filename))
    else:
        print('not found: {}'.format(filename))
value_all = np.concatenate(value, axis=0)
np.savez(kind, fields=value_all, date=np.array(date_list))
pass

kind = 'T'
value = []
date_list = []
for i in range((end_date-start_date).days):
    t0 = time()
    c_date = start_date+timedelta(i)
    filename = '/home/ess/cxt/work/data/WACCM/{}/{}_height/FWSD_2010.cam.h1.{}-00000.{}.2-5km.npz'.format(c_date.year, kind, c_date.strftime('%Y-%m-%d'), kind)

    seconds = np.arange(0, 24*60*60, 60*30)
    date_i = np.array([c_date+timedelta(0, int(seconds[i])) for i in range(seconds.size)])

    if os.path.exists(filename) is True:
        with np.load(filename) as data_load:
            value.append(np.array(data_load['value'][:, -1].astype('float32')))      
        date_list.append(date_i)
        t1 = time()
        print('time usage:{}   finish:{}'.format(t1-t0, filename))
    else:
        print('not found: {}'.format(filename))
value_all = np.concatenate(value, axis=0)
np.savez(kind, fields=value_all, date=np.array(date_list))

kind = 'U'
value = []
date_list = []
for i in range((end_date-start_date).days):
    t0 = time()
    c_date = start_date+timedelta(i)
    filename = '/home/ess/cxt/work/data/WACCM/{}/{}_height/FWSD_2010.cam.h1.{}-00000.{}.2-5km.npz'.format(c_date.year, kind, c_date.strftime('%Y-%m-%d'), kind)

    seconds = np.arange(0, 24*60*60, 60*30)
    date_i = np.array([c_date+timedelta(0, int(seconds[i])) for i in range(seconds.size)])

    if os.path.exists(filename) is True:
        with np.load(filename) as data_load:
            value.append(np.array(data_load['value'][:, -1].astype('float32')))      
        date_list.append(date_i)
        t1 = time()
        print('time usage:{}   finish:{}'.format(t1-t0, filename))
    else:
        print('not found: {}'.format(filename))
value_all = np.concatenate(value, axis=0)
np.savez(kind, fields=value_all, date=np.array(date_list))

kind = 'V'
value = []
date_list = []
for i in range((end_date-start_date).days):
    t0 = time()
    c_date = start_date+timedelta(i)
    filename = '/home/ess/cxt/work/data/WACCM/{}/{}_height/FWSD_2010.cam.h1.{}-00000.{}.2-5km.npz'.format(c_date.year, kind, c_date.strftime('%Y-%m-%d'), kind)

    seconds = np.arange(0, 24*60*60, 60*30)
    date_i = np.array([c_date+timedelta(0, int(seconds[i])) for i in range(seconds.size)])

    if os.path.exists(filename) is True:
        with np.load(filename) as data_load:
            value.append(np.array(data_load['value'][:, -1].astype('float32')))      
        date_list.append(date_i)
        t1 = time()
        print('time usage:{}   finish:{}'.format(t1-t0, filename))
    else:
        print('not found: {}'.format(filename))
value_all = np.concatenate(value, axis=0)
np.savez(kind, fields=value_all, date=np.array(date_list))

kind = 'P'
value = []
date_list = []
for i in range((end_date-start_date).days):
    t0 = time()
    c_date = start_date+timedelta(i)
    filename = '/home/ess/cxt/work/data/WACCM/{}/{}_height/FWSD_2010.cam.h1.{}-00000.lev.2-5km.npz'.format(c_date.year, kind, c_date.strftime('%Y-%m-%d'))

    seconds = np.arange(0, 24*60*60, 60*30)
    date_i = np.array([c_date+timedelta(0, int(seconds[i])) for i in range(seconds.size)])

    if os.path.exists(filename) is True:
        with np.load(filename) as data_load:
            value.append(np.array(data_load['value'][:, -1].astype('float32')))      
        date_list.append(date_i)
        t1 = time()
        print('time usage:{}   finish:{}'.format(t1-t0, filename))
    else:
        print('not found: {}'.format(filename))
value_all = np.concatenate(value, axis=0)
np.savez(kind, fields=value_all, date=np.array(date_list))

