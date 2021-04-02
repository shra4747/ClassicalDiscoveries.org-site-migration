# Imports: Requests: API, JSON: Saving Data, Re: Modifying Elements, BS4: HTML Parsing
import requests
import json
import sys
import re
import os
import unicodedata
from bs4 import BeautifulSoup

fileName = str(input("File Name: "))

composerIndex = 0
workIndex = 1
performersIndex = 2
labelIndex = 3
air_timeIndex = 4

current_date = ""
current_description = ""
all_data_of_page = []

# Define URL and BS4
URL = 'http://www.classicaldiscoveries.org/playlists_2019.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Find All TDs in Tables
tables = soup.find_all('table')
tables.pop(0)

def mainSongFunc(table):
    global composerIndex
    global workIndex
    global performersIndex
    global labelIndex
    global air_timeIndex

    tds = table.find_all('td')
    ths = table.find_all('th')

    index = 0
    fullStuff = []
    currentStuff = []

    if len(ths) < 5:
        print("OK LESS THATN 5")
        trs = table.find_all("tr")
        for tr in trs:
            value = str(tr)
            if "line-height" in value and "colspan" in value:
                continue

            if 'td width="' in value:
                continue
            print("\n\n\n\n***************** Other Format TR")
            tdstr = tr.find_all('td')
            for tyty in tdstr:
                print(tyty.text)
            composer = str(input("Composer: (or skip: (s)): "))
            if composer == "s":
                continue
            currentStuff = [
                composer,
                str(input("Work: ")),
                str(input("Performers: ")),
                str(input("Label: ")),
                str(input("Air time: "))
            ]
            fullStuff.append(currentStuff)
    else:
        if "composer" in str(ths[0].text).lower():
            # Normal Table
            composerIndex = 0
            workIndex = 1
            performersIndex = 2
            labelIndex = 3
            air_timeIndex = 4
        elif "air time" in str(ths[0].text).lower():
            # Air Time Comes First
            composerIndex = 1
            workIndex = 2
            performersIndex = 3
            labelIndex = 4
            air_timeIndex = 0
        else:
            # Other Comes First
            composerIndex = int(input("Composer Index?: "))
            workIndex = int(input("Work Index?: "))
            performersIndex = int(input("Performers Index?: "))
            labelIndex = int(input("Label Index?: "))
            air_timeIndex = int(input("AirTime Index?: "))

        for td in tds:
            item = str(td.text)
            item = item.replace(u'\xa0', u' ')
            item = item.replace("\r", "")
            item = item.replace("\n", "")
            item = re.sub(' +', ' ', item)
            item = unicodedata.normalize('NFKD', item).encode(
                'ascii', 'ignore').decode()
            item = item.encode("ascii", "ignore")
            item = item.decode()
            item = item.replace("\t", "")
            item = item.strip()

            value = str(td)
            if "img" in value:
                continue

            if "line-height" in value and "colspan" in value:
                continue
                            
            if 'td width="' in value:
                continue
        
            if (re.search('[a-zA-Z]', item)) == None and re.search(r'\d', item) == None:
                item = "--"

            if index == 0:
                fullStuff.append(currentStuff)
                currentStuff = []
                index += 1
                currentStuff.append(item)
            elif index != 4:
                currentStuff.append(item)
                index += 1
            elif index == 4:
                index = 0
                currentStuff.append(item)
    
    # Remove Empty Array

    fullStuff.append(currentStuff)

    fullStuff.pop(0)

    playlist = []
    for x in fullStuff:
        if x[0] == "":
            continue

        print("\n\n\n\n\n()()()()()()()")
        print(x)
        composer = x[composerIndex]
        work = x[workIndex]
        performers = x[performersIndex]
        label = x[labelIndex]
        air_time = x[air_timeIndex]

        song = {
            "composer": composer,
            "work": work,
            "performers": performers,
            "label": label,
            "air time": air_time
        }
        playlist.append(song)

    dataSchema = {
        "date": current_date,
        "description": current_description,
        "playlist": playlist
    }
    all_data_of_page.append(dataSchema)

for table in (tables):
    strTable = str(table)
    print(strTable)
    if "playlist" in strTable.lower() and "go to" in strTable.lower():
        continue

    if "Wednesday " in strTable or "Wednesday, " in strTable:
        whatToDo = "d"
    elif "composer" in strTable.lower() and "work" in strTable.lower() and "performers" in strTable.lower():
        whatToDo = "t"
    else:
        whatToDo = str(input("Date (d), Table (t) or Skip (s)?: "))

    if whatToDo == "d":
        titletds = table.find_all('td')
        try:
            item = str(titletds[0].text)
        except:
            current_date = str(input("What is the Date?: "))
            current_description = str(input("What is the Description?: "))
        item = item.replace(u'\xa0', u' ')
        item = item.replace("\r", "")
        item = item.replace("\n", "")
        item = re.sub(' +', ' ', item)
        item = item.encode("ascii", "ignore")
        item = item.decode()

        if item == "":
            continue
        elif item[0] == " ":
            item = item[1:]

        if item[(len(item))-1] == " ":
            item = item[:-1]

        size = len(((str(item).split(":00", 1)[0])))
        date = ((str(item).split(":00", 1)[0])[:size - 4])
        try:
            description = ((str(item).split(":00", 1)[1])[8:])
        except:
            print("\n\n\n")
            print(item)
            description = ""
            i = input("ERROR ABOVE??")
        try:
            if description == "":
                pass
            elif description[0] == " ":
                description = description[1:]
        except:
            print(description)
            print("Error")
        current_date = date
        current_description = description
    elif whatToDo == "t":
        mainSongFunc(table)
    elif whatToDo == "s":
        "OK Skipping"
        continue
    else:
        sys.exit("ERROR!")

with open(f'/Users/shravanp/Coding/FOP/Big-Projects/DrRosen/YearDataJSON/{fileName}.json', 'w') as fout:
    json.dump(all_data_of_page, fout)
