import requests
import re
from bs4 import BeautifulSoup

response = requests.get("https://adventofcode.com/2020/day/1", cookies={"session": ''})
with open("response.html", "w") as f:
    f.write(response.text)
with open("response.html", "r") as f:
    soup = BeautifulSoup(f.read(), "html.parser")
    with open("main.html", "w") as r:
        main = str(soup.main)
        main = re.sub(r"<a href=[^>]*>", "", main)
        main = re.sub("</a>", "", main)
        main = re.sub("<p>You can also(.|\s)*", "", main)
        r.write(main + "</main>")