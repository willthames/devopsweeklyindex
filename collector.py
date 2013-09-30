from bs4 import BeautifulSoup
from urlparse import urlparse
from contextlib import closing
import urllib2
import re

def read(resource):
    pr = urlparse(resource) 

    with closing(urllib2.urlopen(resource)) as fp:
        html = fp.read()
    return html

if __name__ == "__main__":
    html = read("http://devopsweekly.com/archive")
    soup = BeautifulSoup(html)
    for link in soup("li"):
        if re.match('issue', link):
            html = read("http://devopsweekly.com" + link.a['href'])
            with open("archive/" + link.a['href'].split('/')[-2] + ".html") as fp:
                fp.write(html)
