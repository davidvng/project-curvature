from getdist import plots

g=plots.get_subplot_plotter(chain_dir=r'/home1/davidvng/repos/project-curvature/chains')
roots = []
roots.append('lcdm_highTE+lowEE')
roots.append('lcdm_highTT+lowEE')
roots.append('lcdm_highTTTEEE+lowEE')
xparams = ['omega_b', 'omega_cdm', 'theta_s_1e2', 'tau_reio', 'n_s', 'logA']
yparams = ['H0', 'Omega_m', 'sigma8']
g.rectangle_plot(xparams, yparams, roots=roots, filled=True)
g.export('planck_lcdm_3combined.pdf')
