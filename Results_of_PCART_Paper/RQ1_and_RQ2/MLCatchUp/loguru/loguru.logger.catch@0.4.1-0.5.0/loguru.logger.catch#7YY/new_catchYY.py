from loguru import logger
logger.catch(ValueError, onerror=None, exclude=None)
