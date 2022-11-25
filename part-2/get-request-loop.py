import http.client
import pprint
import time

web_url = 'goldwin1.ir'

# def get_website(url):
#   connection = http.client.HTTPConnection(url, 80, timeout=10)
#   connection.request("GET", "/")
#   response = connection.getresponse()
#   headers = response.getheaders()
#   pp = pprint.PrettyPrinter(indent=4)
#   pp.pprint("Headers: {}".format(headers))
#   return response


# while True:
#   res = get_website(web_url)
#   print(res.headers)
#   time.sleep(5)

from http.client import HTTPSConnection
from urllib.parse import urljoin

def get(host, url):
    print(f'GET {url}')

    connection = HTTPSConnection(host)
    connection.request('GET', url)

    response = connection.getresponse()
    location_header = response.getheader('location')

    if location_header is None:
        return response
    else:
        location = urljoin(url, location_header)
        return get(host, location)

response = get('https://goldwin1.ir', '/blog')

print(response.read())