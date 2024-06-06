from loguru import logger
logger.catch(exception=ValueError, level='ERROR', reraise=False, default=None)
