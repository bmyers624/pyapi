#!/usr/bin/python3

import requests

def main():
    resp = requests.get('https://statsapi.web.nhl.com/api/v1/teams')

    for teams in resp.json()["teams"]:
        print(teams.get("name"))

if __name__ == "__main__":
    main()
