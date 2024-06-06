from loguru import logger
logger.catch(exception=ValueError, reraise=False, default=None)
