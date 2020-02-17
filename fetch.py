#!/usr/bin/env python

from rar import fetch_rar_lineup

if __name__ == "__main__":
  bands = fetch_rar_lineup()
  print(bands)
