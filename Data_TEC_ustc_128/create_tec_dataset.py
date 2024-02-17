import h5py
import numpy as np
import os
import h5py

for year in range(2005, 2014):
    with h5py.File(os.path.join('/home/ess/cxt/work/data/GIM/', 'Step2_data_{}.mat'.format(year))) as data_load:
        tec_list = []
        tec_list.append(np.array(data_load['TECA']).transpose(0, 2, 1))

        #zoom tec_all
        from scipy.ndimage import zoom
        tec_all = np.vstack(tec_list).astype(np.float32)
        # tec_all = zoom(tec_all[:100], (1, 720/tec_all.shape[1], 1440/tec_all.shape[-1]))
        # tec_all = np.dstack((tec_all, tec_all[:, :, 0][:, :, None]))
        #
        # tec_all_reshape = tec_all[:tec_all.shape[0]//13*13].reshape((-1, 13, tec_all.shape[1], tec_all.shape[2]))
        #
        # np.save('tec_dataset', tec_all_reshape)

        # interp
        shape = [128, 256]
        x = np.linspace(0, 1, tec_all.shape[1])
        y = np.linspace(0, 1, tec_all.shape[2])
        x_new = np.linspace(0, 1, shape[0])
        y_new = np.linspace(0, 1, shape[1])
        from scipy import interpolate

        tec_all_new = np.zeros((tec_all.shape[0], shape[0], shape[1]), dtype=np.float32)
        for i in range(tec_all.shape[0]):
            # fi = interpolate.interp2d(y, x, tec_all[i])
            fi = interpolate.RectBivariateSpline(x, y, tec_all[i])
            tec_all_new[i] = fi(x_new, y_new)
        # tec_all_new = np.hstack((tec_all_new, tec_all_new[:, 0][:, None]))
        tec_all_reshape = tec_all_new[:tec_all_new.shape[0]//13*13].reshape((-1, 13, tec_all_new.shape[1], tec_all_new.shape[2]))
        # np.save('{}'.format(year), tec_all_reshape)

        with h5py.File('{}.h5'.format(year), 'w') as f:
            f.create_dataset("fields", data=tec_all_reshape)
        print('finish: {}'.format(year))
        del tec_all_reshape, tec_all_new, tec_all, tec_list