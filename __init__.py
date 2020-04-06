"""
HTB API Wrapper for HnH
Author: Nate Singer, Jack Lambert
Depends:
    import: requests (pip install requests)
    file: server.apikey (create this in the relative root and place server's API key on line 1)
"""
import requests

version = 'v0.1'


class machines:
    def __init__(self):
        with open('server.apikey', 'r') as f: self.api_key = f.read()  # pull in API key
        self.base_url = 'https://www.hackthebox.eu/api'

    def __build_headers(self, *argv):
        header = {'User-Agent': 'HnH_API_WRAPPER_' + version}  # build user agent as base of header chain
        for arg in argv:
            header.update(arg)
        return header

    def _get(self, request_obj):
        r = requests.get('{}{}/?api_token={}'.format(self.base_url, request_obj, self.api_key),
                         headers=self.__build_headers())

        if r.status_code == 200:
            return r.json()
        else:
            return

    def getall(self):
        request_obj = "/machines/get/all"
        return (self._get(request_obj))

    def getboxbyid(self, machine_id):
        request_obj = f"/machines/get/{str(machine_id)}"
        return (self._get(request_obj))

    def getboxbyname(self, search_for):
        all_boxes = self.getall()
        for i in all_boxes:
            if i['name'] == search_for:
                return i
        return

    def os(self, s):
        r = self.field(s, "os")
        return r

    def ip(self, s):
        r = self.field(s, "ip")
        return r

    def points(self, s):
        r = self.field(s, "points")
        return r

    def released(self, s):
        r = self.field(s, "release")
        return r

    def retired(self, s):
        r = self.field(s, "retired_date")
        return r

    def maker(self, s):
        r = self.field(s, "maker")
        # r.append self.field(s, "maker2")
        return r

    def rating(self, s):
        r = self.field(s, "rating")
        return r

    def userowns(self, s):
        r = self.field(s, "user_owns")
        return r

    def rootowns(self, s):
        r = self.field(s, "root_owns")
        return r

    def isretired(self, s):
        r = self.field(s, "retired")
        return r

    def isfree(self, s):
        r = self.field(s, "retired_date")
        return r

    def retired(self, s):
        r = self.field(s, "retired_date")
        return r

    def field(self, search_for, field):
        if isinstance(search_for, str):
            r = self.getboxbyname(search_for)
        else:
            r = self.getboxbyid(search_for)
        return r[field]


class member:
    def __init__(self):
        with open('server.apikey', 'r') as f: self.api_key = f.read()  # pull in API key
        self.base_url = 'https://www.hackthebox.eu/api'

    def __build_headers(self, *argv):
        header = {'User-Agent': 'HnH_API_WRAPPER_' + version}  # build user agent as base of header chain
        for arg in argv:
            header.update(arg)
        return header

    def _get(self, request_obj, request_data=None):
        r = requests.get('{}{}/?api_token={}'.format(self.base_url, request_obj, self.api_key),
                         headers=self.__build_headers())

        if r.status_code == 200:
            return r.json()
        else:
            return

    def _post(self, request_obj, request_data=None):
        r = requests.post('{}{}/?api_token={}'.format(self.base_url, request_obj, self.api_key), data=request_data,
                          headers=self.__build_headers(
                              {'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'}))

        if r.status_code == 200:
            return r.json()
        else:
            return

    def id(self, member=None):
        request_obj = "/user/id"
        request_data = {'username': '{}'.format(member)}
        r = self._post(request_obj, request_data)
        return r['id']


def main():
    m = machines()
    u = member()
    a = m.maker('Lame')
    print(a)


if __name__ == "__main__":
    main()

"""
Queries for potential future use:
    {base}/machines/owns/?api_token={apitoken} //this gives the owned machines of the user who's API key is passed
"""
