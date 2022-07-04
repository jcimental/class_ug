import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/jacquelinecimental/Public/class_public-3.1.2/output/base_2018_plikHM_TTTEEE_lowl_lowE_lensing00_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['base_2018_plikHM_TTTEEE_lowl_lowE_lensing00_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 1])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()