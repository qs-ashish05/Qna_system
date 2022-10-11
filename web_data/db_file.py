from fastapi import FastAPI, Query
from fastapi import Response,status,HTTPException
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from bs4 import BeautifulSoup
import requests
# print("dependencies addd")

# url 
#url = "https://dl.acm.org/doi/abs/10.1145/1353535.1346295"

# instance of FastAPI
app = FastAPI()

# connecting to a database
while True:
    try:
        conn = psycopg2.connect(host = 'localhost',database='QnA project',user='postgres',password='Ashu123',cursor_factory=RealDictCursor)
        cursor = conn.cursor() 
        print('Databse connection was succesfull')
        break

    except Exception as error:
        print('Connecting to Database failed')
        print('Error : ',error)
        time.sleep(3)          # if connection failed then before reconnection wait for 3 second



# for testing purpose
@app.get('/')
async def root():
    return{"Meessage":"Hello world"}

@app.get('/url')
async def Data(url):
    response=requests.get("https://dl.acm.org/doi/abs/10.1145/1353535.1346295")
    data=response.text
    soup=BeautifulSoup(data,"html.parser")

    for data in soup(['style', 'script']):    
        data.decompose()
    text_data=' '.join(soup.stripped_strings)
    return{"Useful content":text_data}

   