from loguru import logger
logger.add(sink='error.log', level='DEBUG', diagnose=True)
