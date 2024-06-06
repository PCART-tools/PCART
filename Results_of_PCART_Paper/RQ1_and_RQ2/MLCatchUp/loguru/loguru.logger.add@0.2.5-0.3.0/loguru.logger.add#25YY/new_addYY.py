from loguru import logger
logger.add(catch=True, sink='error.log', diagnose=True)
