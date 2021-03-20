# Imports: Requests: API, JSON: Saving Data, Re: Modifying Elements, BS4: HTML Parsing
import requests
import json
import sys
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

    if "February 17" in str(current_date) or "February 10" in str(current_date) or "February 13" in str(current_date):
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
    # usage = input("Usage??: ")
    # if usage == "n" or usage == "d":
    #     fieldIndex = "n"
    # else:
    #     fieldIndex = input("Fields Normal or Custom (a for airtime first!)?:")
    # if fieldIndex == "n":
    #     composerIndex = 0
    #     workIndex = 1
    #     performersIndex = 2
    #     labelIndex = 3
    #     air_timeIndex = 4
    # elif fieldIndex == "a":
    #     composerIndex = 1
    #     workIndex = 2
    #     performersIndex = 3
    #     labelIndex = 4
    #     air_timeIndex = 0
    # elif fieldIndex == "c":
    #     composerIndex = int(input("Composer Index:"))
    #     workIndex = int(input("Work Index:"))
    #     performersIndex = int(input("Performers Index:"))
    #     labelIndex = int(input("Label Index:"))
    #     air_timeIndex = int(input("Air Time Index:"))


# print(all_data_of_page)
with open(f'/Users/shravanp/Coding/FOP/Big-Projects/DrRosen/YearDataJSON/{fileName}.json', 'w') as fout:
    json.dump(all_data_of_page, fout)
