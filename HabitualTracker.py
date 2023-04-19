import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb
import sys
import re
import random
from itertools import count,cycle
from time import sleep
from pyfiglet import Figlet
from datetime import datetime,timedelta


def heatmap(data):
    weekdays = [[], [], [], [], [], [], []]
    y = ['S', 'M', 'T', 'W', 'T', 'F', 'S']

    date = datetime.strptime(data['date'][0], '%Y-%m-%d')  # left
    number = int(date.strftime('%w'))

    for i in range(number):  # fill in missing weekdays on left
        weekdays[i].append(0)

    for d, n in zip(data.date, data['scale']):  # correspond scale values to weekdays
        day = datetime.strptime(d, '%Y-%m-%d')
        weekdays[int(day.strftime('%w'))].append(n)

    longest = 0
    for i in range(len(weekdays)):  # right
        if len(weekdays[i]) > longest:
            longest = len(weekdays[i])

    for i in range(len(weekdays)):  # equalize the length of right
        if len(weekdays[i]) != longest:
            weekdays[i].append(0)

    heatmap = np.array(weekdays)
    sb.heatmap(heatmap, cmap='Reds', linewidth=0.5, linecolor='azure', yticklabels=y)
    plt.ylabel("Weekdays")
    plt.xlabel("weeks")
    plt.show()

def bar(data):
    month = []
    scale = []
    length = len(data)  # length of date and scale is always the same

    plt.ylabel('Scale')

    if len(data) > 28:
        for i in range(28, 0, -1):
            month.append(28 - i)
            scale.append(data.scale[length - i])

        date = datetime.strptime(data.date[length - 1], '%Y-%m-%d').strftime('%B')

        plt.xlabel('the last 28 days starting from the month of ' + date)
        plt.bar(month, scale, color='maroon')
    else:
        for i in range(length, 0, -1):
            month.append(length - i)
            scale.append(data.scale[length - i])

        date = datetime.strptime(data.date[length - 1], '%Y-%m-%d').strftime('%B')
        plt.xlabel('the last ' + str(length) + ' days starting from the month of ' + date)

    plt.bar(month, scale, color='maroon')
    plt.show()

def line(data):
    month = []
    scale = []
    length = len(data)  # length of date and scale is always the same

    plt.ylabel('Scale')

    if len(data) > 28:
        for i in range(28, 0, -1):
            month.append(28 - i)
            scale.append(data.scale[length - i])

        date = datetime.strptime(data.date[length - 1], '%Y-%m-%d').strftime('%B')
        plt.xlabel('the last 28 days starting from the month of ' + date)
        plt.plot(month, scale, color = 'maroon')

    else:
        for i in range(length, 0, -1):
            month.append(length - i)
            scale.append(data.scale[length - i])

        date = datetime.strptime(data.date[length - 1], '%Y-%m-%d').strftime('%B')
        plt.xlabel('the last ' + str(length) + ' days starting from the month of ' + date)

    plt.plot(month, scale, color = 'maroon')
    plt.show()

def hint(csv, type):
    return (
        'Hint: you can also give arguments for a quicker result, python habitualtracker.py '
        + csv
        + ' '
        + type.capitalize()
    )

def parse(csv):
    if re.search('^\w+\.csv$', csv):
        return True
    else:
        return False

def check_title(data):  # check if data is in proper format "Date,scale"
    format = ['date', 'scale']
    for title, correct in zip(data, format):
        if title != correct:
            return True
    return False


def resort_weekdays(first):   # resort the weekdays starting from first
    weekdays = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday',
    ]
    if first != 0:
        tmp = []
        for i in range(6):
            if first == 6:
                tmp.append(weekdays[first])
                first = 0
                tmp.append(weekdays[first])
            else:
                tmp.append(weekdays[first])
            first = first + 1
        weekdays = tmp
    return weekdays


def check_data(data):  # doesnt check the year
    try:
        weekdays = resort_weekdays(
            int(datetime.strptime(data['date'][0], '%Y-%m-%d').strftime('%w'))
        )
    except:
        return True

    for weekday, n in zip(
        data.date, cycle(weekdays)
    ):  # check for flaws in data like missing days or days repeating
        weekday = datetime.strptime(weekday, '%Y-%m-%d').strftime('%A')
        if weekday != n:
            return True

    return False


