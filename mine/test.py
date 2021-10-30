import requests

r = requests.get("https://minexmr.com/dashboard?address=447QujSc1De9mbXueNH2i5gyu1E3YHgsnC6Potcew6EkQM2Qp8op9xBWBjRZPzVpXy1cEZr8UpgXtFBuuEWBVp2P5cRvCGa")

print(r)

temp = r.text

with open("web.hrml", "w") as f:
    f.write(temp)

print(temp)

temp = temp.split('<tbody class="table-click" id="off-workers" title="click for more details">')

for i in temp:
    #print(i)
    print("")
    print("")

print("")

total_values = temp[1].split("</tbody>")

total_values = total_values[0]

print(total_values)

