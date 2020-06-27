import utils

# Test that we are reading from the correct column which gives us the name of a food
def test_food_recommendation_correct_column():
    csv_path = "tests/test_one_food_db.csv"

    assert utils.food_recommendation(csv_path) == "Vegetarian Tofu Rice"

# There can be occasional failures when both samples collected are the same
def test_food_recommendation_randomized():
    csv_path = "tests/test_food_db.csv"

    first_rand_food = utils.food_recommendation(csv_path)
    second_rand_food = utils.food_recommendation(csv_path)
    assert first_rand_food  != second_rand_food