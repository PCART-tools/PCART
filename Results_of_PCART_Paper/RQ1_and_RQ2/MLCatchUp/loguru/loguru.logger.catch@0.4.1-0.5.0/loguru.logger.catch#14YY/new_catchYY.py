from loguru import logger
logger.catch(level='ERROR', exception=ValueError, onerror=None, exclude=None)
