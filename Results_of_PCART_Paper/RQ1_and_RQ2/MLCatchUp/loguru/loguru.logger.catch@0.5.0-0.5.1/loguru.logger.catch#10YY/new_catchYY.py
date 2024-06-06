from loguru import logger
logger.catch(exclude=None, message='An exception occurred!', onerror=None, level='ERROR', reraise=False, default=None)
