# app/utils/logger.py

import os
import sys
from logging.handlers import RotatingFileHandler

from loguru import logger

# ------------------------------------------------------------------------------
# GET LOGGER INSTANCE
# ------------------------------------------------------------------------------

def get_logger(name: str = __name__):
    """
    Return bound logger instance

    Usage:
        logger = get_logger(__name__)
        logger.info("Application started")
    """

    return logger.bind(module=name)

# ------------------------------------------------------------------------------
# LOG DIRECTORY
# ------------------------------------------------------------------------------

LOG_DIR = "logs"

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# ------------------------------------------------------------------------------
# REMOVE DEFAULT LOGGER
# ------------------------------------------------------------------------------

logger.remove()

# ------------------------------------------------------------------------------
# CONSOLE LOGGER
# ------------------------------------------------------------------------------

logger.add(
    sys.stdout,
    level="INFO",
    colorize=True,
    format=(
        "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
        "<level>{level: <8}</level> | "
        "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
        "<level>{message}</level>"
    )
)

# ------------------------------------------------------------------------------
# INFO FILE LOGGER
# ------------------------------------------------------------------------------

logger.add(
    f"{LOG_DIR}/application.log",
    rotation="10 MB",
    retention="30 days",
    compression="zip",
    level="INFO",
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level: <8} | "
        "{name}:{function}:{line} | "
        "{message}"
    )
)

# ------------------------------------------------------------------------------
# ERROR FILE LOGGER
# ------------------------------------------------------------------------------

logger.add(
    f"{LOG_DIR}/error.log",
    rotation="5 MB",
    retention="60 days",
    compression="zip",
    level="ERROR",
    enqueue=True,
    backtrace=True,
    diagnose=True,
    format=(
        "{time:YYYY-MM-DD HH:mm:ss} | "
        "{level: <8} | "
        "{name}:{function}:{line} | "
        "{message}"
    )
)

# ------------------------------------------------------------------------------
# LOGGER CLASS
# ------------------------------------------------------------------------------

class LoggerManager:

    @staticmethod
    def info(message: str):
        logger.info(message)

    @staticmethod
    def warning(message: str):
        logger.warning(message)

    @staticmethod
    def error(message: str):
        logger.error(message)

    @staticmethod
    def debug(message: str):
        logger.debug(message)

    @staticmethod
    def critical(message: str):
        logger.critical(message)


# ------------------------------------------------------------------------------
# SAMPLE USAGE
# ------------------------------------------------------------------------------

if __name__ == "__main__":

    LoggerManager.info("Application started")
    LoggerManager.debug("Debugging application")
    LoggerManager.warning("Warning message")
    LoggerManager.error("Error occurred")
    LoggerManager.critical("Critical issue")