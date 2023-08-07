import logging


class LogGen:
    @staticmethod
    def loggen():
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        file = logging.FileHandler(r'C:\Users\Dell\PycharmProjects\mercury\loggs\logs.log')
        formatter = logging.Formatter('%(message)s : %(asctime)s : %(lineno)s : %(funcName)s')
        file.setFormatter(formatter)
        logger.addHandler(file)
        return logger
