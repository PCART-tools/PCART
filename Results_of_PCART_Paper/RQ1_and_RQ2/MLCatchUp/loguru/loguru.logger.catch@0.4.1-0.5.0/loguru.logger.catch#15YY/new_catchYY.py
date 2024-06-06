from loguru import logger
logger.catch(exception=ValueError, reraise=False, onerror=None, exclude=None)
