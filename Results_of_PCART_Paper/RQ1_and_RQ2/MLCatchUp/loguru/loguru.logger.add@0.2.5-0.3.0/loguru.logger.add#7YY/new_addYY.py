from loguru import logger
logger.add('error.log', backtrace=True, diagnose=True)
