import beepy
from datetime import datetime, timedelta
import os
import time
from selenium.webdriver.common.by import By

from selenium_initialization import initialize_selenium



PARIS_APPOINTMENT_URL = "https://teleservices.paris.fr/rdvtitres/jsp/site/Portal.jsp?page=appointmentsearch&category=titres"


def main():
    driver = initialize_selenium()
    driver.get(PARIS_APPOINTMENT_URL)
    time.sleep(2)

    # Username
    username_input = driver.find_element(By.XPATH, "//input[@id='username']")
    username_input.clear()
    username_input.send_keys(os.environ.get('USERNAME'))

    # Password
    password_input = driver.find_element(By.XPATH, "//input[@id='password']")
    password_input.clear()
    password_input.send_keys(os.environ.get('PASSWORD'))

    button = driver.find_element(By.XPATH, "//form[@id='form-login']//button[@type='submit']")
    button.click()

    time.sleep(2)

    # Limit Date
    from_date_input = driver.find_element(By.XPATH, "//form[@name='search']//input[@id='from_date']")
    from_date_input.clear()
    from_date_input.send_keys(datetime.now().strftime("%d/%m/%Y"))
    driver.execute_script("document.getElementById('ui-datepicker-div').style.display = 'none';")
    time.sleep(3)

    to_date_input = driver.find_element(By.XPATH, "//form[@name='search']//input[@id='to_date']")
    print(to_date_input)
    to_date_input.clear()
    print((datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y"))
    to_date_input.send_keys(os.environ.get('DATE_LIMIT'), (datetime.now() + timedelta(days=30)).strftime("%d/%m/%Y"))
    driver.execute_script("document.getElementById('ui-datepicker-div').style.display = 'none';")

    print("Monitoring en cours")

    while True:
        button = driver.find_element(By.XPATH, "//form[@name='search']//button[@type='submit']")
        button.click()
        time.sleep(5)
        no_rendez_vous_elems = driver.find_elements(By.XPATH, "//h3[@class='text-warning' and contains(text(),'Aucun rendez-vous')]")
        if len(no_rendez_vous_elems) == 1:
            print('Aucun rendez-vous')
            continue
        print('RENDEZ-VOUS TROUVE')
        beepy.beep(sound="ping")
        time.sleep(50)


if __name__ == '__main__':
    main()
