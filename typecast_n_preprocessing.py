from bs4 import BeautifulSoup
import pandas as pd
import requests

def typecast_n_preprocessing(rating_list, review_list):
    
    # function to change datatype form string to int/float before appending in dataframe
    
    new_rating_list =[]
    new_review_list = []
        
    for l,m in zip(rating_list, review_list):

        rating = float(l.text)
        new_rating_list.append(rating)
        
        no_review = int(m.text[2:-1])
        new_review_list.append(no_review)
        
    data = {'Rating': new_rating_list, 'No. of reviews': new_review_list}
 
    return data