import logging
from colorlog import ColoredFormatter

def setup_logging():
    # Define a colored formatter with your specified format and colors
    formatter = ColoredFormatter(
        "%(log_color)s%(asctime)s - %(levelname)s - %(message)s%(reset)s",
        log_colors={
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red,bg_white',
        }
    )

    # Create a console handler and set the formatter
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Configure the root logger
    logging.basicConfig(
        level=logging.DEBUG,    # Set the default log level to DEBUG
        handlers=[console_handler]  # Only the colored console handler
    )

def get_logger():
    """Returns the configured logger instance."""
    return logging.getLogger(__name__)

# Initialize logging when this file is imported
setup_logging()