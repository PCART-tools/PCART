from loguru import logger
logger.catch(ValueError, reraise=False, message='An exception occurred!', level='ERROR', onerror=None, exclude=None)
