from loguru import logger
logger.add(format='<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>', filter=None, serialize=False, backtrace=True, catch=True, colorize=None, enqueue=False, sink='error.log', level='DEBUG', diagnose=True)
