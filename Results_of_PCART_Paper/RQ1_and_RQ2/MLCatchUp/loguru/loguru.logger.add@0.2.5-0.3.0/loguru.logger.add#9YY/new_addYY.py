from loguru import logger
logger.add('error.log', catch=True, diagnose=True)
