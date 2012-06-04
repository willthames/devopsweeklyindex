from bs4 import BeautifulSoup
from urlparse import urlparse
from contextlib import closing
from collections import defaultdict
import pprint
import urllib2
import string
import sys
import re

def strip_extra_whitespace(content):
    return re.sub(r'[ \t\n]+', r' ', content)

def fix_apostrophes(content):
    return re.sub(u'\u2019', u"'", content)

def segment(input):
    soup = BeautifulSoup(input)

    # strip out span tags
    for tag in soup("span"):
        tag = tag.unwrap()
 
    result = defaultdict(list)
    
    content = ""
    for seg in soup.body.find_all(["p","h2"]):
        if seg.name == "h2":
            tag = seg.contents[0]
            content = ""
        if seg.name == "p":
            if seg.a:
                url = seg.a.contents[0]
                # strip out unnecessary additional white space (particularly newlines)
                content = strip_extra_whitespace(content)
                content = fix_apostrophes(content)
                result[tag].append({'url': url, 'content': content })
                content = ""
            else:
                if content:
                    content += " " 
                content += string.join(map(unicode, seg.contents), " ")
            
    return result


def read(resource):
   pr = urlparse(resource) 

   if pr.netloc: 
       with closing(urllib2.urlopen(resource)) as fp:
           html = fp.read()
   else:
       with open(resource) as fp:
           html = fp.read()
   return segment(html)

if __name__ == "__main__":
    # work on command line argument
    result = read(sys.argv[1])
    pprint.pprint(result)
