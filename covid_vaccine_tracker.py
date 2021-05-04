from datetime import datetime
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pincode", help="Enter pincode")
parser.add_argument("-d", "--date", help="Enter date (format dd-mm-YYYY)")
args = parser.parse_args()


def get_available_slots(pincode="410206", date=datetime.today().strftime('%d-%m-%Y')):
    base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode=pin_placeholder&date=date_placeholder"
    base_url = base_url.replace("pin_placeholder", pincode)
    base_url = base_url.replace("date_placeholder", date)
    res = requests.get(base_url).json()
    not_available = True
    for c_id in res['centers']:
        if c_id['sessions'][0]['available_capacity'] > 0:
            print(c_id['sessions'][0])
            flag = False
    if not_available:
        print(f"Vaccine is not available in pincode {pincode} for {date}")
    return res

# get_available_slots(pincode=args.pincode, date=args.date)
get_available_slots()