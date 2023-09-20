import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Reviews = []

for i in range(2,14):
    url="https://www.flipkart.com/search?q=mobiles+under+50000rs&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r = requests.get(url)
    #print(r)

    soup = BeautifulSoup(r.text,"lxml")
    box = soup.find("div",class_= "_1YokD2 _3Mn1Gg")
    #print(soup)

    names = box.find_all("div",class_ ="_4rR01T" )
    for i in names:
        name = i.text
        Product_name.append(name)

    #print(Product_name)

    prices = box.find_all("div",class_ ="_30jeq3 _1_WHN1" )
    for i in prices:
        name = i.text
        Prices.append(name)

    #print(Prices)

    desc = box.find_all("ul",class_="_1xgFaf")
    for i in desc:
        name = i.text
        Description.append(name)

    #print(Description)

    reviews = box.find_all("div",class_="_3LWZlK")
    for i in reviews:
        name = i.text
        Reviews.append(name)

    #print(len(Reviews))


def pad_dict_list(dict_list, padel):
    lmax = 0
    for lname in dict_list.keys():
        lmax = max(lmax, len(dict_list[lname]))
    for lname in dict_list.keys():
        ll = len(dict_list[lname])
        if  ll < lmax:
            dict_list[lname] += [padel] * (lmax - ll)
    return dict_list


dict_list = {"Product Name":Product_name,"Prices":Prices,"Description":Description,"Reviews":Reviews}
dict_list = pad_dict_list(dict_list, 0)
#print(dict_list)

df = pd.DataFrame(dict_list)
#print(df)

df.to_csv("Flipkart_mobile Dataset.csv")





















#np = soup.find("a",class_ = "_1LKTO3").get("href")
#cnp = "https://www.flipkart.com" + np
#print(cnp)
