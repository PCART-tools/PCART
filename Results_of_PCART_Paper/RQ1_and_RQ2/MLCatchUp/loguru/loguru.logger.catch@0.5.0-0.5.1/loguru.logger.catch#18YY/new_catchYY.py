from loguru import logger
logger.catch(ValueError, level='ERROR', reraise=False, onerror=None, default=None)
