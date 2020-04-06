import re
import numpy as np

def classify_time(time_data):
    if 5<=time_data<=13:
        return 'morning'
    elif 13<time_data<21:
        return 'afternoon'
    elif time_data<5 and time_data>21:
        return 'night'

def assign_time(time_data):
    if str(time_data).lower() in ['morning','afternoon','night']:
        return str(time_data).lower()
    else:
        list_matches=re.findall(r'\d{2}h\d{2}',str(time_data))
        if len(list_matches)>0:
            lista_horas=[]
            for horas in list_matches:
                hora=int(horas[:2])
                minutos=int(horas[-2:])
                if minutos>30:
                    hora+=1
                lista_horas.append(hora)
            return classify_time(sum(lista_horas)/len(lista_horas))
        else:
            return np.nan

def busqueda_población(dataframe,dictionary):
    dataframe['Total_population_of_country']=''
    for index in dataframe.index:
        for key,value in dictionary.items():
            if dataframe.Country.iloc[index]==key:
                dataframe.Total_population_of_country.iloc[index]=value
                   
