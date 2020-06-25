import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

#plt.rcParams['text.usetex']=True
#font = {'size'   : 12, 'family':'sans-serif','sans-serif':['Helvetica']}
axislabelfontsize='large'
#plt.rc('font', **font)
plt.rcParams["figure.figsize"] = [8.0,6.0]

from getdist import loadMCSamples
sample = loadMCSamples('chains/lcdm_lmax800', settings={'ignore_rows': 0.1})
sample2 = loadMCSamples('chains/lcdm_lmin800', settings={'ignore_rows': 0.1})

stats = sample.getMargeStats()
stats2 = sample2.getMargeStats()

par11 = stats.parWithName('omega_cdm')
par12 = stats.parWithName('H0')
par13 = stats.parWithName('sigma8')
par14 = stats.parWithName('Omega_m')
par21 = stats2.parWithName('omega_cdm')
par22 = stats2.parWithName('H0')
par23 = stats2.parWithName('sigma8')
par24 = stats2.parWithName('Omega_m')

x_pos = np.arange(2)
labels = ['Lmax800', 'Lmin800']

fig, (ax, ax2, ax3, ax4) = plt.subplots(4, sharex=True)

ax.errorbar(0, par11.mean, yerr=par11.err, capsize=5, fmt='_', c='r', ms=10)
ax.errorbar(1, par21.mean, yerr=par21.err, capsize=5, fmt='_', c='g', ms=10)
ax.set_xticks(x_pos)
ax.set_xticklabels(labels)
ax.minorticks_on()
ax.tick_params(axis='x', which='minor', bottom=False)
ax.set_title('Omega_c*h^2', x=0.5, y=0.5)
ax.margins(x=0.7)

ax2.errorbar(0, par12.mean, yerr=par12.err, capsize=5, fmt='_', c='r', ms=10)
ax2.errorbar(1, par22.mean, yerr=par22.err, capsize=5, fmt='_', c='g', ms=10)
ax2.set_xticks(x_pos)
ax2.set_xticklabels(labels)
ax2.minorticks_on()
ax2.tick_params(axis='x', which='minor', bottom=False)
ax2.set_title('H0', x=0.5, y=0.5)
ax2.margins(x=0.7)

ax3.errorbar(0, par13.mean, yerr=par13.err, capsize=5, fmt='_', c='r', ms=10)
ax3.errorbar(1, par23.mean, yerr=par23.err, capsize=5, fmt='_', c='g', ms=10)
ax3.set_xticks(x_pos)
ax3.set_xticklabels(labels)
ax3.minorticks_on()
ax3.tick_params(axis='x', which='minor', bottom=False)
ax3.set_title('sigma8', x=0.5, y=0.5)
ax3.margins(x=0.7)

ax4.errorbar(0, par14.mean, yerr=par14.err, capsize=5, fmt='_', c='r', ms=10)
ax4.errorbar(1, par24.mean, yerr=par24.err, capsize=5, fmt='_', c='g', ms=10)
ax4.set_xticks(x_pos)
ax4.set_xticklabels(labels)
ax4.minorticks_on()
ax4.tick_params(axis='x', which='minor', bottom=False)
ax4.set_title('Omega_m', x=0.5, y=0.5)
ax4.margins(x=0.7)

fig.savefig('valentino3_lcdm.pdf')
