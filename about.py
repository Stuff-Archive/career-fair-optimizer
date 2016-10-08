# Fileswitcher for testing
import os
import os.path as op
import argparse
from bs4 import BeautifulSoup
from subprocess import Popen
import requests
import json
from readability import Document
import sys


api_prefix = "http://api.glassdoor.com/api/api.htm?"

def api_request_generate(params):
    prefix = api_prefix
    for key in params:
        prefix = prefix + key + "=" + str(params[key]) + "&"

    print(prefix[:-1])
    return prefix[:-1]



def main():

    prams = {"v":1, "format":'json', "t.p": 99384, "t.k":"bvReWCBITHk", "userip":"0.0.0.0", "useragent":"Mozilla/%2F4.0", "action":"employers"}

    url = api_request_generate(prams)

    user_agent = {'User-agent': 'Mozilla/5.0'} #useragent workaroudn


    "?v=1&format=json&t.p=120&t.k=fz6JLNDfgVs&action=employers&q=pharmaceuticals&userip=192.168.43.42&useragent=Mozilla/%2F4.0"


    #parser = argparse.ArgumentParser(description='Switch the appropriate file for testing via symbolic link.')
    #parser.add_argument('integers', type=int, nargs=1, help='index of file to switch')

    r = requests.get(url, headers=user_agent)

    #doctest = Document(r.text)
    #soup = BeautifulSoup(r.text, "html.parser")


    #print(r.text)

    decoder = json.JSONDecoder()
    arr = decoder.decode(r.text)
    for x in arr:
        print(x)
    #print(doctest.title())
    #print(html)



if __name__ == '__main__':
    main()
