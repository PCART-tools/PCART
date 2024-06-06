from loguru import logger
logger.catch(message='An exception occurred!', onerror=None, exclude=None)
