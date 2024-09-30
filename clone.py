import os
import yaml

default_clone_cmd = 'git clone'

with open('config.yaml', 'r') as repo_config:
    config = yaml.safe_load(repo_config)

working_dir = input(f"Working directory set to: {config['working_directory']}, is this correct? [y/N]")
if (working_dir == 'N'):
    working_dir = input(f'Please type in working directory: ')
else:
    working_dir = config['working_directory']

base_url = input(f"Base URL is set to: {config['base_url']}, is this correct? [y/N]")
if (base_url == 'N'):
    base_url = input(f'Please enter base URL for repository: ')
else:
    base_url = config['base_url']

os.system('cd ' + working_dir)
for repo in config['repos']:
    print(f'Cloning {repo} from {base_url}/{repo} ..')
    # os.system(f'{default_clone_cmd} {base_url}/{repo}')