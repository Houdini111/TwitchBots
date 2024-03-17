import logging
from typing import Self
from twitchio.ext import commands
from traceback import format_exc
import LoggingConfig

logger = logging.getLogger(__name__)

class CustomizedBot(commands.Bot):
	pass
	
	#TODO:
	# Metadata:
	#   Creator contact info
	# Creator command (!creator, !contact)
	# Default data as json config file
	# Use SecretStorage
