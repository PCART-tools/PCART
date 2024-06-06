from loguru import logger
logger.add(sink='error.log', filter=None, diagnose=True)
