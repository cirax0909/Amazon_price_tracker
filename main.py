import requests
from bs4 import BeautifulSoup
import lxml

endpoint = "https://www.amazon.ca/Legend-Zelda-Breath-Wild-Switch/dp/B01N33O68B/ref=pd_sbs_sccl_4_6/138-2887960-" \
           "6239104?pd_rd_w=xpPII&content-id=amzn1.sym.6d44cef4-95d9-4421-b5e2-6074721e9da2&pf_rd_p=6d44cef4-95d9-4421-" \
           "b5e2-6074721e9da2&pf_rd_r=6AVMMM001JX4RGTW14YW&pd_rd_wg=L699V&pd_rd_r=c96d0a5d-419d-4b6f-97e5-4b12e45d3a85&" \
           "pd_rd_i=B01N33O68B&psc=1"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63"
                  " Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
TARGET_PRICE = '60'
web = requests.get(url=endpoint, headers=header)
soup = BeautifulSoup(web.content, "lxml")
response = soup.find(name='span', class_='a-offscreen')
price = float(response.text.split('$')[1])
print(price)