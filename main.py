import urllib.request
import gzip
import shutil
import requests
import os
from datetime import date
from bs4 import BeautifulSoup

def getSuperSalUrl():
    url = "http://prices.shufersal.co.il/FileObject/UpdateCategory?catID=0&storeId=413"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    links = soup.find_all("a")
    for link in links:
        if "PriceFull" in link["href"]:
            return link["href"]

def downloadFile(url,name):
    file_name = "./downloads/"+name+".xml.gz"
    file_name_finel = "./downloads/"+name+".xml"
    urllib.request.urlretrieve(url, file_name)
    decompressFile(file_name,file_name_finel)

def decompressFile(file_name,file_name_finel):
    with gzip.open(file_name, 'rb') as f_in:
        with open(file_name_finel, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
    os.remove(file_name)

today = date.today()
# mmyydd
d1 = today.strftime("%Y%m%d")

#אתר להורדת המידע עבור מחסני השוק וויקטורי:
#http://matrixcatalog.co.il/NBCompetitionRegulations.aspx
#מחסני השוק
url_mck = 'http://matrixcatalog.co.il/CompetitionRegulationsFiles/latest/7290661400001/PriceFull7290661400001-097-'+d1+'0359-001.xml.gz'
#ויקטורי
url_victory = 'http://matrixcatalog.co.il/CompetitionRegulationsFiles/latest/7290696200003/PriceFull7290696200003-097-'+d1+'0320-001.xml.gz'
#שופרסל
url_supersal = getSuperSalUrl()

downloadFile(url_mck,'mck')
downloadFile(url_victory,'victory')
downloadFile(url_supersal,'supersal')
