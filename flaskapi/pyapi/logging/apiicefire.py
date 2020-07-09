#!/usr/bin/python3

import logging
import requests
import argparse
import pprint

BOOK = "https://www.anapioficeandfirie.com/api/books"

def main():
    logging.basicConfig(filename='icefire.log', format='%(levelname)s:%(asctime)s %(message)s',\
        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)

    try:
        logging.info('Scripting started')

        icefire = requests.get(BOOK + "/" + args.bookno)

        pprint.pprint(icefire.json())

        logging.info("API Response Code -" + str(icefire))

    except Exception as err:
        logging.critical(err)

    finally:
        logging.info("Program ended")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--bookno', help='Enter the book number (integer) to look up.')
    args = parser.parse_args()
    main()
