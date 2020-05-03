from bs4 import BeautifulSoup
import pandas as pd
import requests
from get_rank import get_rank
from dataframe_maker import dataframe_maker

base_url = "https://www.airbnb.co.uk"
nav_url = "/s/Melbourne--Australia/homes"                    # Enter here the city link (default: melbourne)
user_url = input()      # Enter here the user profile url

df = dataframe_maker(base_url, nav_url)
df.sort_values("No. of reviews", axis = 0, ascending = False, inplace = True, na_position ='last') 
shape= df.shape


user_page = requests.get(user_url)
user_soup = BeautifulSoup(user_page.text, 'html.parser')


div_list = user_soup.find(class_='_1ekkhy94')

div_list2 = user_soup.find(class_='_czm8crp')
user_review = int(div_list2.text[:-8])

rank = get_rank(df, shape, user_review)

print(div_list.text)
print(user_review, " reviews")
print("Among top ", rank, "% user")
