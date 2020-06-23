from cobaya.yaml import yaml_load_file

info_from_yaml = yaml_load_file("omegak_lowEE+lowTT+highTT_range.yaml")

from cobaya.run import run

updated_info, sampler = run(info_from_yaml)
