# local imports
from tools import logger as logging
from tools import args as argparser

# create a new logger, in 	dir		namespace
logger = logging.get_logger("logs", "main.py")

try:
    args = argparser.get_and_check_args()
except ValueError as e:
    logger.error(e)
    exit(1)

if args.output_std:
    logging.enable_stdout(logger)
    logger.info("STD out logging enabled.")

logger.info("Passed arguement check")
logger.debug("Args - %s" % args)
