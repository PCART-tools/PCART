from loguru import logger
logger.catch(reraise=False, level='ERROR', exclude=None, message='An exception occurred!', exception=ValueError, onerror=None, default=None)
