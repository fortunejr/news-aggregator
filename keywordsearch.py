import os
import nltk
import nltk.corpus
from nltk.tokenize import word_tokenize
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
science = ['moon','sun','nasa','mars','']
business = ['dollar','money','rich','stock market','bitcoin','btc','crypto','btc','market','chinese','america','us','ethereum','wallet','sp500','fortune500','dow jones','forex','dollar','dollars','cap','$','euro','euros','europe','european']
tech = ['apple','microsoft','python','programming','coding','code','samsung','hp','macbook','tecno','infinix','bot','chat','netflix','technology','tech','java','javascript','js','hp','computers','py']
health = ['COVID','disease','hospital','covid-19','allergy','ache','appetite','aspirin','blood','bone','bruise','clinic','cold','cough','diarrhea','fever','hiv','aids','first aid','lassa','flu','injection','infection','injury','muscle','pain','rash','heat','stomach','head','leg','virus','fungi','bacteria','fungus','viral','bacterium','sick']
economy = ['naira','money','forex','scarcity','insurance','oil boom','dollar','russia', 'nigeria','america','canada','subsidy','budget','capital','bankrupt','bankruptcy','cash','consumer','credit','currency','debt','deficit','finance','dollars','dollar','naira','loan','investment']
war = ['ukraine','russia','ally','allies']
politics = ['election','biden','putin','tinubu','obi','peter','bat','senate','apc','pdp','lp','labour','party','atiku','igbo','yoruba']
sport = ['football','soccer','nba','manchester','ucl','laliga','epl','barca','barcelona','madrid','atletico','messi','ronaldo','neymar','world cup','man city','treble','mbappe','psg','chelsea','liverpool','arsenal','epl','pl','tottenham','spurs','man utd','ac milan','inter','milan','napoli','juventus','bayern','dortmund','leipzig','bundesliga','serie a','mls','soccer','saudi','saka','rice','haaland','alvarez','benardo','gundogan','rodrigo','rashford','de gea','fernandes','salah','firmino','nunez','allison','gakpo','van dijk','diaz','jesus','martinelli','kane','son','lloris','lewandowski','pedri','gavi','benzema','vini jr','mane']
entertainment = ['davido','wizkid','rema','burnaboy']


def fetchnews():
    
    urls = []
    
    query = input('Enter your interest: ')
    print(query)
    interests.append(query)
    
    
    query2 = query.split()
    for x in query2:
        if x in science:
            print('Science')
        elif x in business:
            print('Business')
        elif x in tech:
            print('Tech')
        elif x in health:
            print('Health')
        elif x in economy:
            print('Economy')
        elif x in war:
            print('War')
        elif x in politics:
            print('Politics')
        elif x in sport:
            print('Sport')
        elif x in entertainment:
            print('Ent')
        else:
            print('N/A')
    new = query
    new_tokens = nltk.pos_tag(word_tokenize(new))
    
    grammer_np = r'NP: {<DT>?<JJ>*<NN>}'
    chunk_parser = nltk.RegexpParser(grammer_np)
    chunk_result = chunk_parser.parse(new_tokens)
    print(new_tokens)
    for new in new_tokens:
        if new[1] == 'NNS' or new[1] == 'NN':
            print(new[0])
            print(new[1])
    print(chunk_parser)
    print(chunk_result)

fetchnews()

# The machine following a set of instructions is one thing, making it learn from the available data is something diff.
