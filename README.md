vb3_7_scraper
=============

VBulletin forum scraper using python.  This has been tailored for www.s2forum.com, the spiders can easily be updated for other sites

Experimenting with python scrapey to extra forums, threads and posts from VBulletin forum pre API

Installation
============

1. Setup virtual environment if you prefer
2. Using easy nstall: 
    *scrapy
    *scrapyd
    
   You may also need to install dependent packages to compile on Ubuntu 14.04:
   sudo apt-get install libxml2-dev libxslt1-dev python-dev build-essential lib32z1-dev gccxml libffi-dev libssl-dev

Usage
=====

Generating a list of forums

```
scrapy crawl s2forum_forum -a user=<username> -a password=<password>
```

