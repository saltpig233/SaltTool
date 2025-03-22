import json
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)
if config["use_path"]:
    PATH = config['test_path2']
else:
    PATH = ""
VERSON = config['version']
LAST_UPDATE = config['last_update']
UPDATE_TIME = config['update_time']
