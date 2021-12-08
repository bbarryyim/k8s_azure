import yaml
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s :: %(levelname)s :: %(message)s')

def loadConfigurations():
    os.chdir('/etc/config')
    with open("mainConfiguration.yml","r") as file:
        try:
            config = yaml.safe_load(file)
            return config
        except yaml.YAMLError as exc:
            logging.error(exc)