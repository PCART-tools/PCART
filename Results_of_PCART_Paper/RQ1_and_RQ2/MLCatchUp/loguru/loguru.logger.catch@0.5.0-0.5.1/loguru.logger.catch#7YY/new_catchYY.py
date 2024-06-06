from loguru import logger
logger.catch(level='ERROR', reraise=False, default=None)
