#!/usr/bin/python3

import pandas

def main():

    mydata = [
    {'hostname': 'dumbledore', 'ip': '192.168.9.22', 'service': 'objectstorage'},
    {'hostname': 'hermione', 'ip': '10.0.2.66', 'service': 'httpd'}
    ]

    df = pandas.DataFrame(mydata)

    df.to_csv("inventorypandas.csv", index=False)

if __name__ == "__main__":
    main()
