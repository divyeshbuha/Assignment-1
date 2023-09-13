import requests

class Indiarating(object):
    def __init__(self,arg='d',issureid=3064):
        self.key=arg
        self.id=issureid

    def search(self):
        global name
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        params = {
            'searchKey':self.key,
            'noOfShowEntry': '0',
        }
        url='https://www.indiaratings.co.in/home/GetSearchIssuerData'
        search_page = requests.get(url,params=params,headers=headers)
        data=(search_page.json())
        issuer = []
        india_ratings=[]
        for item in data:
            id=item.get('issuerID')
            issuer.append(id)
        params = {
            'issuerID':self.id,
            'noOfShowEntry': '50',
        }
        if self.id in issuer:
            search_url = requests.get('https://www.indiaratings.co.in/home/GetIssuerDetails', params=params,
                                      headers=headers)
            details = search_url.json()
            for detail in details:
                # print(detail.get('name'))
                name=detail.get('name')
                ratingslist = (detail.get('ratingsList'))
                # for ratingslist_name in ratingslist:
                #     india_rating = {}
                #     india_rating['name'] = (detail.get('name'))
                #     # india_rating['instrumentName'] = (ratingslist_name.get('instrumentName'))
                #     # india_rating['amount'] = ratingslist_name.get('amount')
                #     # india_rating['currency'] = ratingslist_name.get('currency')
                #     # india_rating['rating'] = ratingslist_name.get('rating')
                #     # print(india_rating)
                #     india_ratings.append(india_rating)
                #     # print(india_ratings)
        else:
            print("please enter valid issuerid/key")
        return self.find_detail(name)

    def find_detail(self,name):

        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        }
        params = {
            'searchText': name,
            'pageNumber': '0',
            'noOfShowEntry': '100',
        }
        # print(params)
        get_data = requests.get('https://www.indiaratings.co.in/home/GetNCOMaintenanceMidcorporates',
            params=params,headers=headers)
        m_data=get_data.json()
        # print(m_data)
        for data in m_data:
            rating={}
            rating['issuerName'] = (data.get('issuerName'))
            rating['instrumentType'] = (data.get('instrumentType'))
            rating['outStandingAmount'] = data.get('outStandingAmount')
            rating['reviewDate'] = data.get('reviewDate')
            rating['rating'] = data.get('rating')
            rating['totalRowsCount'] = data.get('totalRowsCount')
            print(rating)

Indiarating().search()
Indiarating().find_detail()


# import requests
#
#
# def search():
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#     }
#     params = {
#         'searchKey': 'b',
#         'noOfShowEntry': '0',
#     }
#     url = 'https://www.indiaratings.co.in/home/GetSearchIssuerData'
#     search_page = requests.get(url, params=params, headers=headers)
#     data = (search_page.json())
#     india_ratings = []
#
#     for item in data:
#         id = item.get('issuerID')
#         params = {
#             'issuerId': id,
#             'noOfShowEntry': '10',
#         }
#         id_url = "https://www.indiaratings.co.in/home/GetIssuerDetails"
#         response = requests.get(id_url, params=params, headers=headers)
#         detail = (response.json())
#
#         for details in detail:
#
#             ratingslist = (details.get('ratingsList'))
#             for ratingslist_name in ratingslist:
#                 india_rating = {}
#                 india_rating['name'] = (details.get('name'))
#                 india_rating['instrumentName'] = (ratingslist_name.get('instrumentName'))
#                 india_rating['amount'] = ratingslist_name.get('amount')
#                 india_rating['currency'] = ratingslist_name.get('currency')
#                 india_rating['rating'] = ratingslist_name.get('rating')
#                 try:
#                     india_ratings.append(india_rating)
#                 except Exception as e:
#                     print(e)
#                 # print((details.get('name')))
#                 # print((ratingslist_name.get('instrumentName')))
#                 # print(ratingslist_name.get('amount'))
#                 # print(ratingslist_name.get('currency'))
#                 # print(ratingslist_name.get('rating'))
#
#         print(india_ratings)
#         break
#
#         # filename = 'data.csv'
#         # with open(filename, 'w', newline='') as f:
#         #     w = csv.DictWriter(f, ['name', 'instrumentName', 'amount', 'currency', 'rating'])
#         #     w.writeheader()
#         #     for india_rating in india_ratings:
#         #         w.writerow(india_rating)
#
#
# class Indiarating(object):
#     pass
#
#
# search()

# class Indiarating(object):
#     def __init__(self,arg):
#         self.host="https://www.indiaratings.co.in/searchbykey;key="
#         self.alphabet=arg['a']
#     def search(self):
#         headers = {
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
#         }
#         params = {
#             'searchKey': 'a',
#             'noOfShowEntry': '0',
#         }
#         url=self.host+self.alphabet
#         search_page = requests.get(url,params=params,headers=headers)
#         data=(search_page.json())
#         india_ratings = []
#
#         for item in data:
#             id=item.get('issuerID')
#             params = {
#                 'issuerId': id,
#                 'noOfShowEntry': '10',
#             }
#             id_url="https://www.indiaratings.co.in/home/GetIssuerDetails"
#             response=requests.get(id_url,params=params,headers=headers)
#             detail=(response.json())
#
#             for details in detail:
#
#
#                 ratingslist=(details.get('ratingsList'))
#                 for ratingslist_name in ratingslist:
#                     india_rating = {}
#                     india_rating['name'] = (details.get('name'))
#                     india_rating['instrumentName'] = (ratingslist_name.get('instrumentName'))
#                     india_rating['amount'] = ratingslist_name.get('amount')
#                     india_rating['currency'] = ratingslist_name.get('currency')
#                     india_rating['rating'] = ratingslist_name.get('rating')
#                     try:
#                         india_ratings.append(india_rating)
#                     except Exception as  e:
#                         print(e)
#                     # print((details.get('name')))
#                     # print((ratingslist_name.get('instrumentName')))
#                     # print(ratingslist_name.get('amount'))
#                     # print(ratingslist_name.get('currency'))
#                     # print(ratingslist_name.get('rating'))
#
#             print(india_ratings)
#
#             # filename = 'data.csv'
#             # with open(filename, 'w', newline='') as f:
#             #     w = csv.DictWriter(f, ['name', 'instrumentName', 'amount', 'currency', 'rating'])
#             #     w.writeheader()
#             #     for india_rating in india_ratings:
#             #         w.writerow(india_rating)
#
# Indiarating().search()

# after all rating details
#-------------------------------------------------------------------







