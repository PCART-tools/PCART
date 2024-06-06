from loguru import logger
logger.catch(ValueError, level='ERROR', default=None)
