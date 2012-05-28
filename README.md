# devopsweeklyindex

A project that could one day provide an index for http://devopsweekly.com/. 
Ideally I'd like to have indexes by keyword, by blogs referenced and by authors. 
Phase one just indexes by content.

## Important methods

`parser.read` - takes HTML from file or URL and converts it into a list of 
`{ url, content}` dicts, keyed by section name
`indexer.index` - creates a whoosh index from the results of parser.read.
