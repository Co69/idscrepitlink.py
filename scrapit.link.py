import requests
import re
#tkaya lera link dabne 

url = input("type links : ")

html = requests.get(url).text 

links = re.findall('"(https?://.*?)"', html)

for link in links:
    print(link)

#DONE