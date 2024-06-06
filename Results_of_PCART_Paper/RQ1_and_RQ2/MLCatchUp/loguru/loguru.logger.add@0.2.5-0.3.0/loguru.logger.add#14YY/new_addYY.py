from loguru import logger
logger.add('error.log', format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', backtrace=True, level='DEBUG', colorize=None, filter=None, serialize=False, diagnose=True)
