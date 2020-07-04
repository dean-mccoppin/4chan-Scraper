# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 15:30:08 2020

@author: truet
"""
#work on retrieving link to each thread post
import requests
from bs4 import BeautifulSoup as bs
import re

term = input("Search exact phrase/word to be searched: ")
#pages = 1
url = "https://find.4chan.org/?q={}".format(term)
r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})


def fourchanScraper(term):
    """searches 4chan for a specified term"""
    chan = bs(r.text, "lxml")
    #find every thread on page
    thread = chan.find_all("div", {"class":"thread"})
    n = 0
    for page in range(90): #collect from every page (1-10)
        for post in thread:
            #board if parent thread post
            try:
                board = post.find("div", {"class":"fileText"}).a.text
                print("Board: " + board)
            except:
                print("Anoymous, Unkown Board")
            #title
            title = post.find("div", {"class":"postInfo desktop"}).span.text
            if re.search('[a-zA-Z]', title) != None:
                print("Post Title: " + title.strip())
            else:
                print("(Child Post)")
            #grab link to the post------ WIP
            link = post.find("span", {"class":"postNum desktop"}).a
            print("Link: " + link['href'])
            #text from posts
            optext = post.find_all("blockquote", {"class":"postMessage"})
            for text in optext:
                check = re.search(term, text.text)
                if check != None:
                    n += 1
                    print(text.text)
                    print(f'^ ----- Post {n} ----- ^')
            global pages
            pages =+ 10
            
fourchanScraper(term)