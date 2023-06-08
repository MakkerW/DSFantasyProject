import os
import pandas as pd

#from GreenGroceries import app

#DATASET_PATH = os.path.join(app.root_path, 'dataset', 'fruitvegprices-2017_2022.csv')
DATASET_PATH = "C:/Users/welin/Downloads/DSFantasyProject/GreenGroceries/GreenGroceries/GreenGroceries/dataset/merged_gw.csv"



class ModelChoices:
    
    def __init__(self, choices_list):
        choices_list = list(choices_list)  # Convert choices_list to a list if it's not already
        choices_list.append('None')  # Add "none" as a choice
        for item in choices_list:
            item_str = str(item)  # Convert item to string
            item_str = item_str.replace("_", " ").capitalize()
            setattr(self, item_str.lower(), item_str)
    def choices(self):
        return [(k, v) for k, v in self.__dict__.items()]

    def values(self):
        return [v for v in self.__dict__.keys()]

    def labels(self):
        return [l for l in self.__dict__.values()]


df = pd.read_csv(DATASET_PATH, sep=',')
df.dropna(subset=['GW'], inplace=True)
df['GW'] = df['GW'].astype(int)
df['total_goals'] = df.groupby('name')['goals_scored'].transform('sum')
df['all_points'] = df.groupby('name')['total_points'].transform('sum')
df['total_assists'] = df.groupby('name')['assists'].transform('sum')
GWChoices = ModelChoices(df.GW)
PositionChoices = ModelChoices(df.position)
UserTypeChoices = ModelChoices(['Farmer', 'Customer'])

