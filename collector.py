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
        if re.search('Issue', str(link)):
            url = "http://devopsweekly.com" + link.a['href']
            html = read(url)
            print "Downloading " + url
            outputfile = link.a['href'].split('/')[-2] + ".html"
            with open("archive/" + outputfile.replace("issue-", ""), "w") as fp:
                fp.write(html)
