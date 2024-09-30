import os
import yaml

default_clone_cmd = 'git clone'

with open('config.yaml', 'r') as repo_config:
    config = yaml.safe_load(repo_config)

os.system('cd ' + config['working_directory'])
for repo in config['repos']:
    os.system(f'{default_clone_cmd} {config['base_url']}/{repo}')