#!/usr/bin/env python

from rar import fetch_rar_lineup
from hurricane import fetch_hurricane_lineup
from southside import fetch_southside_lineup

def write_bands(bands, out):
  with open(out, 'w') as out_file:
    for band in bands:
      out_file.write("{}\n".format(band))

if __name__ == "__main__":
  rar_bands = fetch_rar_lineup()
  write_bands(rar_bands, "rar_bands")

  hurricane_bands = fetch_hurricane_lineup()
  write_bands(hurricane_bands, "hurricane_bands")

  southside_bands = fetch_southside_lineup()
  write_bands(southside_bands, "southside_bands")