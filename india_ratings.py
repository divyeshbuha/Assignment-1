import datetime
import json
import pymysql
import requests
from bs4 import BeautifulSoup
import datetime

class Indiarating(object):

    def __init__(self):
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }

    def search(self):
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                    'u', 'v', 'w', 'x', 'y', 'z']

        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="test",
            database="indiarating"
        )
        cursor = connection.cursor()


        for arg in alphabet:
            params = {
                'searchKey': arg,
                'noOfShowEntry': '0',
            }
            url = 'https://www.indiaratings.co.in/home/GetSearchIssuerData'
            search_page = requests.get(url, params=params, headers=self.headers)
            data = (search_page.json())
            today = datetime.datetime.now()

            for item in data:
                issuer_id = item.get('issuerID')
                name = item.get('name').strip()

                try:
                    in_data="INSERT INTO india_rating_company (name,issuer_id,add_date,modified) VALUES(%s,%s,%s,%s)"
                    in_val=(name,issuer_id,today,today)
                    cursor.execute(in_data,in_val)
                    connection.commit()
                except:
                    pass

    def find_char(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="test",
            database="indiarating"
        )
        cursor = connection.cursor()
        alphabet="SELECT alphabet FROM india_rating_company ORDER BY  modified DESC"
        cursor.execute(alphabet)
        db_com_alph = cursor.fetchone()
        for char in db_com_alph:
            if char == ('',):
                next_char='a'
            else:
                ch = char[0].strip()
                i = ord(ch)
                if (i >= 122):
                    i = 97
                else:
                    i = i + 1
                next_char = chr(i)
            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            }
            params = {
                'searchKey': next_char,
                'noOfShowEntry': '0',
            }
            url = 'https://www.indiaratings.co.in/home/GetSearchIssuerData'
            search_page = requests.get(url, params=params, headers=headers)
            data = (search_page.json())

            today = datetime.datetime.now()
            company_name = "SELECT name FROM india_rating_company"
            cursor.execute(company_name)
            db_com_name = cursor.fetchall()

            name_list = []
            for com_name in db_com_name:
                com_name = com_name[0].strip()
                name_list.append(com_name)

            for item in data:
                issuer_id = item.get('issuerID')
                name = item.get('name').strip()

                if name in name_list:
                        sql="UPDATE india_rating_company SET alphabet=%s, modified=%s WHERE issuer_id=%s"
                        val=(next_char,today,issuer_id)
                        cursor.execute(sql, val)
                        connection.commit()
                else:
                    pass

    def find_detail(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="test",
            database="indiarating"
        )
        cursor = connection.cursor()
        my_res = "SELECT name,issuer_id FROM india_rating_company WHERE history_crawl_flag='0'"
        cursor.execute(my_res)
        co_name = cursor.fetchall()
        for company in co_name:
            p_name = company[0].strip()
            p_issuer_id=company[1]
            print(p_issuer_id)
            params = {
                'searchText': p_name,
                'pageNumber': '0',
                'noOfShowEntry': '100',
            }

            headers = {
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
            }
            get_data = requests.get('https://www.indiaratings.co.in/home/GetNCOMaintenanceMidcorporates',
                                    params=params, headers=headers)
            m_data = get_data.json()
            rating_history = []
            for data in m_data:
                rating = {}
                try:
                   rating['issureid'] = p_issuer_id

                except:
                    rating['issureid']=None

                try:
                   rating['issuerName'] = data.get('issuerName')
                except:
                    rating['issuerName']=None

                try:
                   rating['instrumentType'] = data.get('instrumentType')
                except:
                    rating['instrumentType']=None

                try:
                   rating['outStandingAmount'] = data.get('outStandingAmount')
                except:
                    rating['outStandingAmount']=None

                try:
                   rating['reviewDate'] = data.get('reviewDate')
                except:
                    rating['reviewDate']=None

                try:
                    rating['rating'] = data.get('rating')

                    if '/' in rating['rating']:
                        lt_st=rating['rating'].split('/')
                        rating['long_term']=lt_st[0]
                        rating['short_term']=lt_st[1]

                    else:
                        rating['long_term']=data.get('rating')
                        rating['short_term']=None
                except:
                    rating['rating'] = None

                try:
                    rating['totalRowsCount'] = data.get('totalRowsCount')
                except:
                    rating['totalRowsCount']=None
                rating_history.append(rating)
                params = {
                    "issuerId": data.get('issuerId')
                }
                lastpr_url = requests.get("https://www.indiaratings.co.in/home/GetLastPR", params=params)
                lastpr_url_data = lastpr_url.json()

                params = {
                    'pressReleaseId': lastpr_url_data,
                    'uniqueIdentifier': '122.170.18.40-20230710',
                }
                pre_url = requests.get("https://www.indiaratings.co.in/pressReleases/GetPressreleaseData",
                                       params=params)
                pre_url_data = pre_url.json()
                for pre_data in pre_url_data:
                    lastpr = {}

                    try:
                        lastpr['pressReleaseID'] = pre_data.get("pressReleaseID")
                    except:
                        lastpr['pressReleaseID']=None

                    try:
                        lastpr['pressReleaseTitle'] = pre_data.get("pressReleaseTitle")
                    except:
                        lastpr['pressReleaseTitle']=None

                    try:
                        lastpr['prTypeName'] = pre_data.get("prTypeName")
                    except:
                        lastpr['prTypeName']=None

                    try:
                        lastpr['acceptanceStatus'] = pre_data.get("acceptanceStatus")
                    except:
                        lastpr['acceptanceStatus']=None

                    try:
                        lastpr['sector'] = pre_data.get("sector")
                    except:
                        lastpr['sector']=None

                    try:
                        lastpr['subSecto'] = pre_data.get("subSector")
                    except:
                        lastpr['subSecto']=None

                    try:
                        lastpr['issuerID'] = pre_data.get("issuerID")
                    except:
                        lastpr['issuerID']=None

                    try:
                        lastpr['issuerName'] = pre_data.get("issuerName")
                    except:
                        lastpr['issuerName']=None

                    try:
                        lastpr['primaryAnalystID'] = pre_data.get("primaryAnalystID")
                    except:
                        lastpr['primaryAnalystID']=None

                    try:
                        lastpr['secondaryAnalystID'] = pre_data.get("secondaryAnalystID")
                    except:
                        lastpr['secondaryAnalystID']=None

                    try:
                        lastpr['tertiaryAnalystID'] = pre_data.get("tertiaryAnalystID")
                    except:
                        lastpr['tertiaryAnalystID']=None

                    try:
                        lastpr['chairpersonID'] = pre_data.get("chairpersonID")
                    except:
                        lastpr['chairpersonID']=None

                    try:
                        lastpr['mediaContactID'] = pre_data.get("mediaContactID")
                    except:
                        lastpr['mediaContactID']=None

                    try:
                        lastpr['location'] = pre_data.get("location")
                    except:
                        lastpr['location']=None

                    try:
                        lastpr['metaTags'] = pre_data.get("metaTags")
                    except:
                        lastpr['metaTags']=None

                    try:
                        lastpr['effectiveDate'] = pre_data.get("effectiveDate")
                    except:
                        lastpr['effectiveDate']=None

                    try:
                        lastpr['effectiveDateTime'] = pre_data.get("effectiveDateTime")
                    except:
                        lastpr['effectiveDateTime']=None

                    try:
                        lastpr['dateOfCreation'] = pre_data.get("dateOfCreation")
                    except:
                        lastpr['dateOfCreation'] =None

                    try:
                        lastpr['viewCount'] = pre_data.get("viewCount")
                    except:
                        lastpr['viewCount']=None

                    try:
                        lastpr['ratingCriteriaReportsIDs'] = pre_data.get("ratingCriteriaReportsIDs")
                    except:
                        lastpr['ratingCriteriaReportsIDs']=None

                    try:
                        lastpr['pressReleaseStatus'] = pre_data.get("pressReleaseStatus")
                    except:
                        lastpr['pressReleaseStatus']=None

                    try:
                        lastpr['activity'] = pre_data.get("activity")
                    except:
                        lastpr['activity']=None

                    try:
                        lastpr['lastActivityDate'] = pre_data.get("lastActivityDate")
                    except:
                        lastpr['lastActivityDate']=None

                    try:
                        currentRatings = pre_data.get("currentRatings")
                        currentRatings_soup = BeautifulSoup(currentRatings, 'lxml')
                        current_Ratings = []
                        for currentRatings_data in currentRatings_soup.findAll('tr')[1:]:
                            td = currentRatings_data.find_all('td')
                            current_Rating = {}
                            current_Rating['Instrument Type'] = td[0].text.strip().replace('\r\n', '')
                            current_Rating['Size of Issue (million)'] = td[4].text.strip().replace('\r\n', '')
                            current_Rating['Rating'] = td[5].text.strip().replace('\r\n', '')
                            current_Rating['Rating Action'] = td[6].text.strip().replace('\r\n', '')
                            current_Ratings.append(current_Rating)
                        lastpr['currentRatings'] = current_Ratings
                    except:
                        lastpr['currentRatings']=None

                    try:
                        ratingHistory = pre_data.get("ratingHistory")
                        ratingHistory_soup = BeautifulSoup(ratingHistory, 'lxml')

                        column_name = []
                        for ratingHistory_data in ratingHistory_soup.findAll('tr')[1:2]:
                            td = column_name.append(
                                ratingHistory_data.text.replace('\r\n', ' ').replace('\n\n\n', ',').replace('\n\n',
                                                                                                            '').replace(
                                    '  ', ''))
                        c_name = column_name[0].split(',')
                        f_column = c_name.insert(0, 'Instrument Type')

                        ratings_History = []
                        for ratingHistory_data in ratingHistory_soup.findAll('tr')[2:]:
                            td = ratingHistory_data.find_all('td')

                            rating_History = {}
                            for column in range(len(c_name)):
                                rating_History[c_name[column]] = td[column].text.strip().replace('\r\n', '')
                            ratings_History.append(rating_History)

                        lastpr['rating_History'] = ratings_History
                    except:
                        lastpr['rating_History']=None

                    try:
                        complexityLevelOfInstruments = pre_data.get("complexityLevelOfInstruments")
                        complexityLevelOfInstruments_soup = BeautifulSoup(complexityLevelOfInstruments, 'lxml')
                        complexityLevelO_Instruments = []
                        for complexityLevelOfInstruments_data in complexityLevelOfInstruments_soup.findAll('tr')[1:]:
                            td = complexityLevelOfInstruments_data.find_all('td')
                            complexityLevelO_Instrument = {}
                            complexityLevelO_Instrument['Instrument Type'] = td[0].text.strip().replace('\r\n', '')
                            complexityLevelO_Instrument['Complexity Indicator'] = td[1].text.strip().replace('\r\n', '')
                            complexityLevelO_Instruments.append(complexityLevelO_Instrument)
                        lastpr['complexityLevelOfInstruments'] = complexityLevelO_Instruments

                    except:
                        lastpr['complexityLevelOfInstruments']=None

                    try:
                        lastpr['industry'] = pre_data.get("industry")
                    except:
                        lastpr['industry']=None

                    try:
                        lastpr['primaryAnalystName'] = pre_data.get("primaryAnalystName")
                    except:
                        lastpr['primaryAnalystName']=None

                    try:
                        lastpr['primaryAnalystDesignation'] = pre_data.get("primaryAnalystDesignation")
                    except:
                        lastpr['primaryAnalystDesignation']=None

                    try:
                        lastpr['primaryAnalystCompanyName'] = pre_data.get("primaryAnalystCompanyName")
                    except:
                        lastpr['primaryAnalystCompanyName']=None

                    try:
                        lastpr['primaryAnalystAddress'] = pre_data.get("primaryAnalystAddress")
                    except:
                        lastpr['primaryAnalystAddress']=None

                    try:
                        lastpr['primaryAnalystContactNumber'] = pre_data.get("primaryAnalystContactNumber")
                    except:
                        lastpr['primaryAnalystContactNumber']=None

                    try:
                        lastpr['secondaryAnalystName'] = pre_data.get("secondaryAnalystName")
                    except:
                        lastpr['secondaryAnalystName']=None

                    try:
                        lastpr['secondaryAnalystDesignation'] = pre_data.get("secondaryAnalystDesignation")
                    except:
                        lastpr['secondaryAnalystDesignation']=None

                    try:
                        lastpr['secondaryAnalystContactNumber'] = pre_data.get("secondaryAnalystContactNumber")
                    except:
                        lastpr['secondaryAnalystContactNumber']=None

                    try:
                        lastpr['chairpersonName'] = pre_data.get("chairpersonName")
                    except:
                        lastpr['chairpersonName']=None

                    try:
                        lastpr['chairpersonDesignation'] = pre_data.get("chairpersonDesignation")
                    except:
                        lastpr['chairpersonDesignation']=None

                    try:
                        lastpr['chairpersonContactNumber'] = pre_data.get("chairpersonContactNumber")
                    except:
                        lastpr['chairpersonContactNumber']=None

                    try:
                        lastpr['mediaRelationName'] = pre_data.get("mediaRelationName")
                    except:
                        lastpr['mediaRelationName']=None

                    try:
                        lastpr['mediaRelationDesignation'] = pre_data.get("mediaRelationDesignation")
                    except:
                        lastpr['mediaRelationDesignation']=None

                    try:
                        lastpr['mediaRelationContactNumber'] = pre_data.get("mediaRelationContactNumber")
                    except:
                        lastpr['mediaRelationContactNumber']=None

                    rating['lastPR'] = lastpr
                    last_pr = json.dumps(lastpr)
                    db_date = datetime.strptime(rating['reviewDate'], '%d/%m/%Y')
                    today=date.today()
                    rating_history.append(rating)
                    try:
                        sql_history = "INSERT INTO india_rating_history (issuer_id,instrument_type,outstanding_amount,date,long_term_rating,short_term_rating) VALUES (%s,%s,%s,%s,%s,%s)"
                        val_history = (
                            p_issuer_id, rating['instrumentType'], rating['outStandingAmount'], db_date,
                            rating['long_term'],
                            rating['short_term'])
                        # cursor.execute(sql_history, val_history)
                        # print(val_history)
                        connection.commit()
                    except:
                         pass

                    try:
                        sql_release = "INSERT INTO india_rating_press_release (issuer_id,press_release_id,data,add_date) VALUES (%s,%s,%s,%s)"
                        val_release = (p_issuer_id, lastpr['pressReleaseID'], last_pr, today)
                        # cursor.execute(sql_release, val_release)
                        connection.commit()
                    except:
                        pass

            india_company = "UPDATE india_rating_company SET history_crawl_flag = %s WHERE issuer_id = %s"
            val_company=(1,p_issuer_id)
            # cursor.execute(india_company,val_company)
            connection.commit()

Indiarating().find_char()


