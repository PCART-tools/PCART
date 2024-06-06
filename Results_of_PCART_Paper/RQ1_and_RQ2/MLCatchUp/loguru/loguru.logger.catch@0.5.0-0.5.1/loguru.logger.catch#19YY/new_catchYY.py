from loguru import logger
logger.catch(ValueError, level='ERROR', onerror=None, reraise=False, exclude=None, default=None)
