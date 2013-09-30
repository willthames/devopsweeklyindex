# devopsweeklyindex

A project that could one day provide an index for http://devopsweekly.com/. 
Ideally I'd like to have indexes by keyword, by blogs referenced and by authors. 
# How to build and run the index
It's probably best to do this in a virtualenv
```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Once that's done, then collect the docs and index them
```
python collector.py 
python indexer.py archive/*
```
Then just run the flask app using
```
python devopsweeklyindex/__init.py
```
(there may be a nicer way than that)
