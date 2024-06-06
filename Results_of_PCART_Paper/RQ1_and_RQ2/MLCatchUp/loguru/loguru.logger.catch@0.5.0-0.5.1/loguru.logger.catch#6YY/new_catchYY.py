from loguru import logger
logger.catch(message='An exception occurred!', default=None)
