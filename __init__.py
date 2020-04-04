"""
HTB API Wrapper for HnH
Author: Nate Singer
Depends:
    requests (pip install requests)
"""
import requests

wrapper_version='v0.1'

class HnHBartender:
    user_agent='HnH_API_WRAPPER_' + wrapper_version
    base_url='https://www.hackthebox.eu/api'

    def __init__(self, pass_api_key=None, pass_user_agent=user_agent, pass_base_url=base_url):
        self.api_key = pass_api_key
        self.headers = {'User-Agent':pass_user_agent}
        self.api_base_url = pass_base_url

    def __auth(self, pass_path):
        return pass_path + '?api_token=' + self.api_key

    def query_example(self):
        response=requests.get(self.base_url + self.__auth('/machines/owns/'), headers=self.headers)
        print(response.json())

request = HnHBartender()
request.query_example()
