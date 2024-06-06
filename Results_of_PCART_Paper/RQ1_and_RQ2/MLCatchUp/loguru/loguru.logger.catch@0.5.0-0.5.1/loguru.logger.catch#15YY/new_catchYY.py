from loguru import logger
logger.catch(ValueError, exclude=None, default=None)
