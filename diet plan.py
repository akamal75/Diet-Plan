food_database = {
    "chicken_breast": {"protein": 25, "calories": 165},
    "salmon": {"protein": 22, "calories": 206},
    "brown_rice": {"protein": 5, "calories": 216},
    "spinach": {"protein": 2, "calories": 7},
    "beef": {"protein": 22, "calories": 240},
    "sweet_potato": {"protein": 2, "calories": 115},
    "broccoli": {"protein": 2, "calories": 31},
    "eggs": {"protein": 6, "calories": 78},
    "tuna": {"protein": 25, "calories": 120},
    "mixed_salad": {"protein": 2, "calories": 14},
    "chicken": {"protein": 25, "calories": 165},
    "rice": {"protein": 5, "calories": 216},
    # ...
}

def calculate_nutrition(food_item, servings, nutrient):
    if food_item not in food_database:
        raise ValueError(f"Invalid food item: {food_item}")

    nutrient_per_serving = food_database[food_item][nutrient]
    total_nutrient = servings * nutrient_per_serving
    return total_nutrient

def print_meal_plan(diet_plan):
    for meal, items in diet_plan.items():
        print(meal)
        for food_item, servings in items.items():
            try:
                calories = calculate_nutrition(food_item, servings, "calories")
                protein = calculate_nutrition(food_item, servings, "protein")
                print(f"{food_item}: {servings} servings, {calories} calories, {protein}g protein")
            except ValueError as e:
                print(f"Error: {e}")
        print()

def generate_diet_plan(game, gender):
    diet_plans = {
        "basketball": {
            "male": {"breakfast": {"chicken_breast": 2, "brown_rice": 1}, "lunch": {"salmon": 1, "spinach": 2},
                     "dinner": {"beef": 1, "sweet_potato": 1, "broccoli": 2}},
            "female": {"breakfast": {"chicken_breast": 2, "brown_rice": 1}, "lunch": {"salmon": 1, "spinach": 2},
                       "dinner": {"beef": 1, "sweet_potato": 1, "broccoli": 2}}
        },
        # Add diet plans for other games and genders similarly
    }

    if game not in diet_plans or gender not in diet_plans[game]:
        raise ValueError("Invalid game or gender.")

    diet_plan = diet_plans[game][gender]
    print(f"{game.capitalize()} Diet Plan for {gender.capitalize()} Players:")
    print_meal_plan(diet_plan)

def view_food_database():
    print("Food Database:")
    for food_item, nutrition_info in food_database.items():
        print(f"{food_item}: {nutrition_info['protein']}g protein, {nutrition_info['calories']} calories")
    print()

# User Input and Execution
try:
    print("Welcome to the Diet Planner App!")
    name = input("Enter your name: ")
    sex = input("Enter your sex (M/F): ").lower()
    game_choice = input("Select a game (basketball/football/tennis): ").lower()

    if sex not in ["m", "f"]:
        raise ValueError("Invalid sex. Please enter 'M' or 'F'.")

    if game_choice not in ["basketball", "football", "tennis"]:
        raise ValueError("Invalid game choice. Please enter 'basketball', 'football', or 'tennis'.")

    generate_diet_plan(game_choice, sex)

    while True:
        print("\nOptions:")
        print("1. View Food Database")
        print("2. Modify Diet Plan")
        print("3. Exit")

        option = input("Select an option (1/2/3): ")

        if option == "1":
            view_food_database()
        elif option == "2":
            # Add logic to modify the diet plan
            print("Modify Diet Plan - Work in progress!")
        elif option == "3":
            print("Exiting the Diet Planner App. Goodbye!")
            break
        else:
            print("Invalid option. Please enter a valid option.")

except ValueError as e:
    print(f"Error: {e}")
