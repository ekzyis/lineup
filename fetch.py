#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup

def fetch_rar_lineup():
  lineup_url = "https://www.rock-am-ring.com/lineup"
  r = requests.get(lineup_url)
  lineup_page = BeautifulSoup(r.text, features="html.parser")
  band_tags = lineup_page.select("div.Appearance > a > h5 > span")
  bands = [tag.string for tag in band_tags]
  return bands

if __name__ == "__main__":
  bands = fetch_rar_lineup()
  print(bands)
