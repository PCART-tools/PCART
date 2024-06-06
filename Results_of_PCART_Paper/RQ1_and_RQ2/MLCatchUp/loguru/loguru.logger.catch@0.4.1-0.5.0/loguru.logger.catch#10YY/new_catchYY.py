from loguru import logger
logger.catch(ValueError, message='An exception occurred!', onerror=None, exclude=None)
