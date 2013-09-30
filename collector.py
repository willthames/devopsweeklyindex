from bs4 import BeautifulSoup
from urlparse import urlparse
from contextlib import closing
from datetime import datetime
import re
import requests
import os

def download_if_newer(url, outputfile):
    if os.path.exists(outputfile):
        modified = datetime.fromtimestamp(os.path.getmtime(outputfile))
    else:
        modified = datetime.fromtimestamp(0)
    mod_date = modified.strftime('%a, %d %b %Y %H:%M:%S %Z')
    print mod_date
    r = requests.get(url, headers = { 'If-Modified-Since': mod_date })

    print "{} {}".format(r.status_code, url)
    with open(outputfile, "w") as f:
        f.write(r.text.encode('utf8'))


if __name__ == "__main__":
    html = requests.get("http://devopsweekly.com/archive").text
    soup = BeautifulSoup(html)
    for link in soup("li"):
        if re.search('Issue', str(link)):
            url = "http://devopsweekly.com" + link.a['href']
            issueno = link.a['href'].split('/')[-2].replace("issue-", "")
            outputfile = os.path.join("archive", "issueno" + ".html")
            download_if_newer(url, outputfile)
