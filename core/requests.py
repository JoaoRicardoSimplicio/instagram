import json
import random

import requests


class Request:

    def __init__(self, sessionid: str = None, *args, **kwargs) -> None:
        self.session = requests.Session()
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Referer": "https://www.instagram.com/",
            "Origin": "https://www.instagram.com",
            "X-IG-App-ID": "936619743392459",
        }

        if sessionid:
            self.session.cookies.set("sessionid", sessionid, domain=".instagram.com")

        self.session.headers.update(**self.headers)

    def add_headers(self, headers: dict) -> None:
        self.session.headers.update(headers)

    def set_cookie(self, key, value):
        self.session.cookies.set(key, value)

    def post(self, url, data=None, json=None):
        response = self.session.post(
            url=url,
            data=data,
            json=json
        )

        return response

    def get(self, url, params=None):
        response = self.session.get(
            url=url,
            params=params
        )

        return response
