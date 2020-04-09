from bs4 import BeautifulSoup
import pandas as pd
import requests
from typecast_n_preprocessing import typecast_n_preprocessing

def dataframe_maker(base_url, nav_url):
    
    # function for making dataframe from city data
    
    df = pd.DataFrame(columns = ['Rating', 'No. of reviews'])
    
    for i in range(14):

        page = requests.get(base_url + nav_url)
        soup = BeautifulSoup(page.text, 'html.parser')

        rating_list = soup.find_all(class_="_3zgr580")
        review_list = soup.find_all(class_="_a7a5sx")

        data = typecast_n_preprocessing(rating_list, review_list)

        df_temp = pd.DataFrame(data)    
        df = df.append(df_temp, ignore_index= True)   

        page_nav = soup.find(class_="_i66xk8d")
        
        if page_nav != None:
            nav_url = page_nav.find('a')['href']
    
    return df
