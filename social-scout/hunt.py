
from sources import sources
from tqdm import tqdm

import logger

import requests
import logging

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
}

def hunt(name: str):    
    found = []
    for i in tqdm(sources, desc="Fetching accounts", leave=True):
        source = sources[i]
        url = source["url"].format(name)
        response = requests.get(url, headers=headers)

        data = { "name": i, "url": url }
        if source.get("redirect", True) == False:
            if len(response.history) == 0:
                found.append(data)
        elif main := source.get("urlMain", None):
            if main != response.url:
                found.append(data)
        elif code := source.get("errorCode", None):
            if code != response.status_code:
                found.append(data)
        elif msg := source.get("errorMsg", None):
            if not (msg in response.content.decode("utf-8")):
                found.append(data)
        else:
            raise Exception("Unknown response handle")
        
    for user in found:
        print(f"{user['name']}: {user['url']}")