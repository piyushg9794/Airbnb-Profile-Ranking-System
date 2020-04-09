from bs4 import BeautifulSoup
import pandas as pd
import requests

def get_rank(dataframe, shape, user_review):
    
    # rank calculation function
    
    count=0;
    
    for i in dataframe['No. of reviews']:
        count+=1
        if i<=user_review:
            break
        
    rank = ((count)/shape[0])*100                          
    
    return rank