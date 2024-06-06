from loguru import logger
logger.catch(onerror=None, exception=ValueError, default=None)
