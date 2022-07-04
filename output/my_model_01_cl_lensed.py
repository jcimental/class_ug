import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/jacquelinecimental/Public/class_public-3.1.2/output/my_model_01_cl_lensed.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['my_model_01_cl_lensed']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = [u'TT', u'EE', u'TE', u'BB', u'phiphi', u'TPhi', u'Ephi']
tex_names = ['TT', 'EE', 'TE', 'BB', 'phiphi', 'TPhi', 'Ephi']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))
ax.loglog(curve[:, 0], abs(curve[:, 2]))
ax.loglog(curve[:, 0], abs(curve[:, 3]))
ax.loglog(curve[:, 0], abs(curve[:, 4]))
ax.loglog(curve[:, 0], abs(curve[:, 5]))
ax.loglog(curve[:, 0], abs(curve[:, 6]))
ax.loglog(curve[:, 0], abs(curve[:, 7]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()