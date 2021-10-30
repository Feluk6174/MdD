#_*_coding: utf-8_*_

import requests
import time

r = requests.get("https://minexmr.com/dashboard?address=447QujSc1De9mbXueNH2i5gyu1E3YHgsnC6Potcew6EkQM2Qp8op9xBWBjRZPzVpXy1cEZr8UpgXtFBuuEWBVp2P5cRvCGa", headers={'User-Agent': 'Mozilla/5.0'})

print(r.content)