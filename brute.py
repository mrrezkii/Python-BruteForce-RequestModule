import requests
import os

for i in range(5000, 6000):
    x = requests.get("https://web.ctf.rasyidmf.com/chal10/", params={"no" : i})
    flag = os.system("echo '{}' >> hasil.txt".format(x.text))
