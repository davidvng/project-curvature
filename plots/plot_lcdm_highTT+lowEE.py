from getdist import plots

g=plots.get_subplot_plotter(chain_dir=r'/home1/davidvng/repos/project-curvature/chains')
roots = ['lcdm_highTT+lowEE']
xparams = ['omega_b','omega_cdm','theta_s_1e2', 'tau_reio','n_s','logA']
yparams = ['H0', 'Omega_m', 'sigma8']
g.rectangle_plot(xparams, yparams, roots=roots, filled=True)
g.export('lcdm_highTT+lowEE.pdf')
