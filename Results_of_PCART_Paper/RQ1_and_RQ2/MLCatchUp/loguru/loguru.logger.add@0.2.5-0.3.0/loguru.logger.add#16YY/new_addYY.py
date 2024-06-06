from loguru import logger
logger.add('error.log', catch=True, enqueue=False, filter=None, level='DEBUG', backtrace=True, serialize=False, format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', colorize=None, diagnose=True)
