from bs4 import BeautifulSoup
import requests
import json
from readability import Document

api_prefix = "http://api.glassdoor.com/api/api.htm?"

class GetCompany:
    params = {"v": 1, "format": 'json', "t.p": 99384, "t.k": "bvReWCBITHk", "userip": "0.0.0.0",
             "useragent": "Mozilla/%2F4.0", "action": "employers", "q": "nvidia"}
    #gd = None

    def __init__(self, company):
        self.params['q'] = company
        user_agent = {'User-agent': 'Mozilla/5.0'}
        url = self.api_request_generate()
        resp = requests.get(url, headers=user_agent)
        decoder = json.JSONDecoder()
        self.gd = decoder.decode(resp.text)

    def api_request_generate(self):
        prefix = api_prefix
        for key in self.params:
            prefix = prefix + key + "=" + str(self.params[key]) + "&"

        print(prefix[:-1])
        return prefix[:-1]

    def success_check(self):
        """Returns bool if the request was processed successfully"""
        return self.gd['success']

    def get_status(self):
        """Returns the status of the request"""
        return self.gd['status']

    def get_response(self):
        """Returns json response from server"""
        return self.gd['response']


def main():

    new = GetCompany("nvidia")
    old = GetCompany("ibm")

    print(new.get_status())
    print(new.get_response())
    print(old.get_response())
    #print(test['name'])
    #print(doctest.title())
    #print(html)





if __name__ == '__main__':
    main()
