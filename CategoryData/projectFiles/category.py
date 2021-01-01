import pandas as pd
import requests
from bs4 import BeautifulSoup

df1 = pd.read_excel(r'BD_App_List.xlsx')
bundle_names = df1['app'].tolist()


url = 'https://play.google.com/store/apps/details?id='
urls = []

for bundle_name in bundle_names:
    urls.append(url+str(bundle_name))

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        h1 = soup.find("a", class_="hrTbp R8zArc").find_next("a", class_="hrTbp R8zArc").text
    except:
        pass

    # h1 = soup.find("span", class_ ="T32cc UAO9ie")
    # h1 = soup.find("div", class_="qQKdcc")

    print(h1)

