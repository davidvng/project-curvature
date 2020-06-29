import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

plt.rcParams['text.usetex']=True
font = {'size'   : 12, 'family':'sans-serif','sans-serif':['Helvetica']}
axislabelfontsize='large'
plt.rc('font', **font)
plt.rcParams["figure.figsize"] = [8.0,6.0]

from getdist import loadMCSamples

# Replace chains here
sample = loadMCSamples('chains/lcdm_lmax800', settings={'ignore_rows': 0.1})
sample2 = loadMCSamples('chains/lcdm_lmin800_chain2', settings={'ignore_rows': 0.1})

stats = sample.getMargeStats()
stats2 = sample2.getMargeStats()

par = [[stats.parWithName('omega_cdm'), stats.parWithName('H0'), stats.parWithName('sigma8'), stats.parWithName('Omega_m')],
         [stats2.parWithName('omega_cdm'), stats2.parWithName('H0'), stats2.parWithName('sigma8'), stats2.parWithName('Omega_m')]]

title = [r'$\Omega_\mathrm{c} h^2$', r'$H_0$', r'$\sigma_8$', r'$\Omega_\mathrm{m}$']

x_pos = np.arange(2)
labels = [r'$L_{max800}$', r'$L_{min800}$']

fig, ax = plt.subplots(4, sharex=True)

for i in range(4):
    ax[i].errorbar(0, par[0][i].mean, yerr=par[0][i].err, capsize=5, fmt='_', c='r', ms=10)
    ax[i].errorbar(1, par[1][i].mean, yerr=par[1][i].err, capsize=5, fmt='_', c='g', ms=10)
    ax[i].set_xticks(x_pos)
    ax[i].set_xticklabels(labels)
    ax[i].minorticks_on()
    ax[i].tick_params(axis='x', which='minor', bottom=False)
    ax[i].set_title(title[i], x=0.5, y=0.5)
    ax[i].margins(x=0.7)

# Give plot name    
fig.savefig('valentino3_lcdm.pdf')
