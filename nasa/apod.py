#!/usr/bin/python3

import urllib.request
import json

NASAAPI = "https://api.nasa.gov/planetary/apod?"

def main():
    ## define creds
    with open("/home/student/nasa.creds") as mycreds:
        nasacreds = mycreds.read()

    ## remove any "extra" new line feeds on our key
    nasacreds = "api_key=" + nasacreds.strip("\n")

    ## call webservice with key
    apodurlobj = urllib.request.urlopen(NASAAPI + nasacreds)

    ## read file-like object
    apodread = apodurlobj.read()

    ## decode JSON to Python data struct
    apod = json.loads(apodread.decode("utf-8"))

    ## display python data
    print("\n\nConverted Python data")
    print(apod)

    print()

    print(apod["title"] + "\n")

    print(apod["date"] + "\n")

    print(apod["explanation"] + "\n")

    print(apod["url"])

if __name__ == "__main__":
    main()
