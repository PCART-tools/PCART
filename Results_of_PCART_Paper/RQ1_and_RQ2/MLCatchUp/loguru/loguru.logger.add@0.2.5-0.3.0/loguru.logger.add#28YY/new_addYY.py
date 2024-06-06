from loguru import logger
logger.add(filter=None, sink='error.log', format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', colorize=None, level='DEBUG', diagnose=True)
