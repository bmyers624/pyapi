#!/usr/bin/python3

import argparse

import requests

import pandas

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    matchedwords = []

    for item in items.get("results"):
        if args.searchword in item.get("name"):
            matchedwords.append(item.get("name"))

    finishedlist = matchedwords.copy()

    matchedwords = {}
    matchedwords["matched"] = finishedlist

    print(f"There are {len(finishedlist)} words that contain the word '{args.searchword}' in the Pokemon Item API!")
    print(f"List of Pokemon items containing '{args.searchword}': ")
    print(matchedwords)

    itemsdf = pandas.DataFrame(matchedwords)

    itemsdf.to_excel("pokemonitems.xlsx", index=False)

    print("Gotta catch 'em all!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pass in a word to search\
    the Pokemon item API")
    parser.add_argument('searchword', metavar='SEARCHW',\
    type=str, default='ball', help="Pass in any word. Default is 'ball'")
    args = parser.parse_args()
    main()
