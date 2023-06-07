import os
import pandas as pd

#from GreenGroceries import app

#DATASET_PATH = os.path.join(app.root_path, 'dataset', 'fruitvegprices-2017_2022.csv')
DATASET_PATH = "C:/Users/welin/Downloads/DSFantasyProject/GreenGroceries/GreenGroceries/GreenGroceries/dataset/cleaned_players.csv"



class ModelChoices:
    def __init__(self, choices_list):
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

ProduceCategoryChoices = ModelChoices(df.first_name)
ProduceItemChoices = ModelChoices(df.second_name)
ProduceVarietyChoices = ModelChoices(df.goals_scored)
ProduceUnitChoices = ModelChoices(df.minutes)

UserTypeChoices = ModelChoices(['Farmer', 'Customer'])

