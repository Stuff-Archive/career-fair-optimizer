from bs4 import BeautifulSoup
import requests
import json
from readability import Document

api_prefix = "http://api.glassdoor.com/api/api.htm?"

class GetCompany:
    params = {"v": 1, "format": 'json', "t.p": 99384, "t.k": "bvReWCBITHk", "userip": "0.0.0.0",
             "useragent": "Mozilla/%2F5.0", "action": "employers", "q": "nvidia"}
    #gd = None

    def __init__(self, company):
        self.params['q'] = company
        user_agent = {'User-agent': 'Mozilla/5.0'}
        url = self.api_request_generate()
        resp = requests.get(url, headers = user_agent)
        print(resp.text)
        decoder = json.JSONDecoder()
        self.gd = decoder.decode(resp.text)
        self.response = self.gd['response']
        self.employers = self.response['employers']

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

    def is_exact_match(self):
        return self.employers[0]['exactMatch']

    def get_company(self):
        return self.employers[0]

class Company:
    def __init__(self, company):
        self.comp = company

    def get_name(self):
        return self.comp['name']

    def get_website(self):
        return self.comp['website']

    def get_industry(self):
        return self.comp['industry']

    def get_overallrating(self):
        return self.comp['overallRating']

    def get_cultureandvaluesrating(self):
        return self.comp['cultureAndValuesRating']

    def get_leadershiprating(self):
        return self.comp['seniorLeadershipRating']

    def get_compensationrating(self):
        return self.comp['compensationAndBenefitsRating']

    def get_workliferating(self):
        return self.comp['workLifeBalanceRating']

    def get_sectorname(self):
        return self.comp['sectorName']

    def get_logo(self):
        return self.comp['squareLogo']

    def get_featuredreview(self):
        return self.comp['featuredReview']

    def get_ceo(self):
        return self.comp['ceo']



def main():

    n = GetCompany("nvidia")

    print(n.get_response())
    print(n.get_status())
    print(n.is_exact_match())

    c = Company(n.get_company())

    print(c.get_name())
    print(c.get_overallrating())
    print(c.get_industry())
    print(c.get_sectorname())
    print(c.get_compensationrating())
    print(c.get_cultureandvaluesrating())
    print(c.get_leadershiprating())
    print(c.get_workliferating())
    print(c.get_website())
    print(c.get_logo())
    print(c.get_featuredreview())
    print(c.get_ceo())




if __name__ == '__main__':
    main()
