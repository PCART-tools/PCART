from loguru import logger
logger.catch(level='ERROR', exception=ValueError, default=None)
