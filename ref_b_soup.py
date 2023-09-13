import requests
from bs4 import BeautifulSoup
import urllib.parse
import csv
import random

class Exportsindia(object):
    """docstring for Exportindia"""

    def __init__(self, arg):
        self.host = "https://www.exportersindia.com/"
        self.company_name = arg['company_name']
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

        numbers = ["9", "7", "8", "6", "5", "4", "3", "2", "1"]
        mobile = "98"
        for i in range(8):
            mobile = mobile + random.choice(numbers)

        return {"email": email, "name": name, "mobile": mobile}

    #get the final result
    def get_final_contact(self,company_contact_data,url):

        if company_contact_data:
            udata = self.gen_random_email()
            final_res = []
            # url=company_contact_data[0]['contact_link'].replace("'","")
            # parsed = urllib.parse.urlparse(url)
            # mem_id=urllib.parse.parse_qs(parsed.query)['mem_id']
            data = {
                "country_code": "IN^91",
                "isd_code": "",
                "login_status": "",
                "mem_url": "https://members.exportersindia.com/",
                "mobile_phone": udata['mobile'],
                "other_city": "Mumbai",
                "page_url": "",
                "pgfrm": "",
                "ph_ccode1": "",
                "search_keyword": "",
                "submit_form_view_mobile": "Submit",
                "user_name": udata['email'],
                "your_name": udata['name']
            }
            # req=requests.post(url,data=data)

            for con in company_contact_data:
                url = con['contact_link'].replace("'", "")
                print(url)
                parsed = urllib.parse.urlparse(url)
                mem_id = urllib.parse.parse_qs(parsed.query)['mem_id'][0]
                data['mem_id'] = mem_id
                contact_html = requests.post(
                    url, data=data, proxies=self.proxy)
                soup = BeautifulSoup(contact_html.text, "lxml")
                contact_ul = soup.find_all(
                    'ul', attrs={"class": "fo ac-fl ac-p5px"})
                con['name'] = contact_ul[0].find(
                    'li', attrs={"class": "black xlarge"}).get_text()
                con['mobile_no'] = [contact_ul[1].find(
                    'li', attrs={"class": "black xlarge"}).get_text()]
                con['phone_no'] = []
                del con['contact_link']
                del con['business_type']
                final_res.append(con)
                con = {}
            return final_res
    #search result from expoters india
    def search(self):
        proxy=""
        url =self.host + "search.php?term=" +self.company_name + "&srch_catg_ty=comp&cont=IN"
        search_page = requests.get(url, proxies=proxy)
        search_html = BeautifulSoup(search_page.text, "lxml")
        # print(search_page.status_code)
        search_result = search_html.find_all(
            'div', attrs={"class": "fo pr bdr bsb5px10-hover"})
        # print(search_result)#all result of company name
        company_contact_data = []
        contact_data = {}
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
                    company_contact_data.append(contact_data)
                    contact_data = {}

                except Exception as e:
                    pass
        return self.get_final_contact(company_contact_data,url)
Exportsindia().search()




