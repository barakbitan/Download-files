import urllib.request
import gzip
import shutil
from datetime import date

today = date.today()
# mmyydd
d1 = today.strftime("%Y%m%d")

#אתר להורדת המידע עבור מחסני השוק וויקטורי:
#http://matrixcatalog.co.il/NBCompetitionRegulations.aspx
#מחסני השוק
url_mck = 'http://matrixcatalog.co.il/CompetitionRegulationsFiles/latest/7290661400001/PriceFull7290661400001-097-'+d1+'0359-001.xml.gz'
#ויקטורי
url_victory = 'http://matrixcatalog.co.il/CompetitionRegulationsFiles/latest/7290696200003/PriceFull7290696200003-097-'+d1+'0320-001.xml.gz'

def downloadFile(url,name):
    file_name = "C:\\prices\\"+name+"\\"+name+'_'+d1+".xml.gz"
    file_name_finel = "C:\\prices\\"+name+"\\"+name+'_'+d1+".xml"
    urllib.request.urlretrieve(url, file_name)
    decompressFile(file_name,file_name_finel)

def decompressFile(file_name,file_name_finel):
    with gzip.open(file_name, 'rb') as f_in:
        with open(file_name_finel, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)

downloadFile(url_mck,'mck')
downloadFile(url_victory,'victory')
