"""
logger.py
logging information / Process of recording, what your program is doing while running. [diary]
create folder = keep all your logging data

advantages/uses:
Tracing, filtering the importance, data changes, errors, one file, it supports large data, display in console
save log information
"""

import logging  # inbuilt logging module (logger,handler,formatter,log levels)
import os # create folder, join paths, locate files
from logging.handlers import RotatingFileHandler # special file handler, creates the new logger file when it's reaches the max of data

def get_logger(name=__name__):
    logger = logging.getLogger(name) # creating a logger object

    if not logger.handlers: # helps to keep single data
        logger.setLevel(logging.DEBUG) # setting the log level
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # setting the path root
        log_dir = os.path.join(project_root,"logs")
        os.makedirs(log_dir,exist_ok=True)
        log_file_path = os.path.join(log_dir,"test_log.log")

    # Handlers
        console_handler = logging.StreamHandler()
        file_handler = RotatingFileHandler(log_file_path, maxBytes=3000000, backupCount=3)

    # Formatter # setting display format
        formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

    # Adding Handlers
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger