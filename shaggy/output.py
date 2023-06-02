
import csv

def output_accounts(output: str, accounts: list):
    with open(output, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for user in accounts:
            spamwriter.writerow([ user['name'], user['url'] ])
