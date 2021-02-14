from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd


def home(request):
    template = ''
    
    r = requests.get('https://www.hockey-reference.com/leagues/NHL_2021_skaters.html')

    soup = BeautifulSoup(r.text, 'lxml')

    table = soup.select('table')

    # new_table = pd.DataFrame(columns=range(0,28), index = [0])

    # row_marker = 0
    # for row in table.find_all('tr'):
    #     column_marker = 0
    #     columns = row.find_all('td')
    #     for column in columns:
    #         new_table.iat[row_marker,column_marker] = column.get_text()
    #         column_marker += 1

    for row in table.select:
        print(row)
  
    return render(request, 'home.html')
