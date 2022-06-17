
"""The user can enter primary ingredients and the program will search
 through the list to find if there is anything that can be made"""

# List of all ingredients to display to user if needed
ingredients = ["Buns", "Ground Beef", "Cheese", "Lettuce", "Tomatoes", "Pickles", "Noodles",
               "Tomato Sauce", "Taco Shells", "Tortillas", "Tortilla Chips", "Queso", "Salsa",
               "Chicken", "Flour", "Egg", "Bell Peppers", "Onion", "Zucchini", "Bread Crumbs",
               "Mayo", "Butter", "Bacon", "Tuna", "Bread", "Crab", "Shrimp", "Potatoes", "Celery",
               "Mustard"]

# Making each meal as a dictionary with the meal name as keys, list of ingredients as values
meals = {"Cheeseburgers" : ["Buns", "Ground Beef", "Cheese", "Lettuce", "Tomatoes", "Pickles"],
         "Spaghetti" : ["Noodles", "Ground Beef", "Tomato Sauce"],
         "Tacos" : ["Taco Shells", "Ground Beef", "Cheese", "Lettuce", "Tomatoes"],
         "Burritos" : ["Tortillas", "Ground Beef", "Cheese", "Lettuce", "Tomatoes"],
         "Nachos" : ["Tortilla Chips", "Ground Beef", "Cheese", "Lettuce", "Tomatoes", "Queso", "Salsa"],
         "Chicken Tenders" : ["Chicken", "Flour", "Egg"],
         "Chicken Parmesan" : ["Chicken", "Tomato Sauce", "Cheese"],
         "Stuffed Peppers" : ["Bell Peppers", "Ground Beef", "Cheese", "Onion", "Tomatoes", "Zucchini"],
         "Meatballs" : ["Ground Beef", "Bread Crumbs", "Egg"],
         "BLT Sandwiches" : ["Bread", "Bacon", "Lettuce", "Tomatoes", "Mayo", "Butter"],
         "Tuna Melts" : ["Bread", "Tuna", "Mayo", "Pickles", "Cheese", "Tomatoes", "Butter"],
         "Crab Cakes" : ["Crab", "Mayo", "Egg", "Bread Crumbs"],
         "Shrimp Tacos" : ["Tortillas", "Shrimp", "Lettuce", "Tomato", "Cheese"],
         "Potato Salad" : ["Potatoes", "Celery", "Egg", "Onion", "Mayo", "Mustard"]}

# Get input from user, iterate through meals to find which are doable
def check_ingredient():
    print("What primary food item would you like to use?")
    user_in = input().lower()

    potential_meals = []

    for meal, ingredients in meals.items():
        for ingredient in ingredients:
            if user_in == ingredient.lower():
                potential_meals.append(meal)

    if len(potential_meals) == 0:
        print("I'm sorry, nothing in our recipe book contains that ingredient. Would you like to try another?Y/N")
        user_in2 = input()
        if user_in2.upper() == "Y":
            return check_ingredient()
        else:
            exit()

    return potential_meals

# List of the meals that come back from check_ingredient()
elligible_meals = check_ingredient()

# if statement to keep from automatically running when the user says "N" to try again
# Displays list of elligible meals and allows user to pick the one they would like
if len(elligible_meals) > 0:
    print("Here is a list of meals you could make with your chosen ingredient:")
    num = 1
    for i in elligible_meals:
        print(str(num) + ". " + i)
        num += 1

print("Enter the number of the meal you would like to choose. Enter 0 to exit.")
meal_choice = int(input())

# Verifies that the user picks between the meals provided
while meal_choice > len(elligible_meals):
    meal_choice = int(input("Please enter a valid choice or press 0 to exit.\n"))

print("Here is the complete list the ingredients you will need to make " + elligible_meals[meal_choice - 1])
print(meals[elligible_meals[meal_choice - 1]])
