# src/eda_dolphin/utils/logger.py
import logging
import os

def setup_logger(name=__name__, log_level=logging.INFO):
    """Setup and return a logger instance."""
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    
    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)
    
    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    # Add handler to logger
    logger.addHandler(console_handler)
    
    return logger

# Create a default logger instance
logger = setup_logger('eda_dolphin')