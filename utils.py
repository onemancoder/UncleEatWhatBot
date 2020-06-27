from telegram.ext import BaseFilter
import pandas as pd

def food_recommendation(csv_path):
    food_db = pd.read_csv(csv_path, delimiter = ",")

    rand_food_row = food_db.sample()
    rand_food = rand_food_row["Name of food"].values[0]

    return rand_food

class Filter_via_bot(BaseFilter):
    def filter(self, message):
        return not message.via_bot