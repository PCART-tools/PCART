from loguru import logger
logger.catch(ValueError, reraise=False, level='ERROR', onerror=None, exclude=None)
