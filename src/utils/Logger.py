import sys, logging, traceback

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logging.basicConfig(format='%(levelname)s : %(asctime)s : %(name)s')

class Logger(object):

  @staticmethod
  def setLevel(level):
    loggingLevel = getattr(logging, level, None)
    if not isinstance(loggingLevel, int):
      raise ValueError('Invalid log level: %s' % level)
    logger.setLevel(loggingLevel)

  @staticmethod
  def info(msg):
    logger.info(msg)

  @staticmethod
  def warning(msg):
    logger.warning(msg)

  @staticmethod
  def error(msg):
    logger.error(msg)
