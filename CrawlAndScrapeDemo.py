# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup

def getResponse(url):
    response = requests.get(url)
    if(response.status_code == 200):
        print("Successful connection " + str(response.status_code))
    else:
        print("Error making connection" + str(response.status_code))
        response = False
    
    return response
    

def main():
    url = "https://www.tripadvisor.com/Restaurant_Review-g1143390-d3448252-Reviews-Le_Napolitain-Saclay_Essonne_Ile_de_France.html"
    #url = "https://www.hec.edu/games"
    response = getResponse(url)
    if(response):
        print("Scraping data")
        soup = BeautifulSoup(response.text,'html.parser')
        print(soup)
        count = 0
        """for review in soup.find_all('p',class_ = 'partial_entry'):
            count = count + 1
            print("Review number" + str(count))
            print(review.text)"""
        
        for reviewContainer in soup.find_all('div',class_ = 'review-container'):
            count = count + 1
            print("Review number" + str(count))
            """for title in reviewContainer.find_all('div',class_ = 'quote'):
                print(title.text)
            for reviewText in reviewContainer.find_all('p',class_ = 'partial_entry'):
                print(reviewText.text)"""
            reviewTitle = reviewContainer.find('div',class_='quote')
            reviewText = reviewContainer.find('p',class_ = 'partial_entry')
            print(reviewTitle.text)
            print(reviewText.text)
        
main()
    
    
