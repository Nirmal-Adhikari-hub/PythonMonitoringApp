import logging


def setup_logging(log_file):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )


def log_check_result(website, check_name, result):
    logging.info(f"Check for {website['url']} - {check_name} - {result}")