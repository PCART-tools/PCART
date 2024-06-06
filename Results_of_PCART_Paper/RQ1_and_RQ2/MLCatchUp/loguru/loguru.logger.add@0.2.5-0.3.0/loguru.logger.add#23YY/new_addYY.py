from loguru import logger
logger.add(sink='error.log', backtrace=True, diagnose=True)
