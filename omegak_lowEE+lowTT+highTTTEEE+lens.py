from cobaya.yaml import yaml_load_file

info_from_yaml = yaml_load_file("flat_omegak.yaml")

from cobaya.run import run

updated_info, sampler = run(info_from_yaml)
