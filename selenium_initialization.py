import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem



def initialize_selenium():

    options = ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')

    options.add_argument('--window-size=1980,1080')

    if int(os.environ.get('SELENIUM_IS_HEADLESS', '0')) == 1:
        options.add_argument('--headless')

    software_names = [SoftwareName.CHROME.value]
    operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]
    user_agent_rotator = UserAgent(software_names=software_names,
                                operating_systems=operating_systems,
                                limit=100)
    user_agent = user_agent_rotator.get_random_user_agent()

    options.add_argument(f"user-agent={user_agent})")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(options=options)

    if os.environ.get('SELENIUM_IS_HEADLESS') == 1:
        driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
            "source": "Object.defineProperty(navigator, 'plugins', {get: () => [5, 3, 9, 2, 1, 8, 4]});"
        })

    driver.set_page_load_timeout(int(os.environ.get('SELENIUM_MAX_TIMEOUT', 120)))
    return driver
