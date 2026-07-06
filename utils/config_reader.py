import yaml
import os

class ConfigReader:

    @staticmethod
    def read_config():
        config_path = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "config",
            "config.yaml"
        )
        # work with different os (windows, linux,macOS)

        with open(config_path,'r') as file: # file handling
            return yaml.safe_load(file)