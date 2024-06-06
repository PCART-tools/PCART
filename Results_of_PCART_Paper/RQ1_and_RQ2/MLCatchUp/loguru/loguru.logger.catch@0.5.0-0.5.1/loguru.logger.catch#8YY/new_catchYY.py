from loguru import logger
logger.catch(reraise=False, level='ERROR', onerror=None, default=None)
