from loguru import logger
logger.catch(exception=ValueError, onerror=None, exclude=None)
