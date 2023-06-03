import time
from shaggy.sources import sources
from tqdm import tqdm

import multiprocessing.dummy as mp 
from multiprocessing import Array

from termcolor import colored
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0",
}


def hunt(names: list):
    # Create an empty list to store the found social media accounts
    found = []

    # Add data to the found sources if it does not exist
    def add_to_name(data):
        
        # A flag indicating that the source has already been found
        # foundSource = False
        # for s in found:
        #     if data['name'] == s['name']:
        #         foundSource = True

        # if not foundSource:
        found.append(data)

    niceNames = ""
    for i in range(len(names)):
        niceNames += names[i]
        if i < (len(names)-1):
            niceNames += ", "

    # Print a message indicating that the search is starting
    print(
        f"[{colored('🔍', 'yellow', attrs=['bold'])}] Searching for social media accounts for username(s): {colored(niceNames, 'green', attrs=['bold'])}"
    )

    def hunt_user(name: str):
        # Iterate through the sources using tqdm to display a progress bar
        for i in tqdm(sources, ascii=".#", leave=False):
            # Get the current source
            source = sources[i]

            # Generate the URL to search for the username in the current source
            url = source.get("api", source["url"]).format(name)

            try:
                # Send a GET request to the URL, if there's an exception,
                # we just go to the next source
                response = requests.get(
                    url, headers={**headers, **source.get("headers", {})}
                )
            except requests.exceptions.RequestException:
                continue

            # Create a dictionary to store the source name and URL
            data = {"name": i, "url": source["url"].format(name)}

            # Check the conditions for a valid social media account based on the source 
            # configuration
            if source.get("redirect", True) is False:
                # If the source does not allow redirects and there are no redirects in the 
                # response, consider it a valid account
                if len(response.history) == 0:
                    add_to_name(data)
            elif errorURL := source.get("errorUrl", None):
                # If an error URL is specified for the source and it's not present in the 
                # response URL, consider it a valid account
                if not (errorURL in response.url):
                    add_to_name(data)
            elif msg := source.get("errorMsg", None):
                # If an error message is specified for the source and it's not present in 
                # the response content, consider it a valid account
                if not (msg in response.content.decode("utf-8")):
                    add_to_name(data)
            elif main := source.get("urlMain", None):
                # If a main URL is specified for the source and it's different from the 
                # response URL, consider it a valid account
                if main != response.url:
                    add_to_name(data)
            else:
                # If no specific conditions are specified, consider it a valid account if 
                # the response status code is 200
                if response.status_code == 200:
                    add_to_name(data)

    p=mp.Pool(len(names))
    p.map(hunt_user,names)
    p.close()
    p.join()

    # Print a message indicating the number of found social media accounts
    print(
        f"\n[🌐] Found {colored(len(found), 'green', attrs=['bold'])} social media accounts for {colored(niceNames, 'green', attrs=['bold'])} on the following platforms:\n"
    )

    # Iterate through the found social media accounts and print their names and URLs
    for user in found:
        print(
            f"[{colored('✓', 'green', attrs=['bold'])}] {colored(user['name'], 'green', attrs=['bold'])}: {user['url']}"
        )

    return found

