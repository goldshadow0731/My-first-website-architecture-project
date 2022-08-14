import logging
from logging.handlers import TimedRotatingFileHandler
import sys
from datetime import date


class Log():
    log_format = "%(asctime)s [%(levelname)-8s] %(name)s:%(lineno)d - %(message)s"

    @classmethod
    def init_log(cls):
        # Format
        formatter = logging.Formatter(cls.log_format)

        # Stream
        stream_handler = logging.StreamHandler(sys.stdout)
        stream_handler.setLevel(logging.DEBUG)
        stream_handler.setFormatter(formatter)

        # File
        file_handler = TimedRotatingFileHandler(
            f'./Log/service_{date.today().strftime("%Y-%m-%d")}.log',
            when="D",
            interval=1,
            backupCount=7)
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(formatter)

        logging.basicConfig(format=cls.log_format,
                            level=logging.INFO,
                            handlers=[stream_handler, file_handler])
