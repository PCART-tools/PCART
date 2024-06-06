from loguru import logger
logger.catch(level='ERROR', reraise=False, exclude=None, exception=ValueError, onerror=None, default=None)
