#!/usr/bin/python3

import requests

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## grab creds
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove newline char from api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## make call to NASAAPI with key
    apodresp = requests.get(NASAAPI + nasacreds)

    ## strip off json
    apod = apodresp.json()

    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"])

    print(apod["url"])

if __name__ == "__main__":
    main()
