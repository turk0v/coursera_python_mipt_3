import requests
from bs4 import BeautifulSoup
from decimal import Decimal
s='02/03/2002'
# resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?date_req={}".format(s))
resp = requests.get("http://www.cbr.ru/scripts/XML_daily.asp?date_req=17/02/2005")
soup=BeautifulSoup(resp.content,"lxml")
# current_from_value=Decimal(soup.find('CharCode',text='AUD').find_parent().find('Value').get_text().replace(',','.'))
# nominal_from_value=int(soup.find("CharCode",text='AUD').find_next_sibling('Nominal').string)
# result=Decimal(current_from_value/nominal_from_value)
# print(current_from_value)
# cur=soup.find('CharCode',text='AUD').find_parent().find('Value').get_text()
cur=Decimal(soup.find("charcode",text='AUD').find_next_sibling('value').get_text().replace(',','.'))
print(cur)


