from whoosh.index import create_in, exists_in, open_dir
from whoosh.fields import * 
import parser
import pprint
import os


def get_schema():
    return Schema(id=ID,
                  section=TEXT(stored=True),
                  url=TEXT(stored=True), 
                  content=TEXT(stored=True))


def get_index():
    """ Return an index
    creates index if empty
    
    """ 
    if not exists_in("index", indexname="contents"):
        if not os.path.exists("index"):
            os.mkdir("index")
        create_in("index", indexname="contents", schema=get_schema())
    return open_dir("index", indexname="contents") 


def check_for_presence(ix, segments):
    """ Tests whether segments has already been indexed
    Keyword arguments: 
    ix: index
    segments: dict with section keys of { url, content} pair arrays
    
    """
    return False


def add_to_index(writer, segment, section, resource):
    """ Adds a segment to an index
    Keyword arguments: 
    writer: IndexWriter
    segment: url, content pair
    section: section of content
    resouce: original resource of content
    """
    writer.add_document(id=unicode(resource),
                        section=section,
                        url=segment['url'],
                        content=segment['content'])


def index(resource, reindex=False):
    segments = parser.read(resource)
    
    ix = get_index()
    writer = ix.writer()
    
    if not check_for_presence(ix, segments) or reindex:
        for title in segments:
            for segment in segments[title]:
                if segment.get("content") and segment.get("url"): 
                    add_to_index(writer, segment, title, resource)
    writer.commit()
 
    return(ix)


if __name__ == "__main__":
    # work on command line argument
    for arg in sys.argv[1:]:
        index(arg)
    result = get_index()
    with result.searcher() as searcher:
        docnums = searcher.document_numbers()
        pprint.pprint(searcher.key_terms(docnums, "content", numterms=1000))
