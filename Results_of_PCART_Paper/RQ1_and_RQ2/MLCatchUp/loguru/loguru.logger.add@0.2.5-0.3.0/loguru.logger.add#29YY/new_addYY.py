from loguru import logger
logger.add(filter=None, serialize=False, format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', level='DEBUG', sink='error.log', colorize=None, diagnose=True)
