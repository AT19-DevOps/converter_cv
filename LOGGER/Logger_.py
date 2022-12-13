from Singleton import SingletonMeta
import logging
import logging.config

class LoggerManager(metaclass=SingletonMeta):
    
    logging.config.fileConfig("logging.conf")

    def debug(self, message):
        logging.debug(message)
    
    def info(self, message):
        logging.info(message)

    def warning(self, message):
        logging.warning(message)

    def error(self, message):
        logging.error(message)

    def critical(self, message):
        logging.critical(message)