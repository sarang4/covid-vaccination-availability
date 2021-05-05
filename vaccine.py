# creator Sarang Shravagi
import time, os
import requests, argparse
from datetime import datetime


def fetch(district_id):
    try:
        available_flag = False
        url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/calendarByDistrict?district_id=%s&date=%s' % (district_id, datetime.now().strftime("%d-%m-%Y"))
        res = requests.get(url)
        print(res)
        if res.status_code == 200:
            k = res.json()
            for i in k['centers']:
                for j in i['sessions']:
                    if j['min_age_limit'] == 18 and j['available_capacity'] >= 2:
                        available_flag = True
                        print (i['name'], i['pincode'], i['fee_type'], j['date'], j['available_capacity'], j['slots'])
            if not available_flag:
                print("Not Available...")
    except Exception as e:
        print e
        return


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-d", "--district_id", required=True, help="District Id")
    args = vars(ap.parse_args())
    while True:
        fetch(args["district_id"])
        print("Sleeping....")
        time.sleep(1)