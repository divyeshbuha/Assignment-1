# import requests
# from bs4 import BeautifulSoup
#
# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'Accept-Language': 'en-US,en;q=0.9,gu;q=0.8',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Origin': 'https://www.gatikwe.com',
#     'Referer': 'https://www.gatikwe.com/',
#     'Sec-Fetch-Dest': 'document',
#     'Sec-Fetch-Mode': 'navigate',
#     'Sec-Fetch-Site': 'same-origin',
#     'Sec-Fetch-User': '?1',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
# }
#
# data = {
#     'status': 'status_docket',
#     'docket_id': '319526214',
# }
# url='https://www.gatikwe.com/OurTrack/DktTrack.php'
# r = requests.post(url, headers=headers, data=data)
# soup=BeautifulSoup(r.content,'html5lib')
# # print(r.content)
# packs=[]
# for table in soup.find_all('table',{'class':'table docket-table'}):
#     tds = table.find_all('td')
#     pack={}
#     pack['Docket No']=tds[0].text
#     pack['Reference No'] =tds[1].text
#     pack['Origin'] =tds[2].text
#     pack['Destination'] =tds[3].text
#     pack['Pickup Date'] =tds[4].text
#     pack['Status'] =tds[5].text
#     packs.append(pack)
# print(packs)
#
# for table2 in soup.find_all('tbody',{'id':'dkt-table-319526214'}):
#     tds2 = table2.find_all('tr')
#     details = []
#     for td in (tds2[1:13]):
#         data=td.find_all('td')
#         detail={}
#         detail['Date']=data[0].text
#         detail['Time'] =data[1].text
#         detail['Location'] =data[2].text
#         detail['Status'] =data[3].text
#         details.append(detail)
# print(details)
from datetime import date

import pymysql
mydb = pymysql.connect(
  host="localhost",
  user="root",
  password="test",
  database="indiarating"
)
mycursor=mydb.cursor()
# sql="CREATE TABLE india_rating_company (id INT AUTO_INCREMENT ,name VARCHAR(200),issuer_id int ,cin VARCHAR(50),history_crawl_flag TINYINT(1) DEFAULT 0,add_date DATETIME,modified DATETIME,UNIQUE(issuer_id)) "
# mycursor.execute(sql)
mydb.commit()
print(date.today())