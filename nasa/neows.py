#!/usr/bin/python3

import requests

## define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def main():
    ## first, grab creds
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove newline char from api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## update date below if wanted
    startdate = "start_date=2019-11-11"

    # make request with request lib
    neowrequest = requests.get(NEOURL + startdate + "&" + nasacreds)

    # strip off json attachment from response
    neodata = neowrequest.json()

    ## display NASA NEOW data
    print(neodata)

if __name__ == "__main__":
    main()
