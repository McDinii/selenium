import logging

def setup_logging():
    logging.basicConfig(filename='logs/test_log.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

setup_logging()
