from bs4 import BeautifulSoup
from urlparse import urlparse
from contextlib import closing
from collections import defaultdict
import pprint
import urllib2

def segment(input):
    soup = BeautifulSoup(input)
 
    result = defaultdict(list)
    
    content = ""
    for seg in soup.body.find_all(["p","h2"]):
        if seg.name == "h2":
            tag = seg.contents[0]
            content = ""
        if seg.name == "p":
            if seg.a:
                url = seg.a.contents[0]
                result[tag].append({'url': url, 'content': content})
                content = ""
            else:
                if content:
                    content += "\n" 
                content += unicode(seg.contents[0])
            
    return result


def read(resource):
   pr = urlparse(resource) 

   if pr.netloc: 
       with closing(urllib2.urlopen(resource)) as fp:
           html = fp.read()
   else:
       html = resource
   return segment(html)

if __name__ == "__main__":
    # work on command line argument
    result = read(sys.argv[1])
    pprint.pprint(result)
