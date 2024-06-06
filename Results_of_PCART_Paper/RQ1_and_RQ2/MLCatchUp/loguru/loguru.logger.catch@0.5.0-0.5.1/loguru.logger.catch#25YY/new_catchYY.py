from loguru import logger
logger.catch(exception=ValueError, exclude=None, default=None)
