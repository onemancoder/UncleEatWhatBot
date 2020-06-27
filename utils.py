import pandas as pd

def food_recommendation(csv_path):
    food_db = pd.read_csv(csv_path, delimiter = ",")

    rand_food_row = food_db.sample()
    print(rand_food_row)
    rand_food = rand_food_row["Name of food"].values[0]

    return rand_food