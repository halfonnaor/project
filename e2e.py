from selenium import webdriver
from selenium.webdriver.common.by import By


class e2e:
    def __init__(self):
        self.difficulty = 0

    def test_scores_service(self, url):
        options = webdriver.Chrome('./chromedriver')
        options.headless = True
        url = 'http://127.0.0.1:30001/'
        options.get(url)
        options.set_page_load_timeout(45)
        a = options.find_element(By.XPATH, '//*[@id="score"]').text
        options.quit()
        if 1 <= int(a) <= 1000:
            return True
        else:
            return False

    def main_function(self):
        app_url = "http://127.0.0.1:30001/"
        test_func = self.test_scores_service(app_url)
        if not test_func:
            return -1
        else:
            return 0


if __name__ == "__main__":
    print(e2e().main_function())