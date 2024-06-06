from loguru import logger
logger.catch(ValueError, onerror=None, default=None)
