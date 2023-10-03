import requests
# from config_loader import ConfigLoader


class CustomRuleEngine:
    def __init__(self, config):
        self.config = config
        self.session = requests.Session()

    def check_login(self, website):
        url = website['url']
        username = website['credentials']['username']
        password = website['credentials']['password']
        expected_status = website['expected']
        # Simulate a login POST request with login credentials
        response = self.session.post(url, data={'username': username, 'password': password})
        if response.status_code == 200:
            # Check for expected content indicating successful login
            
            if expected_status in response.text:
                return f"Login successful for {url}, 'Response-Text:' {response.text}"
            else:
                return f"Returned 200 status code but login attempt for {url} failed or indication not found,  'Response-Text:' {response.text}"
        else:
            return f"Failed to access {url} (Status code: {response.status_code}),  'Response-Text:' {response.text}"




# config = ConfigLoader().load_config()
# custom_rule_engine = CustomRuleEngine(config)
# print(custom_rule_engine.check_login(config['websites'][1]))