from pathlib import Path
import yaml


class ConfigLoader:
    def __init__(self):
        self.config_file_path = Path(__file__).resolve().parent.parent / 'config' / 'config.yaml'

    
    def load_config(self):
        with open(self.config_file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config
    

# configs = ConfigLoader().load_config()
# for key, value in configs.items():
#   print(key, ":", value)
        