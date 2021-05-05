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


def get_distric_id(args):
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/districts/%s" % (args.state_id)
    res = requests.get(url)
    if res.status_code == 200:
        for i in res.json()["districts"]:
            print ("%s: %s" % (i["district_name"], i["district_id"]))

def get_state_id(args):
    url = "https://cdn-api.co-vin.in/api/v2/admin/location/states"
    res = requests.get(url)
    if res.status_code == 200:
        for i in res.json()["states"]:
            print ("%s: %s" % (i["state_name"], i["state_id"]))

def get_availability(args):
    while True:
        fetch(args.district_id)
        print("Sleeping....")
        time.sleep(1)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    subparsers = ap.add_subparsers(help='Sub commands for use')

    parser_a = subparsers.add_parser('states', help='states list command help')
    parser_a.set_defaults(func=get_state_id)
    
    parser_b = subparsers.add_parser('district', help='district list command help')
    parser_b.add_argument("-s", "--state_id", required=True, help="State Id")
    parser_b.set_defaults(func=get_distric_id)

    parser_c = subparsers.add_parser('availability', help='Slot Availability Command')
    parser_c.add_argument("-d", "--district_id", required=True, help="Need distric id")
    parser_c.set_defaults(func=get_availability)

    args = ap.parse_args()
    args.func(args)
