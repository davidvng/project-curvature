import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

plt.rcParams['text.usetex']=True
font = {'size'   : 12, 'family':'sans-serif','sans-serif':['Helvetica']}
axislabelfontsize='large'
plt.rc('font', **font)
plt.rcParams["figure.figsize"] = [8.0,6.0]

from getdist import loadMCSamples
sample = loadMCSamples('chains/lcdm_lmax800', settings={'ignore_rows': 0.1})
sample2 = loadMCSamples('chains/lcdm_lmin800_chain2', settings={'ignore_rows': 0.1})
sample3 = loadMCSamples('chains/omegak_lmax800', settings={'ignore_rows': 0.1})
sample4 = loadMCSamples('chains/omegak_lmin800', settings={'ignore_rows': 0.1})

stats = sample.getMargeStats()
stats2 = sample2.getMargeStats()
stats3 = sample3.getMargeStats()
stats4 = sample4.getMargeStats()

par = [[stats.parWithName('omega_cdm'), stats.parWithName('H0'), stats.parWithName('sigma8'), stats.parWithName('Omega_m')],
         [stats2.parWithName('omega_cdm'), stats2.parWithName('H0'), stats2.parWithName('sigma8'), stats2.parWithName('Omega_m')]]
par2 = [[stats3.parWithName('omega_cdm'), stats3.parWithName('H0'), stats3.parWithName('sigma8'), stats3.parWithName('Omega_m')],
         [stats4.parWithName('omega_cdm'), stats4.parWithName('H0'), stats4.parWithName('sigma8'), stats4.parWithName('Omega_m')]]

title = [r'$\Omega_\mathrm{c} h^2$', r'$H_0$', r'$\sigma_8$', r'$\Omega_\mathrm{m}$']

x_pos = np.arange(2)
labels = [r'$\Lambda CDM,L_{max800}$', r'$\Lambda CDM,L_{min800}$']
labels2 = [r'$\Omega_\mathrm{k}=-0.045,L_{max800}$', r'$\Omega_\mathrm{k}=-0.045,L_{min800}$']

fig, ax = plt.subplots(4, 2)

for i in range(4):
    ax[i, 0].errorbar(0, par[0][i].mean, yerr=par[0][i].err, capsize=5, fmt='_', c='r', ms=10)
    ax[i, 0].errorbar(1, par[1][i].mean, yerr=par[1][i].err, capsize=5, fmt='_', c='g', ms=10)
    ax[i, 0].set_xticks(x_pos)
    ax[i, 0].set_xticklabels(' ')
    ax[i, 0].minorticks_on()
    ax[i, 0].tick_params(axis='x', which='minor', bottom=False)
    ax[i, 0].set_title(title[i], x=0.5, y=0.5)
    ax[i, 0].margins(x=0.7)
ax[3, 0].set_xticklabels(labels, rotation=80)

for i in range(4):
    ax[i, 1].errorbar(0, par2[0][i].mean, yerr=par2[0][i].err, capsize=5, fmt='_', c='r', ms=10)
    ax[i, 1].errorbar(1, par2[1][i].mean, yerr=par2[1][i].err, capsize=5, fmt='_', c='g', ms=10)
    ax[i, 1].set_xticks(x_pos)
    ax[i, 1].set_xticklabels(' ')
    ax[i, 1].minorticks_on()
    ax[i, 1].tick_params(axis='x', which='minor', bottom=False)
    ax[i, 1].set_title(title[i], x=0.5, y=0.5)
    ax[i, 1].margins(x=0.7)
ax[3, 1].set_xticklabels(labels2, rotation=80)

plt.tight_layout()
fig.savefig('valentino3_full.pdf')
