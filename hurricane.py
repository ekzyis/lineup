import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def fetch_hurricane_lineup():
  lineup_url = "https://www.hurricane.de/en/line-up"
  browser = webdriver.Firefox()
  browser.get(lineup_url)
  bands_selector = "a[routerLinkActive]"
  try:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, bands_selector)))
  except TimeoutException:
    print("Lineup elements were not found!")
    browser.close()
    return []
  lineup_page = BeautifulSoup(browser.page_source, features="html.parser")
  band_tags = lineup_page.select("a[routerLinkActive]")
  bands = [tag["href"].replace("#/artist/", "").replace("-", " ") for tag in band_tags]
  browser.close()
  return bands
