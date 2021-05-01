#Modified version of https://github.com/bhattbhavesh91 's work!

import requests
import datetime
import json
import pandas as pd

#Enter user inputs
DIST_ID = 446 # KHURDA
age = 26

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(31)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        # print(json.dumps(resp_json, indent = 1))
        if resp_json["centers"]:
            for center in resp_json["centers"]:
                for session in center["sessions"]:
                    if session["min_age_limit"] <= age:
                        if(session["available_capacity"]>0):
                            print("Available on: {}".format(INP_DATE))
                            print("\t", center["name"])
                            print("\t", center["block_name"])
                            print("\t Price: ", center["fee_type"])
                            print("\t Available Capacity: ", session["available_capacity"])
                            if(session["vaccine"] != ''):                         
                                print("\t Vaccine: ", session["vaccine"])
                            print("\n\n")
