from loguru import logger
logger.add(enqueue=False, filter=None, level='DEBUG', backtrace=True, sink='error.log', colorize=None, serialize=False, format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', diagnose=True)
