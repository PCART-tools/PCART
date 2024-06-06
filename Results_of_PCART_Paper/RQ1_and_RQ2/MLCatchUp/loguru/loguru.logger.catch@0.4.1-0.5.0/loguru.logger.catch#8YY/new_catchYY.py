from loguru import logger
logger.catch(ValueError, level='ERROR', onerror=None, exclude=None)
