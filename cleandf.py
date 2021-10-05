import pandas as pd
import numpy as np

sk_db = pd.read_csv('sk_db.csv')


def cleaning():
    sk_db.drop('index',axis=1,inplace=True)

  
    sk_db.drop('Unnamed: 0',axis=1,inplace=True)
    for number in range(1,7):
        try:
            a=f'index.{number}'
        
            sk_db.drop(a,axis=1,inplace=True)
        
        except:
            pass
    
    
 

def new_numeric_columns():
    sk_db['Confirmed Victims'] = [re.search("^.{0,3}\d+",str(a)).group() for a in sk_db['Victims:']]
    sk_db['Possible Victims']= [re.search("(\d+)(?!.*\d)",str(a)).group() for a in sk_db['Victims:']]
    sk_db['Starting Year of Activity'] = [re.search("^.{0,4}\d+",str(a)).group() for a in sk_db['Years Active:']]

def df_types():
    sk_db.iloc[:, np.r_[41:44,51:91]] = sk_db.iloc[:, np.r_[41:44,51:91]].astype('bool')
    sk_db['Confirmed Victims'] = sk_db['Confirmed Victims'].astype(int)
    sk_db['Possible Victims'] = sk_db['Possible Victims'].astype(int)