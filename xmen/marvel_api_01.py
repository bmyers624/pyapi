#!/usr/bin/python3

import argparse
import time
import hashlib

import requests

## define api 
XAVIER = 'http://gateway.marvel.com/v1/public/characters'

## calculate hash tp [ass through MARVEL API call
## MARVEL API wants md5 calc md5(ts+privateKey+publicKey)
def hashbuilder(timeywimey, pvkee, pubkee):
    return hashlib.md5((timeywimey+pvkee+pubkee).encode('utf-8')).hexdigest()

## Perform call to MARVEL char API
## http://gateway.marvel.com/v1/public/characters
## ?name=Spider-Man&ts=1&apikey=1234&hash=ffd275c5130566a2916217b101f26150
def marvelcharcall(stampystamp, hashyhash, pkeyz, lookmeup):
    r = requests.get(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)

    print(XAVIER+"?name="+lookmeup+"&ts="+stampystamp+"&apikey="+pkeyz+"&hash="+hashyhash)
    return r.json()

def main():

    ## harvest priv key
    with open(args.dev) as mccoy:
        beast = mccoy.read().rstrip('\n')

    ## harvest public key
    with open(args.pub) as munroe:
        storm = munroe.read().rstrip('\n')

    ## create int from float timestamp (for RAND)
    nightcrawler = str(time.time()).rstrip('.')

    ## build hash w/ hashbuilder(timestamp, privkey, pubkey)
    cerebro = hashbuilder(nightcrawler, beast, storm)

    ## call API with marvelcharcall(timestamp, hash, pubkey, char)
    uncannyxmen = marvelcharcall(nightcrawler, cerebro, storm, "Wolverine")

    ## display results
    print(uncannyxmen)

## Define args to collect
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', \
      help ='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', \
      help='Provide the /path/to/file.pub containing Marvel public developer key')
    args = parser.parse_args()
    main()



