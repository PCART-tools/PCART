from loguru import logger
logger.add(sink='error.log', filter=None, level='DEBUG', format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', colorize=None, backtrace=True, serialize=False, diagnose=True)
