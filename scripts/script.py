from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--disable-extensions")
options.add_argument("--start-maximized")
options.add_argument("--disable-gpu")


driver = webdriver.Chrome(options=options)


def extract_urls(url: str) -> list[str]:
    try:
        driver.get(url)
        link_tags = driver.find_elements(By.CLASS_NAME, "elementor-button")
        href_values = [tag.get_attribute("href") for tag in link_tags]
        
    except Exception as e:
        print(e)
    return href_values
