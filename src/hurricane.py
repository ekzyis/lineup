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

def fetch_hurricane_lineup():
  print("Fetching Hurricane bands...")
  lineup_url = "https://www.hurricane.de/en/line-up#/artists/alphabetical"
  browser = webdriver.Firefox()
  browser.get(lineup_url)
  # scroll down until no new bands are lazily loaded
  old_bands = []
  while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    sleep(10)
    bands = get_bands_from_page(browser.page_source)
    print("Fetched {} bands".format(len(bands)))
    if len(old_bands) == len(bands):
      break
    old_bands = bands
  print("Finished fetching of Hurricane bands.")
  print("Total bands: {}".format(len(bands)))
  browser.close()
  return bands
