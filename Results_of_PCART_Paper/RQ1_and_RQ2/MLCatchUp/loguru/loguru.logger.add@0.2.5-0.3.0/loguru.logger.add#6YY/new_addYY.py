from loguru import logger
logger.add('error.log', serialize=False, diagnose=True)
