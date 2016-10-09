# Fileswitcher for testing
import os
import os.path as op
import argparse
from bs4 import BeautifulSoup
from subprocess import Popen
import requests
import json
import sys
import pprint
from details.models import details

api_prefix = "http://api.glassdoor.com/api/api.htm?"

def api_request_generate(params):
    prefix = api_prefix
    for key in params:
        prefix = prefix + key + "=" + str(params[key]) + "&"

    print(prefix[:-1])
    return prefix[:-1]

def getCompanyList():

    prams = {"v":1, "format":'json', "t.p": 99384, "t.k":"bvReWCBITHk", "userip":"0.0.0.0", "useragent":"Mozilla/%2F4.0", "action":"employers"}
    url = api_request_generate(prams)
    user_agent = {'User-agent': 'Mozilla/5.0'} #useragent workaroudn

    r = requests.get(url, headers=user_agent)
    json_data = json.loads(r.text)

    pp = pprint.PrettyPrinter(indent=4)
    theList = [x['name'] for x in json_data['response']['employers']]

    for c in theList:
        details.objects.get_or_create(company_name = c)


def getCompanyInfo(nameOfCompany):
    prams = {"v":1, "format":'json', "t.p": 99384, "t.k":"bvReWCBITHk", "userip":"0.0.0.0", "useragent":"Mozilla/%2F4.0", "action":"employers"}
    url = api_request_generate(prams)
    user_agent = {'User-agent': 'Mozilla/5.0'} #useragent workaroudn

    r = requests.get(url, headers=user_agent)
    json_data = json.loads(r.text)

    pp = pprint.PrettyPrinter(indent=4)
    theList = [x['name'] for x in json_data['response']['employers']]

    return theList

if __name__ == '__main__':
    getCompanyInfo()
