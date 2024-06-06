from loguru import logger
logger.catch(exception=ValueError, default=None)
