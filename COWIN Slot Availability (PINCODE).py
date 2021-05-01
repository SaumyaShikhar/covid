import requests
import datetime
import json

POST_CODE = "751024"
age = 26

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(30)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]

for INP_DATE in date_str:
    URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(POST_CODE, INP_DATE)
    response = requests.get(URL)
    if response.ok:
        resp_json = response.json()
        # print(json.dumps(resp_json, indent = 1))
        flag = False
        #print(resp_json)
        if resp_json["centers"]:
            count = 0
            for center in resp_json["centers"]:
                for session in center["sessions"]:
                    if (session["min_age_limit"] <= age):
                        if(session["available_capacity"]>0):
                            print("Available on: {}".format(INP_DATE))
                            print("\t", center["name"])
                            print("\t", center["block_name"])
                            print("\t Price: ", center["fee_type"])
                            print("\t Available Capacity: ", session["available_capacity"])
                            if(session["vaccine"] != ''):
                                print("\t Vaccine: ", session["vaccine"])
                            print("\n\n")
                            count = count + 1
if count == 0:
    print("No slots available")
