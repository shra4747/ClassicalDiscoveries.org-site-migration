# Imports: Requests: API, JSON: Saving Data, Re: Modifying Elements, BS4: HTML Parsing
import requests
import json
import re
import os
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
    tds = table.find_all('td')
    index = 0
    fullStuff = []
    currentStuff = []

    for td in tds:
        item = str(td.text)

        item = item.replace(u'\xa0', u' ')
        item = item.replace("\r", "")
        item = item.replace("\n", "")
        item = re.sub(' +', ' ', item)

        try:
            if item == "" or item == None:
                continue
            elif item[0] == " ":
                item = item[1:]

            if item[(len(item))-1] == " ":
                item = item[:-1]
        except:
            print("SOMETHING WRONG v OK!")

        print(item)
        if index == 0:
            fullStuff.append(currentStuff)
            currentStuff = []
            index += 1
            currentStuff.append(item)
        elif index != 4:
            currentStuff.append(item)
            index += 1
        else:
            index = 0
            currentStuff.append(item)

    # Remove Empty Array
    fullStuff.pop(0)

    playlist = []

    for x in fullStuff:
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
        print(song)
        playlist.append(song)

    dataSchema = {
        "date": current_date,
        "description": current_description,
        "playlist": playlist
    }
    all_data_of_page.append(dataSchema)


print("ready")
for table in (tables):
    print(str(table))
    usage = input("Usage??: ")
    if usage == "n" or usage == "d":
        fieldIndex = "n"
    else:
        fieldIndex = input("Fields Normal or Custom (a for airtime first!)?:")
    if fieldIndex == "n":
        composerIndex = 0
        workIndex = 1
        performersIndex = 2
        labelIndex = 3
        air_timeIndex = 4
    elif fieldIndex == "a":
        composerIndex = 1
        workIndex = 2
        performersIndex = 3
        labelIndex = 4
        air_timeIndex = 0
    elif fieldIndex == "c":
        composerIndex = int(input("Composer Index:"))
        workIndex = int(input("Work Index:"))
        performersIndex = int(input("Performers Index:"))
        labelIndex = int(input("Label Index:"))
        air_timeIndex = int(input("Air Time Index:"))

    if usage == "d":
        titletds = table.find_all('td')
        item = str(titletds[0].text)
        item = item.replace(u'\xa0', u' ')
        item = item.replace("\r", "")
        item = item.replace("\n", "")
        item = re.sub(' +', ' ', item)
        if item == "":
            continue
        elif item[0] == " ":
            item = item[1:]

        if item[(len(item))-1] == " ":
            item = item[:-1]

        size = len(((str(item).split(":00", 1)[0])))
        date = ((str(item).split(":00", 1)[0])[:size - 4])
        description = ((str(item).split(":00", 1)[1])[8:])
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
    elif usage == "s":
        mainSongFunc(table)
    elif usage == "n":
        print("### OK RUNNING None")
    else:
        print("ERRORORORORORO #*#*#**#*#*#*#**#*##**#**#*#***#*#")


print(all_data_of_page)
with open(f'{fileName}.json', 'w') as fout:
    json.dump(all_data_of_page, fout)
