import logging.config
import yaml
import os

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open('logging_config.yaml', 'rt') as f:
	config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

logger = logging.getLogger(__name__)
logger.warn("Logging Loaded")