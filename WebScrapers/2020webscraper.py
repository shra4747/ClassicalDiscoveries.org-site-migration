# Imports: Requests: API, JSON: Saving Data, Re: Modifying Elements, BS4: HTML Parsing
import requests
import json
import sys
import re
import os
from bs4 import BeautifulSoup


weirdformat = False


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
URL = 'http://www.classicaldiscoveries.org/playlists_2021.html'
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
        item = item.encode("ascii", "ignore")
        item = item.decode()

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
        print(index)
        print("\n\n\n\n")

        if weirdformat and "September 09" in str(current_date):
            if index == 0:
                fullStuff.append(currentStuff)
                currentStuff = []
                index += 1
                currentStuff.append(item)
            elif index == 1:
                currentStuff.append(item)
                index += 1

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

    print(currentStuff)
    # Remove Empty Array

    fullStuff.append(currentStuff)

    print(fullStuff)
    fullStuff.pop(0)

    playlist = []

    if "December 02" in str(current_date) or "November" in str(current_date) or "October" in str(current_date) or "September 30" in str(current_date) or "September 23" in str(current_date) or "September 16" in str(current_date):
        composerIndex = 1
        workIndex = 2
        performersIndex = 3
        labelIndex = 4
        air_timeIndex = 0
    else:
        composerIndex = 0
        workIndex = 1
        performersIndex = 2
        labelIndex = 3
        air_timeIndex = 4

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
        playlist.append(song)

    dataSchema = {
        "date": current_date,
        "description": current_description,
        "playlist": playlist
    }
    all_data_of_page.append(dataSchema)


for table in (tables):
    strTable = str(table)

    if "Wednesday, " in strTable or "Thursday, " in strTable or "Friday, " in strTable or "Saturday, " in strTable or "Sunday, " in strTable or "Monday, " in strTable or "Tuesday, " in strTable:
        if "May" in str(strTable) or "June" in str(strTable) or "July" in str(strTable) or "August" in str(strTable) or "September 02" in str(strTable) or "September 07" in str(strTable) or "September 09" in str(strTable):
            weirdformat = True

        titletds = table.find_all('td')
        item = str(titletds[0].text)
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
    elif "Composer" in strTable or "composer" in strTable:
        mainSongFunc(table)
    else:
        print(str(table))
        i = input("CORRECT?? ")
        if i == "n":
            usage = str(input("What is it? "))
            if usage == "d":
                titletds = table.find_all('td')
                item = str(titletds[0].text)
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


with open(f'/Users/shravanp/Coding/FOP/Big-Projects/DrRosen/YearDataJSON/{fileName}.json', 'w') as fout:
    json.dump(all_data_of_page, fout)
