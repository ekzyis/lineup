import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def get_bands_from_page(page):
  soup = BeautifulSoup(page, features="html.parser")
  band_tags = soup.select("a[routerLinkActive]")
  bands = [tag["href"].replace("#/artist/", "").replace("-", " ") for tag in band_tags]
  return bands

def fetch_southside_lineup():
  lineup_url = "https://www.southside.de/de/line-up/#/artists/alphabetical"
  browser = webdriver.Firefox()
  browser.get(lineup_url)
  # scroll down until no new bands are lazily loaded
  old_bands = []
  while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(10)
    bands = get_bands_from_page(browser.page_source)
    if len(old_bands) == len(bands):
      break
    old_bands = bands
  browser.close()
  return bands
