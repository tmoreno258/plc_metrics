import yaml
from pprint import pprint

with open('plc.settings.yaml', 'r') as cf:
    config_file = yaml.safe_load(cf)
    pprint(config_file)