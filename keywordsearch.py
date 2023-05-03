from googlesearch import search
import webbrowser
import time
#from tkinter import *
from bs4 import BeautifulSoup
import requests
from openpyxl import Workbook
from openpyxl import load_workbook
import random

interests = []

#Categories
business = ['dollar','stock market','bitcoin','btc','crypto']
tech = ['apple','microsoft','python','programming','coding','code','samsung']
health = ['COVID','disease','hospital']
economy = ['naira','forex','scarcity','insurance','oil boom','dollar','russia', 'nigeria','america','canada']
war = ['ukraine','russia']
politics = ['election','biden','putin','tinubu']
sport = ['football','soccer','nba','manchester united','ucl','laliga','epl']
entertainment = ['davido','wizkid','rema','burnaboy']

workbook = Workbook()
sheet = workbook.active

wb = load_workbook('interests.xlsx')
ws = wb.active
sheet = wb.active

def fetchnews():
    sheet_len = len(sheet['A'])
    urls = []
    #print(ws['B2'].value)
    query = input('Enter your interest: ')
    print(query)
    interests.append(query)
    sheet_len = len(sheet['A'])
    sheet['A' + str(sheet_len+1)] = query
    wb.save('interests.xlsx')
    for j in search(query):
        urls.append(j)

    #print(urls)
    html_text = requests.get(urls[0]).text
    soup = BeautifulSoup(html_text, 'lxml')
    head = soup.find('title')
    content = soup.find_all('p')
    print(head.text)
    query2 = query.split()
    for queryword in query2:
        for bus in business:
            if queryword == bus:
                print('Business')
                sheet['C' + str(sheet_len+1)] = 'Business'
        for techh in tech:
            if queryword == techh:
                print('Tech')
                sheet['C' + str(sheet_len+1)] = 'Tech'
        for healthh in health:
            if queryword == healthh:
                print('Health')
                sheet['C' + str(sheet_len+1)] = 'Health'
        for econ in economy:
            if queryword == econ:
                print('Economy')
                sheet['C' + str(sheet_len+1)] = 'Economy'
        for warr in war:
            if queryword == warr:
                print('War')
                sheet['C' + str(sheet_len+1)] = 'War'
        for pols in politics:
            if queryword == pols:
                print('Politics')
                sheet['C' + str(sheet_len+1)] = 'Politics'
        for sportt in sport:
            if queryword == sportt:
                print('Sport')
                sheet['C' + str(sheet_len+1)] = 'Sport'
        for ent in entertainment:
            if queryword == ent:
                print('Entertainment')
                sheet['C' + str(sheet_len+1)] = 'Entertainment'
    
                


    sheet['B' + str(sheet_len+1)] = urls[0]
    wb.save('interests.xlsx')


def load_news():
    html_text = requests.get(ws['B2'].value).text
    soup = BeautifulSoup(html_text, 'lxml')
    head = soup.find('title')
    content = soup.find_all('p')
    print(head.text)
    y = 0
    while y < len(content):
        print(content[y].text)
        y+=1


fetchnews()

