from loguru import logger
logger.catch(reraise=False, default=None)
