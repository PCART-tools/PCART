from loguru import logger
logger.catch(ValueError, message='An exception occurred!', reraise=False, level='ERROR', exclude=None, onerror=None, default=None)
