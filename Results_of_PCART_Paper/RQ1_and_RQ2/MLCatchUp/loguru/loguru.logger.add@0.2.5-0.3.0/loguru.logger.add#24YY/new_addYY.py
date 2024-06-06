from loguru import logger
logger.add(sink='error.log', enqueue=False, diagnose=True)
