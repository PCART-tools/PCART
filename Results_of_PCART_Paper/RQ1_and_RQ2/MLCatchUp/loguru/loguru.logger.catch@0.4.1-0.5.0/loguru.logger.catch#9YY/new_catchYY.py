from loguru import logger
logger.catch(ValueError, reraise=False, onerror=None, exclude=None)
