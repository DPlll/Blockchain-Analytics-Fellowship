# This module configures the logger
import logging 
import colorlog

# Sets up and configures the logger to output to both a file and the terminal with colors.
def configure_logger(log_file='logs/crypto_analysis.log', log_level=logging.INFO):

     # Create a logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # Remove any existing handlers to avoid duplication
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler for logging to a file
    file_handler = logging.FileHandler(log_file, mode='a') # "a" == Append mode, "w" == ovewrite mode
    file_handler.setLevel(log_level) # Set the log level of the file handler
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s') # Set the format of the log messages
    file_handler.setFormatter(file_formatter) # Set the formatter of the file handler to the formatter created above

    # Console handler for colored output
    console_handler = colorlog.StreamHandler() # Create a colored console handler
    console_handler.setLevel(log_level) 
    console_formatter = colorlog.ColoredFormatter(
        '%(asctime)s - %(bold)s%(log_color)s%(levelname)s%(reset)s - %(white)s%(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    console_handler.setFormatter(console_formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler) 
    logger.addHandler(console_handler)

    return logger
