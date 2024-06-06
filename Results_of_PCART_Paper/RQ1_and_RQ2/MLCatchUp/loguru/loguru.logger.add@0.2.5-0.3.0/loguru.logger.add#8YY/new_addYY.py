from loguru import logger
logger.add('error.log', enqueue=False, diagnose=True)
