# system imports
import logging
import sys
from datetime import date
import __main__

# local imports
from constants import FORMATTER, LOGGING_LEVEL


def get_logger(dir, name, level=LOGGING_LEVEL, formatter=FORMATTER):
    # create log name stripping any non-alphanumeric chars
    filename = ''.join(ch for ch in name if ch.isalnum())
    # Create the logger object
    logger = logging.getLogger(name)
    fhdlr = logging.FileHandler('%s/%s-%s.log' % (dir, filename, date.today()))

    # Set the format of the logging
    fhdlr.setFormatter(formatter)
    logger.addHandler(fhdlr)
    # Set the logging level
    logger.setLevel(level)

    return logger


def enable_stdout(logger, formatter=FORMATTER):
    shdlr = logging.StreamHandler(sys.stdout)
    shdlr.setFormatter(formatter)
    logger.addHandler(shdlr)


# Setup automatic logging of uncaught exceptions
def log_uncaught_exception_hook(exc_type, exc_value, exc_traceback):
    # Attempt to attach to the main logger
    logger = logging.getLogger(__main__.__file__ if __main__.__file__ else __name__)
    # Log exception
    logger.error("Uncaught exception", exc_info=(exc_type, exc_value, exc_traceback))
    # Call the original excepthook after we've logged for ourselves.
    sys.__excepthook__(exc_type, exc_value, exc_traceback)
