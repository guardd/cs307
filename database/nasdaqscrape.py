import requests
import csv

def scrape_nasdaq():
    headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
    }

    url = "https://api.nasdaq.com/api/screener/stocks?tableonly=true&limit=25&offset=0&download=true"
    r = requests.get(url, headers=headers)
    j = r.json()
    #print(j)
    table = j['data']
    table_headers = table['headers']

    with open('Stocks.csv', 'w', newline='') as f_output:
        csv_output = csv.DictWriter(f_output, fieldnames=table_headers.values(), extrasaction='ignore')
        csv_output.writeheader()

        for table_row in table['rows']:
            csv_row = {table_headers.get(key, None) : value for key, value in table_row.items()}
            csv_output.writerow(csv_row)