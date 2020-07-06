#!/usr/bin/python3

import requests
import json

# define URL 
GETURL = "http://validate.jsontest.com/"

def main():
    # test data to validate as legal json
    mydata = {"fruit": ["apple", "pear"], "vegetable": ["carrot"]}

    jsonToValidate = f"json={ json.dumps(mydata).replace(' ', '') }"

    # use requests library to send HTTP GET
    resp = requests.get(f"{GETURL}?{jsonToValidate}")

    respjson = resp.json()

    print(respjson)

    print(f"Is your JSON valid? {respjson['validate']}")

if __name__ == "__main__":
    main()
