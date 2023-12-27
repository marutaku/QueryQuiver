from logging import INFO, StreamHandler, getLogger


def create_logger(name, log_level: int = INFO):
    logger = getLogger(name)
    logger.setLevel(log_level)
    stream_handler = StreamHandler()
    stream_handler.setLevel(log_level)
    logger.addHandler(stream_handler)
    return logger
