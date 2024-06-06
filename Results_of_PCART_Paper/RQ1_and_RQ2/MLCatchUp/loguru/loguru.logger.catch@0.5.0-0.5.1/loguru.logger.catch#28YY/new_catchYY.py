from loguru import logger
logger.catch(onerror=None, level='ERROR', reraise=False, exception=ValueError, default=None)
