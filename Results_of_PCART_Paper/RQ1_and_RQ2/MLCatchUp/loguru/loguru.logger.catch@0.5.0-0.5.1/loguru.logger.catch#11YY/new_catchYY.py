from loguru import logger
logger.catch(ValueError, default=None)
