
from sources import sources

from tqdm import tqdm
from termcolor import colored

import logger

import requests
import logging

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
}

def hunt(name: str):    
    found = []
    print(f"[{colored('🔍', 'yellow', attrs=['bold'])}] Searching for social media accounts for username: {colored(name, 'green', attrs=['bold'])}\n")

    for i in tqdm(sources, desc="Fetching accounts", leave=False):
        source = sources[i]
        url = source.get("api", source["url"]).format(name)
        response = requests.get(url, headers=headers)

        data = { "name": i, "url": source["url"].format(name) }
        if source.get("redirect", True) is False:
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

    print(f"\n[🌐] Found {colored(len(found), 'green', attrs=['bold'])} social media accounts for {colored(name, 'green', attrs=['bold'])} on the following platforms:\n")
        
    for user in found:
        print(f"[{colored('✓', 'green', attrs=['bold'])}] {colored(user['name'], 'green', attrs=['bold'])}: {user['url']}")

    print("\n✨ Happy connecting and exploring! ✨")