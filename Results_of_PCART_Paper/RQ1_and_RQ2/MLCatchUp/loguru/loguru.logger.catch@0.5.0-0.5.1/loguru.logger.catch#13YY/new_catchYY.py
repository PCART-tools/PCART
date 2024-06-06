from loguru import logger
logger.catch(ValueError, reraise=False, default=None)
