import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/jacquelinecimental/Public/class_public-3.1.2/output/try32_background.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['try32_background']

fig, ax = plt.subplots()

index, curve = 0, data[0]
y_axis = ['rho_crit']
tex_names = ['(8\\pi G/3)rho_crit']
x_axis = 'z'
ylim = []
xlim = []
ax.plot(curve[:, 0], curve[:, 18])

ax.legend([root+': '+elem for (root, elem) in
    itertools.product(roots, y_axis)], loc='best')

ax.set_xlabel('z', fontsize=16)
plt.show()