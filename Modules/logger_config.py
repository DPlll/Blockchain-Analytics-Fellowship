
import logging
import colorlog

# Sets up and configures the logger to output to both a file and the terminal with colors.
def configure_logger(log_file='crypto_analysis.log', log_level=logging.INFO):
    
    # Create a logger
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # Remove any existing handlers to avoid duplication
    if logger.hasHandlers():
        logger.handlers.clear()
    
    # Create a file handler for logging to a file
    file_handler = logging.FileHandler(log_file, mode='w')
    file_handler.setLevel(log_level)
    
    # Create a console handler for colored output to the terminal
    console_handler = colorlog.StreamHandler()
    console_handler.setLevel(log_level)
    
    # Define the log format for file and console
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_formatter = colorlog.ColoredFormatter(
        '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Set the format for both handlers
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)
    
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

