"""
EDA_DOLPHIN - Comprehensive Exploratory Data Analysis Toolkit
"""

from .components.missing import (
    check_missing, 
    print_missing_summary, 
    quick_missing_report, 
    safe_check_missing
)

from .logger import logger, setup_logger
__version__ = "0.1.0"
__author__ = "Sahil Kumar"
__email__ = "sahilkumar1851320@gmal.com"

__all__ = [
    'check_missing',
    'print_missing_summary',
    'quick_missing_report',
    'safe_check_missing'
]