import requests

class Apollo:
    email = "michael@weworksales.tech" # working apollo account
    password = "Michaelweworksalestech1*"
    headers = {
        'authority': 'app.apollo.io',
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.9',
        'cache-control': 'no-cache',
        'content-type': 'application/json',
        'origin': 'https://app.apollo.io',
        'pragma': 'no-cache',
        'referer': 'https://app.apollo.io/',
        'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        'x-csrf-token': 'oZPE5_gsVfgqZDbX1QfHqEI4vBmPgkI_KBHB_d6ZL_CK3SQl1IMrZkVHpw-l6deoDwHk-2aMF0QxY3-uuM43Yg',
    }

    def __init__(self):
        "Create a login session for apollo."
        json_data = { 'email': self.email, 'password': self.password, 'timezone_offset': -240 }
        self.s = requests.Session()
        self.s.headers.update(self.headers)
        self.s.post('https://app.apollo.io/api/v1/auth/login', json=json_data)
    
    def search(self, payload):
        "Search on /mixed_people/search with payload."
        resp = self.s.post('https://app.apollo.io/api/v1/mixed_people/search', json=payload)
        print(resp.status_code)
        return resp.json()
    
    def req(self, url, json_data=None, params=None, method="post"):
        "Make a request using Apollo session."
        res = self.s.request(url=url, method=method, data=json_data, params=params)
        return res.json()