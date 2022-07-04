import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/jacquelinecimental/Public/class_public-3.1.2/output/try30_cl.dat', '/Users/jacquelinecimental/Public/class_public-3.1.2/output/try31_cl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['try30_cl', 'try31_cl']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

index, curve = 1, data[1]
y_axis = ['TT']
tex_names = ['TT']
x_axis = 'l'
ylim = []
xlim = []
ax.loglog(curve[:, 0], abs(curve[:, 1]))

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('$\ell$', fontsize=16)
plt.show()