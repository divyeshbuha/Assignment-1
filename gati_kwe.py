import requests
from lxml import html

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'
}


def scrape_details(lr_no):
    data = {
        # 'status': 'status_docket',
        'docket_id': lr_no,
        # 'recName': '',
        # 'track1': 'Submit',
    }

    response = requests.post('https://www.gatikwe.com/OurTrack/DktTrack.php', headers=headers, data=data)
    if response.status_code == 200:
        dom = html.fromstring(response.text)

        result = {}
        try:
            result['lr_no'] = dom.xpath('//td[@class="td docket-number"]/text()')[0].strip()
        except:
            result['lr_no'] = None

        try:
            result['reference_no'] = dom.xpath('//td[@class="td reference-number"]/text()')[0].strip()
        except:
            result['reference_no'] = None

        try:
            result['origin'] = dom.xpath('//td[@class="td origin"]/text()')[0].strip()
        except:
            result['origin'] = None

        try:
            result['destination'] = dom.xpath('//td[@class="td destination"]/text()')[0].strip()

        except:
            result['destination'] = None

        try:
            result['pickup_date'] = dom.xpath('//td[@class="td pickup-date"]/text()')[0].strip()
        except:
            result['pickup_date'] = None

        try:
            result['status'] = dom.xpath('//td[@class="td status"]/text()')[0].strip()
        except:
            result['status'] = None

        try:
            result['pod_url'] = dom.xpath('//h3[@class="status-heading"]//a/@href')[0].strip()
        except:
            result['pod_url'] = None

        try:
            result['booking_date'] = response.text.split("Booking Date : </b>")[-1].split("<br>")[0].strip()
        except:
            result['booking_date'] = None

        try:
            result['assured_dly_date'] = response.text.split("Assured Dly. Dt : </b>")[-1].split("<br>")[0].strip()
        except:
            result['assured_dly_date'] = None

        try:
            result['no_of_pkgs'] = response.text.split("No. of Pkgs : </b>")[-1].split("<br>")[0].strip()
        except:
            result['no_of_pkgs'] = None

        try:
            result['weight'] = response.text.split("Weight : </b>")[-1].split("<br>")[0].strip()
        except:
            result['weight'] = None

        st_history = []
        try:
            for tr in dom.xpath('//table[@class="table status-table table-striped"]//tr[@class="dkt-item"]'):
                st_history_dict = {}
                try:
                    st_history_dict['date'] = tr.xpath('./td[1]/text()')[0].strip()
                except:
                    st_history_dict['date'] = None

                try:
                    st_history_dict['time'] = tr.xpath('./td[2]/text()')[0].strip()
                except:
                    st_history_dict['time'] = None

                try:
                    st_history_dict['location'] = tr.xpath('./td[3]/text()')[0].strip()
                except:
                    st_history_dict['location'] = None

                try:
                    st_history_dict['status'] = tr.xpath('./td[4]/text()')[0].strip()
                except:
                    st_history_dict['status'] = None

                st_history.append(st_history_dict)
        except Exception as e:
            print(e)
        result['shipment_tracking_history'] = st_history
        print(result)


if __name__ == "__main__":
    lr_no = "319526214"
    scrape_details(lr_no)
