import requests
# from config_loader import ConfigLoader

class WebsiteChecker:
    def __init__(self, config):
        self.config = config


    def check_status_code(self, website):
        url = website['url']
        expected_code = website['expected']
        response = requests.get(url)
        return response.status_code == expected_code
    

# config = ConfigLoader().load_config()
# checker = WebsiteChecker(config)
# print(checker.check_status_code(config['websites'][0]))