from logging import INFO, getLogger


def create_logger(name, log_level: str = INFO):
    logger = getLogger(name)
    logger.setLevel(log_level)
    return logger
