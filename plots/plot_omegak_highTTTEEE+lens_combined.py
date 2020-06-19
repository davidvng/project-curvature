from getdist import plots

analysis_settings = {'ignore_rows': '0.1'}
g=plots.get_single_plotter(chain_dir=r'/home1/davidvng/repos/project-curvature/chains',analysis_settings=analysis_settings)
roots = ['omegak_lowEE+lowTT+highTTTEEE_lite', 'omegak_lowEE+lowTT+highTTTEEE+lens']
pairs = [['H0', 'Omega_k']]
g.plots_2d(roots, param_pairs=pairs, filled=True, shaded=False)
g.export('omegak_highTTTEEE+lens_combined.pdf')
