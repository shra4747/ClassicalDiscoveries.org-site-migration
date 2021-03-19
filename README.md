# Dr. Rosen Project        
![PYTHON](https://img.shields.io/badge/Python->v3-brightgreen?style=for-the-badge) ![HTML](https://img.shields.io/badge/HTML-5-orange?style=for-the-badge) ![VERSION](https://img.shields.io/badge/VERSION-0.1-blue?style=for-the-badge) ![PLATFORM](https://img.shields.io/badge/Platform-MacOS,%20Windows,%20Linux-lightgray?style=for-the-badge) ![LATEST](https://img.shields.io/badge/Latest%20update-2021/3/18-red?style=for-the-badge)

### New and Previous Song Search

IN PROGRES: Phase 1 - Data Migration

![alt text](http://www.classicaldiscoveries.org/images/ClassDiscLogoWhole.jpg "Classical Discoveries Logo")


## Installation:

1. First, visit the releases page and download the latest release source code zip.
 
  (https://github.com/shra4747/DrRosen/releases)
 
2. CD into the directory of downloaded zip.

##### Mac (Replace USER with your user)
```shell
cd ~/Users/USER/Desktop/DrRosen
```

##### Windows (Replace USER with your user)
```shell
cd C:\Users\USER\Desktop\DrRosen
```

##### Linux (Replace USER with your user)
```shell
cd /home/USER/Desktop/DrRosen
```

3. Unzip the file
```shell
unzip DrRosen-0.1.zip
```

## Web Scraping:

1. Run webscraper.py
```python
python3 webscraper.py
```

**The saved location of the JSON Data is YearDataJSON/----.json

## Convert JSON to HTML:

1. Run dataToHTML.py and set the output to a text file in EndTextResults.
```python
python3 webscraper.py > EndTextResults/----.txt
```

2. CD into EndTextResults and open the file you just created. 
```shell
cd EndTextResults
open ----.txt
```

3. Copy and Paste that text into the HTML input on GoDaddy-WordPress-BeaverBuilder


