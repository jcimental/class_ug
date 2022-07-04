import matplotlib.pyplot as plt
import numpy as np
import itertools

files = ['/Users/jacquelinecimental/Public/class_public-3.1.2/output/base_2018_plikHM_TTTEEE_lowl_lowE_lensing00_pk.dat', '/Users/jacquelinecimental/Public/class_public-3.1.2/output/base_2018_plikHM_TTTEEE_lowl_lowE_lensing00_pk_nl.dat']
data = []
for data_file in files:
    data.append(np.loadtxt(data_file))
roots = ['base_2018_plikHM_TTTEEE_lowl_lowE_lensing00_pk', 'base_2018_plikHM_TTTEEE_lowl_lowE_lensing00_pk_nl']

fig, ax = plt.subplots()
y_axis = ['P(Mpc/h)^3']
tex_names = ['P (Mpc/h)^3']
x_axis = 'k (h/Mpc)'
ax.set_xlabel('k (h/Mpc)', fontsize=16)
plt.show()