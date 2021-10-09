import pandas as pd
import numpy as np
import re



def cleaning():
    try:
        for number in range(1,7):

            sk_db.drop('Unnamed: 0',axis=1,inplace=True)
            sk_db.drop('index',axis=1,inplace=True)
            a=f'index.{number}'
            
            sk_db.drop(a,axis=1,inplace=True)
    except:
        pass   
      
    
    
 

def new_numeric_columns(df):
    df['Confirmed Victims'] = [re.search("^.{0,3}\d+",str(a)).group() for a in df['Victims:']]
    df['Possible Victims']= [re.search("(\d+)(?!.*\d)",str(a)).group() for a in df['Victims:']]
    df['Starting Year of Activity'] = [re.search("^.{0,4}\d+",str(a)).group() for a in df['Years Active:']]

def df_types(df):
    #removed booled types in order to plot graphs in a easier way using Tableau
    df.replace({False: 0, True: 1}, inplace=True)
    # df.iloc[:, np.r_[41:44,51:91]] = df.iloc[:, np.r_[41:44,51:91]].astype('bool')
    df['Confirmed Victims'] = df['Confirmed Victims'].astype(int)
    df['Possible Victims'] = df['Possible Victims'].astype(int)