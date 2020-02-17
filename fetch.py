#!/usr/bin/env python

from rar import fetch_rar_lineup

def write_bands(bands, out):
  with open(out, 'w') as out_file:
    for band in bands:
      out_file.write("{}\n".format(band))

if __name__ == "__main__":
  rar_bands = fetch_rar_lineup()
  write_bands(rar_bands, "rar_bands")
