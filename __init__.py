"""
HTB API Wrapper for HnH
Author: Nate Singer
Depends:
    import: requests (pip install requests)
    import: json (should come out of the box with python3)
    file: server.apikey (create this in the relative root and place server's API key on line 1)
"""
import requests
import json

version='v0.1'

class HnHBartender:
    def __init__(self):
        with open('server.apikey','r') as f: self.api_key = f.read() #pull in API key
        self.base_url = 'https://www.hackthebox.eu/api'

    def __build_headers(self, *argv):
        header = {'User-Agent':'HnH_API_WRAPPER_' + version} #build user agent as base of header chain
        for arg in argv:
            header.update(arg)
        return header

    def get_all_machines(self):
        response=requests.get('{}/machines/get/all/?api_token={}'.format(self.base_url, self.api_key), headers=self.__build_headers())
        print("Code: {}, Response: {}".format(response, response.json()))

    def get_user_id(self, member=None):
        u = "{}/user/id?api_token={}".format(self.base_url, self.api_key)
        d = {'username':'{}'.format(member)}
        h = self.__build_headers({'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8'})

        response=requests.post(u, data=d, headers=h)
        print("Code: {}, Response: {}".format(response, response.content))

bartender = HnHBartender()
bartender.get_all_machines()
bartender.get_user_id('rudem')


"""
Queries for potential future use:
    {base}/machines/owns/?api_token={apitoken} //this gives the owned machines of the user who's API key is passed
"""
