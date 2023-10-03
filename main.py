import time
from monitoring.config_loader import ConfigLoader
from monitoring.custom_rules import CustomRuleEngine
from monitoring.logging_module import setup_logging, log_check_result
from monitoring.website_checker import WebsiteChecker


def main():
    config_loader = ConfigLoader()
    config = config_loader.load_config()

    website_checker = WebsiteChecker(config)
    custom_rule_engine = CustomRuleEngine(config)

    log_file = 'monitoring.log'
    setup_logging(log_file)

    i = 0
    while True:
        if i < 2:
            for website in config['websites']:
                check_type = website['check']
                if check_type == 'status_code':
                    result = website_checker.check_status_code(website)
                elif check_type == 'login':
                    result = custom_rule_engine.check_login(website)

                log_check_result(website, check_type, result)
            i += 1
        else:
            break

        # time.sleep(10)


if __name__ == '__main__':
    main()

