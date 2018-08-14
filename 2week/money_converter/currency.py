from bs4 import BeautifulSoup
from decimal import Decimal


def convert(amount, cur_from, cur_to, date, requests):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp?', 
    						params={"date_req":date})  # Использовать переданный requests
    soup = BeautifulSoup(response.content, 'xml')
    value_to = Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Value').string.replace(',','.'))
    nominal_to = Decimal(soup.find('CharCode', text=cur_to).find_next_sibling('Nominal').string)
    
    if cur_from == "RUR":
        value_from = Decimal(1)
        nominal_from = Decimal(1)
    else:
        value_from = Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Value').string.replace(',','.'))
        nominal_from = Decimal(soup.find('CharCode', text=cur_from).find_next_sibling('Nominal').string)
    result = amount * (value_from/nominal_from) * (nominal_to/value_to)

    return result.quantize(Decimal('0.0001'))

