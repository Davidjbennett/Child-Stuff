import requests
import time
from multiprocessing import cpu_count

# Download a Powerpoint file
# resp = requests.get("http://chuckallison.com/cs3240/Chapter%2010.pptx", headers={"User-Agent": "XY"})
# with open("ch10.pptx","wb") as f:
#     f.write(resp.content)
#The above doesnt work.

# Download a flag from the CIA
# prefix = 'https://www.cia.gov/library/publications/resources/the-world-factbook/graphics/flags/large/'
# fname = prefix + "us-lgflag.gif"
# flag = requests.get(fname).content      # Note: No headers={...}
# with open("us.gif","wb") as f:
#     f.write(flag)


# pic = requests.get('https://iso.500px.com/wp-content/uploads/2016/02/stock-photo-141823007-1500x1000.jpg').content
# with open('rand_pic.jpg', 'wb') as f:
#     f.write(pic)
#Some Practice Code





