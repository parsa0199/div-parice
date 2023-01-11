import time
import requests
from bs4 import BeautifulSoup
import lxml
from unidecode import unidecode


# sum=0
# sum2=0
uc = unidecode("۰۱۲۳۴۵۶۷۸۹")
cites = [
    'borujerd','azarshahr', 'ahar', 'bonab', 'tabriz',"tehran"
]
base_url = 'https://divar.ir'
index = 0
for c in cites:
    sum=0
    sum2=0
    city = cites[index]
    index += 1
    url = f'https://divar.ir/s/{city}/buy-apartment'
    html_text = requests.get(url).text
    soup=BeautifulSoup(html_text,'lxml')

    items=soup.find_all('div',class_="post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46")
    for item in items:
        for link in item.find_all("a"):

            links=link['href']
            full_link=f'{base_url}{links}'
            html_of_ads = requests.get(full_link).text
            soup2 = BeautifulSoup(html_of_ads, 'lxml')
            detail_boxes = soup2.find_all('div', class_='kt-base-row__start kt-unexpandable-row__title-box')
            for detail_box in detail_boxes:
                
                for atr in detail_box.find_all('p'):
                    title=atr.text
                    if title == "قیمت هر متر":
                        full_title=atr.find_next(name=None).text
                        price=full_title.split(' ')
                        clean_price=price[0]
                        eng_price=unidecode(clean_price)
                        intprice=eng_price.replace(',', '')
                        integerPrice=int(intprice)
                        sum =sum+ integerPrice
                        sum2=sum2+1

                    # print(sum/sum2)
                    # print("-------")
                    # print(sum)
                    # print("-------")
                    # print(sum2)
                        print(f'the avg of {city} in {sum2} ads is : {sum/sum2} toman')
                    
                        # break
            time.sleep(0.7)
    print(f'the avg of {city} in {sum2} ads isssssssssss : {sum/sum2}')
print("---------------------")
print(sum)
print("-------")
print(sum2)
        
        

# linkss = soup.find_all('a', {'herf': re.compile('^v\d+')})
