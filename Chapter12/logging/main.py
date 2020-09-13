import logging


def log():
    logging.debug("Looks like rain")
    logging.info("And hail")
    logging.warning("Did I hear thunder?")
    logging.error("Was that lightning?")
    logging.critical("Stop fencing and get inside!")


def log_with_level():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("It's raining again")
    logging.info("With hail the size of hailstones")


def log_with_object():
    logging.basicConfig(level='DEBUG')
    logger = logging.getLogger('bunyan')
    logger.debug('Timber!')


def log_with_handlers():
    fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'
    logging.basicConfig(level='DEBUG', filename='blue_ox.log', format=fmt)
    logger = logging.getLogger('bunyan')
    logger.debug("Where's my axe?")
    logger.warning("I need my axe")


def main():
    # Logging error messages
    # log()
    # log_with_level()
    # log_with_object()
    log_with_handlers()


if __name__ == '__main__':
    main()
