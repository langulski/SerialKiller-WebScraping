import pandas as pd
import numpy as np
import requests
from tqdm import tqdm



def spider_killer():

    dfs=pd.DataFrame()
    dfs1=pd.DataFrame()
    dfs2=pd.DataFrame()
    dfs3=pd.DataFrame()
    dfs4=pd.DataFrame()
    dfs5=pd.DataFrame()
    dfs6=pd.DataFrame()

    tf=[]
    page = 1
    url =f'https://killer.cloud/serial-killers/show/{page}'
    for page in tqdm(range(1,667)):
        try:
            url =f'https://killer.cloud/serial-killers/show/{page}'
            
            response = requests.get(url)
            html = response.content
            df= pd.read_html(html)

            df0 = pd.DataFrame(df[0].set_index('Back to top General Information').transpose().reset_index())

            df1 = pd.DataFrame(df[1].set_index('Characteristics').transpose().reset_index())

            df2 = pd.DataFrame(df[2].set_index('Childhood Information').transpose().reset_index())

            df3 = pd.DataFrame(df[3].set_index('Cognitive Ability').transpose().reset_index())

            df4 = pd.DataFrame(df[4].set_index('Back to top Incarceration').transpose().reset_index())

            df5 = pd.DataFrame(df[5].set_index('Death Information').transpose().reset_index())

            df6 = pd.DataFrame(df[7].droplevel(level=0,axis=1).drop(['TotalAnswered','AnsweredTrue','AnsweredFalse'],axis=1).set_index('KillerQuestion').transpose().reset_index())


            dfs = dfs.append(df0)
            dfs1= dfs1.append(df1)
            dfs2= dfs2.append(df2)
            dfs3= dfs3.append(df3)
            dfs4= dfs4.append(df4)
            dfs5= dfs5.append(df5)
            dfs6= dfs6.append(df6)
            frames= [dfs,dfs1,dfs2,dfs3,dfs4,dfs5,dfs6]
            sk_db = pd.concat(frames,axis=1)
            sk_db.to_csv('sk_db.csv')
        except:
            pass
    return sk_db
