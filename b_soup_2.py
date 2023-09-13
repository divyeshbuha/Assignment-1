import random
import urllib.parse
import requests
from bs4 import BeautifulSoup
class Exportsindia(object):
    def __init__(self, arg='synnova'):
        self.host = "https://www.exportersindia.com/"
        self.company_name = arg
        self.proxy = "" #request_helper.get_free_proxy()

    def gen_random_email(self):
        domains = ["hotmail.com", "gmail.com", "aol.com",
                   "yahoo.in", "mail.kz", "yahoo.com"]
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

        email_name = ""
        for i in range(7):
            email_name = email_name + random.choice(letters)
        email = email_name + '@' + random.choice(domains)
        name = email_name
        # print(email_name)
        # print(email)
        # print(name)
        numbers = ["9", "7", "8", "6", "5", "4", "3", "2", "1"]
        mobile = "98"
        for i in range(8):
            mobile = mobile + random.choice(numbers)
        # print(mobile)
        return {"email": email, "name": name, "mobile": mobile}


    def get_final_contact(self, company_contact_data):


        if company_contact_data:
            udata = self.gen_random_email()
            # print(udata)

            # url=company_contact_data[0]['contact_link'].replace("'","")

            # parsed = urllib.parse.urlparse(url)
            # mem_id=urllib.parse.parse_qs(parsed.query)['mem_id']
            # print(parsed)

            headers = {
                'authority': 'www.exportersindia.com',
                'accept': 'text/html, */*; q=0.01',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'cookie': 'PHPSESSID=i1hkff2vlughnr4g5aoh4r8k5i; _gcl_au=1.1.357428715.1688623200; _gid=GA1.2.1167586139.1688623200; _fbp=fb.1.1688623200648.1994064020; my_cookie_inq_keyword_val=tanisq; _ga=GA1.1.918312186.1688623200; _gat=1; _ga_ZERZR4LL1X=GS1.1.1688623200.1.1.1688623323.60.0.0; _ga_ND6L97XWLF=GS1.2.1688623200.1.1.1688623323.60.0.0; temp_guest_arr=12238803%7C%7Cvishal%7C%7C%7C%7Cgadenaj815%40edulena.com%7C%7CIN%7C%7C9687111146%7C%7C%7C%7CG%7C%7C91%7C%7C%7C%7C%7C%7C%7C%7C; join_now_mem_id=10316361',
                'origin': 'https://www.exportersindia.com',
                'referer': 'https://www.exportersindia.com/search.php?srch_catg_ty=comp&term=tanisq&cont=IN&ss_status=N',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'your_name': 'vishal',
                'mobile_phone': '9687111146',
                'country_code': 'IN^91',
                'user_name': 'gadenaj815@edulena.com',
                'search_kword': '',
                'mem_id': '7367674',
                'submit_form_view_mobile': 'Submit',
                'mob_num': '9687111146',
                'verify_mobile_country_id': 'in',
                'isd_code': '91',
                'baseurl': 'https://www.exportersindia.com',
                'view_contact_version': '2',
                'page_url':self.host + "search.php?term=" +self.company_name + "&srch_catg_ty=comp&cont=IN",
                'mobile_verified': 'Y',
            }

            # params = {
            #     'mem_id': "mem_id",
            #     'sid': '0.1753000357941774',
            # }
            # data = {"your_name": udata['name'],
            #         "mobile_phone": udata['mobile'],
            #         "country_code": "IN^91",
            #         "user_name": udata['email'],
            #         "search_kword": "",
            #         "mem_id": "mem_id",
            #         'sid': '0.1753000357941774',
            #         "submit_form_view_mobile": "Submit",
            #         "mob_num": udata['mobile'],
            #         "verify_mobile_country_id": "in",
            #         "isd_code": "91",
            #         "baseurl": "https://www.exportersindia.com",
            #         "view_contact_version": "2",
            #         "page_url": "www.exportersindia.com/search.php?srch_catg_ty=comp&term=tanisq&cont=IN&ss_status=N",
            #         "mobile_verified":"Y",
            #
            #
            # }
            # req=requests.post(url,data=data)
            final_res = []
            for con in company_contact_data:
                # print(con)
                url = con['contact_link'].replace("'", "")
                parsed = urllib.parse.urlparse(url)
                mem_id = urllib.parse.parse_qs(parsed.query)['mem_id'][0]
                data['mem_id'] = mem_id
                # print(url)
                contact_html = requests.post(
                    url, data=data,headers=headers, proxies=self.proxy)
                # print(contact_html.status_code)
                soup = BeautifulSoup(contact_html.text, "lxml")
                print(soup.text)
                contact_ul = soup.find_all('ul', attrs={"class":"fo ac-fl ac-p7px"})
                # print(contact_ul)
                con['name'] = contact_ul[0].text[11:]#find('li',{"class": "black xlarge"})
                # print(con['name'])
                con['mobile_no'] = contact_ul[1].text[18:] # find('li', attrs={"class": "black xlarge"}).get_text()]
                # print(con['mobile_no'])
                con['phone_no'] = contact_ul[2].text[23:38]
                # print(con['phone_no'])
                del con['contact_link']
                del con['business_type']
                con = {}
                final_res.append(con)
                # print(con)
            return final_res
            # print(final_res)

    def search(self):
        proxy=""
        url = self.host + "search.php?term=" +self.company_name + "&srch_catg_ty=comp&cont=IN"
        # print(url)
        search_page = requests.get(url, proxies=proxy)
        search_html = BeautifulSoup(search_page.content, "lxml")
        # print(search_page.status_code)
        search_result = search_html.find_all(
            'div', attrs={"class": "fo pr bdr bsb5px10-hover"})
        # print(search_result)#all result of company name
        company_contact_data = []
        contact_data = {}
        # print(company_contact_data)
        for search_res in search_result:

                try:
                    company_name = search_res.find('a', attrs={"class": "bn"})

                    contact_data['link'] = company_name['href']#add contact_data dictionary in link
                    contact_data['company_name'] = company_name.get_text()#add contact_data dictionary in company name
                    # print(contact_data)  # add contact_data dictionary in link & company name
                    business_t_add = search_res.find_all('dd', attrs={'ofh mb5px'})


                    try:
                        contact_data['business_type'] = business_t_add[0].get_text()#add contact_data dict in business_type
                        contact_data['address'] = business_t_add[1].get_text()#add contact_data dict in business address
                    except Exception as e:
                        contact_data['address'] = business_t_add[0].get_text()
                        contact_data['business_type'] = ""
                    # print(contact_data)# all data add in dict for company
                    '''a=contact_data['business_type']=business_t_add[0].get_text()
                    b=contact_data['address']=business_t_add[1].get_text()
                    print(a)
                    print(b)'''#second method of find business_type & address
                    js_link = search_res.find('a', attrs={"class": "fl ts0 darkbg4 bsbb bdr p7px10px b white tac"})#find js a tag
                    js_link_fun_string = js_link['href'][js_link['href'].find("(") + 1:js_link['href'].find(")")]#find js in contact detail link
                    # print(js_link)
                    # print(js_link_fun_string)
                    # break
                    contact_data['contact_link'] = js_link_fun_string.split(',')[0]
                    # print(js_link_fun_string.split(',')[0])
                    company_contact_data.append(contact_data)
                    contact_data = {}
                    # print(company_contact_data)
                except Exception as e:
                    pass


        # print(company_contact_data)
        # filename = 'data.csv'
        # with open(filename, 'w', newline='') as f:
        #     w = csv.DictWriter(f, ['link', 'company_name', 'business_type', 'address', 'contact_link'])
        #     w.writeheader()
        #     for contact_data in company_contact_data:
        #         w.writerow(contact_data)
        return self.get_final_contact(company_contact_data)


# the_object = Exportsindia()
Exportsindia().search()
Exportsindia().gen_random_email()
Exportsindia().get_final_contact(company_contact_data=[])
'''company_contact_data=[{'link': 'https://www.exportersindia.com/tanisq-impax/', 'company_name': 'Tanisq impax', 'business_type': 'Supplier /  Retailer', 'address': 'Panipat, Haryana India', 'contact_link': "'https://www.exportersindia.com/view_free_member_mobile.php?mem_id=7367674'"},
                      {'link': 'https://www.exportersindia.com/tanisq-shellac-industry-4163820/', 'company_name': 'Tanisq Shellac Industry', 'business_type': 'Retailer', 'address': 'Masjid Road, Purulia, West Bengal India', 'contact_link': "'https://www.exportersindia.com/view_free_member_mobile.php?mem_id=4163820'"},
                      {'link': 'https://www.exportersindia.com/tanisq-computers-and-4049061/', 'company_name': 'Tanisq Computers And Networking', 'business_type': 'Supplier', 'address': 'Model Town, Panipat, Haryana India', 'contact_link': "'https://www.exportersindia.com/view_free_member_mobile.php?mem_id=4049061'"}]'''
# https://www.indiaratings.co.in/search/issuerid/3201   9504


