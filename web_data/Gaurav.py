from bs4 import BeautifulSoup
import requests

#response=requests.get("https://dl.acm.org/doi/abs/10.1145/1353535.1346295")
response=requests.get("https://www.nobelprize.org/prizes/themes/the-nobel-call/")
data=response.text
soup=BeautifulSoup(data,"html.parser")

for data in soup(['style', 'script']):    
    data.decompose()
text_data=' '.join(soup.stripped_strings)
print(text_data)