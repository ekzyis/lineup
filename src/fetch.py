#!/usr/bin/env python

from rar import fetch_rar_lineup
from hurricane import fetch_hurricane_lineup
from southside import fetch_southside_lineup

def write_bands(bands, out):
  with open(out, 'w') as out_file:
    for band in bands:
      out_file.write("{}\n".format(band))

def read_bands(path):
  bands = []
  with open(path, 'r') as in_file:
    while True:
      line = in_file.readline().strip()
      if not line:
        break
      bands.append(line)
  return bands

def to_lower(arr):
  return [item.lower() for item in arr]

def unique_to(festival, other1, other2):
  return [band for band in festival if band not in other1 and band not in other2]

def compare_lineups(rar, hurricane, southside):
  print("RaR Lineup:")
  print(rar)
  print("{} bands".format(len(rar)))
  print("Hurricane Lineup:")
  print(hurricane)
  print("{} bands".format(len(hurricane)))
  print("Southside Lineup:")
  print(southside)
  print("{} bands".format(len(southside)))
  rar = to_lower(rar)
  hurricane = to_lower(hurricane)
  southside = to_lower(southside)
  unique_to_rar = unique_to(rar, hurricane, southside)
  unique_to_hurricane = unique_to(hurricane, southside, rar)
  unique_to_southside = unique_to(southside, hurricane, rar)
  print("Bands unique to RaR:")
  print(unique_to_rar)
  print("{} bands".format(len(unique_to_rar)))
  print("Bands unique to Hurricane:")
  print(unique_to_hurricane)
  print("{} bands".format(len(unique_to_hurricane)))
  print("Bands unique to Southside:")
  print(unique_to_southside)
  print("{} bands".format(len(unique_to_southside)))
  bands_in_rar_and_hurricane_or_southside = [band for band in rar if band in hurricane or band in southside]
  print("Bands which come to RaR and also to Hurricane or Southside:")
  print(bands_in_rar_and_hurricane_or_southside)
  print("{} bands".format(len(bands_in_rar_and_hurricane_or_southside)))

def evaluate():
  rar_bands = read_bands("rar_bands")
  hurricane_bands = read_bands("hurricane_bands")
  southside_bands = read_bands("southside_bands")
  compare_lineups(rar_bands, hurricane_bands, southside_bands)

def fetch_lineups():
  rar_bands = fetch_rar_lineup()
  write_bands(rar_bands, "rar_bands")

  hurricane_bands = fetch_hurricane_lineup()
  write_bands(hurricane_bands, "hurricane_bands")

  southside_bands = fetch_southside_lineup()
  write_bands(southside_bands, "southside_bands")

if __name__ == "__main__":
  fetch_lineups()
  evaluate()