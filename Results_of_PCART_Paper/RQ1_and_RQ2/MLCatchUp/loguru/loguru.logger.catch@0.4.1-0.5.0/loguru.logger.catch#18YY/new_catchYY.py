from loguru import logger
logger.catch(reraise=False, message='An exception occurred!', exception=ValueError, level='ERROR', onerror=None, exclude=None)
