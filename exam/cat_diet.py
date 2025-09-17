GRAM_FATS = 9
GRAM_PROTEINS = 4
GRAM_CARBOHYDRATES = 4

percent_fats = int(input())
percent_proteins = int(input())
percent_carbohydrates = int(input())
total_calories = int(input())
percent_water = int(input())

total_fats = (total_calories * percent_fats / 100) / GRAM_FATS
total_proteins = (total_calories * percent_proteins / 100) / GRAM_PROTEINS
total_carbohydrates = (total_calories * percent_carbohydrates / 100) / GRAM_CARBOHYDRATES

food_weigh = total_carbohydrates + total_proteins + total_fats
calories_for_gram = total_calories / food_weigh

total_water = calories_for_gram * percent_water / 100

one_gram_food = calories_for_gram - total_water

print(f"{one_gram_food:.4f}")