def organize_data(data):  # has limitations like cant check if scale number is NONE or if theres lacking of commas
    tmp = []
    temp = []

    for date, number in zip(data.date, data.scale):# put data on temporary lists
        tmp.append(date)
        temp.append(float(number))

    dates = []
    scales = []

    for i in range(len(data)):# organize data
        if i == 0:
            dates.append(tmp[i])#for the first day
            scales.append(temp[i])
            continue


        if tmp[i] == tmp[i - 1]:#if the current day equals the day before

                scales[len(scales) - 1] += temp[i]   #repeating day

        elif tmp[i] != (datetime.strptime(tmp[i - 1], "%Y-%m-%d") + timedelta(days=1)).strftime("%Y-%m-%d"):#if the current day doesnt equal the day before plus time delta 1

            for j in count(1): # missing days
                missday = datetime.strptime(tmp[i - 1], "%Y-%m-%d") + timedelta(days=j)
                if missday.strftime("%Y-%m-%d") == tmp[i]:
                    break
                dates.append(missday.strftime("%Y-%m-%d"))
                scales.append(0.0)
            dates.append(tmp[i])#the current day
            scales.append(temp[i])
        else:

            dates.append(tmp[i])#normal day
            scales.append(temp[i])


    newdata = pd.DataFrame()
    newdata['date'] = dates
    newdata['scale'] = scales

    return newdata


def main():
    if len(sys.argv) == 1:
        figlet = Figlet()

        fonts = [
            'fender',
            'stampatello',
            'larry3d',
            'ogre',
            'graffiti',
            'smscript',
            'smslant',
            'epic',
            'standard',
            'slant',
            'cursive',
            'wavy',
            'isometric2',
            'isometric4',
            'invita',
            'speed',
            'shadow',
            'larry3d',
            'drpepper',
            'starwars',
            'cyberlarge',
        ]

        randomfont = random.choice(fonts)
        figlet.setFont(font=randomfont)

        print(figlet.renderText('-------------'))
        print(figlet.renderText('Welcome to Habitual Tracker'))
        print(figlet.renderText('-------------'))
        sleep(2)

        figlet.setFont(font='cybermedium')
        csv = input(figlet.renderText('whats the name of the csv file?'))

        if not parse(csv):
            sys.exit(figlet.renderText(csv + ' is not a csv file'))

        data = pd.read_csv("csv/" + csv, delim_whitespace=False)
        if check_title(data):
            sys.exit(
                'this program only accepts date,scale not '
                + data.columns[0]
                + ','
                + data.columns[1]
            )
        elif check_data(data):
            print('your data may have lacking days and/or repeating days which will crash the program')
            while True:
                match input(figlet.renderText('do you want to organize your data? [Y/N]')).lower():
                    case 'y':
                        data = organize_data(data)
                        break
                    case 'n':
                        sys.exit('exiting program')
                    case _:
                        continue
            while True:
                match input(figlet.renderText('do you want to overwrite the original? [Y/N]')).lower():
                    case 'y':
                        data.to_csv(csv, index=False)
                        break
                    case 'n':
                        csv = input(figlet.renderText('what is the name of the csv file?'))
                        data.to_csv(csv + '.csv', index=False)
                        break
                    case _:
                        continue

        print(figlet.renderText('choose type: '))
        print(figlet.renderText('H'))
        print(figlet.renderText('B'))
        print(figlet.renderText('L'))

        type = input()

        match type.lower():
            case 'h':
                print(hint(csv, type))
                heatmap(data)
            case 'b':
                print(hint(csv, type))
                bar(data)
            case 'l':
                pass
            case _:
                sys.exit(figlet.renderText('you did not choose a type!'))

    elif len(sys.argv) == 3:
        csv = sys.argv[1]
        if not parse(csv):
            sys.exit(sys.argv[1] + ' is not a csv file')

        data = pd.read_csv("csv/" + csv, delim_whitespace=False)
        if check_title(data):
            sys.exit(
                'this program only accepts date,scale not '
                + data.columns[0]
                + ','
                + data.columns[1]
            )
        elif check_data(data):
             while True:
                match input('do you want to organize your data? [Y/N]').lower():
                    case 'y':
                        data = organize_data(data)
                        break
                    case 'n':
                        sys.exit('exiting program')
                    case _:
                        continue
             while True:
                match input('do you want to overwrite the original? [Y/N]').lower():
                    case 'y':
                        data.to_csv(csv, index=False)
                        break
                    case 'n':
                        csv = input('what is the name of the csv file?')
                        data.to_csv(csv + '.csv', index=False)
                        break
                    case _:
                        continue

        match type := sys.argv[2].lower():
            case 'h':
                heatmap(data)
            case 'b':
                bar(data)
            case 'l':
                line(data)
            case _:
                sys.exit('third argument is not H or B or L')

    else:
        sys.exit('too much arguments given, should only be 1 or 3')



if __name__ == '__main__':
    main()

