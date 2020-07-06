#!/usr/bin/python3

import requests

ITEMURL = "http://pokeapi.co/api/v2/item/"

def main():
    items = requests.get(f"{ITEMURL}?limit=1000")
    items = items.json()

    healwords = []

    for item in items.get("results"):
        if 'heal' in item.get("name"):
            healwords.append(item.get("name"))

    ## list all
    print(f"There are {len(healwords)} words that contain the word 'heal' in the Pokemon Item API!")
    print("List of Pokemon items containing heal: ")
    print(healwords)

if __name__ == "__main__":
    main()
