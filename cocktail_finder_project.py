import sys
import turtle
import requests

import json

print('Welcome to happy hour, lets get a cocktail!')
# Here is the code for my very poorly drawn out cocktail glass
turtle.forward(100)
turtle.left(180)
#stem of glass
turtle.forward(50)
turtle.right(90)
turtle.forward(120)
#body of glass
turtle.left(40)
turtle.forward(100)
turtle.left(180)
turtle.forward(100)
turtle.left(100)
turtle.forward(100)
#fill the glass
turtle.left(180)
turtle.forward(40)
turtle.left(310)
turtle.forward(85)
turtle.done()

#Some introductory things to start the cocktail finder off!
name = input('What is your name?')

print('Hello {}!'.format(name))

from time import sleep
sleep(2)

# I used the sleep function because I was not a fan of how quick the output printed
# I wanted the user to have a more conversational experience and have time to read the text with pauses between

yes_or_no_cocktail = input('Do you want a cocktail? Yes / No')

# I added this yes/no section because I wanted to try coding a program where it ends the program if you give
# an answer that it does not like.  So here I had the program end if you said anything but 'yes' to a cocktail

if yes_or_no_cocktail == 'Yes':
    sleep(2)
    print('Great, lets find out what kind of cocktail you want!')

elif yes_or_no_cocktail == 'No':
    sleep(2)
    print('Oh, that is a shame.')
    sleep(1)
    print('Come back when you want a drink')
    sleep(2)
    sys.exit()

else:
    sleep(2)
    print('Sorry, please try again.')
    sleep(1)
    print('Please try putting a Yes or No next time.  Answers are case sensitive.')
    sleep(5)
    sys.exit()

sleep(2)
print('Now, you have three options to pick from!')
sleep(1.5)
print('You can ask me for a random cocktail - option 1')
sleep(1.5)
print('You can give me one ingredient and I will suggest cocktails - option 2')
sleep(1.5)
print('Finally, you can give me two ingredients and I will suggest cocktails - option 3')
sleep(1.5)
user_choice = input('Which option would you like to choose: 1, 2, or 3?  Please type the number only.')

sleep(2)

if user_choice == '1':
    api_url = "http://www.thecocktaildb.com/api/json/v1/"
    api_key = '1'

    random_result = requests.get(api_url + api_key + "/" + "random.php")
    random_cocktail_results = random_result.json()

    random_drinks = random_cocktail_results['drinks']

    for drink in random_drinks:
        print('Here is your random cocktail!')
        sleep(2)
        print(drink['strDrink'])
        sleep(2)
        print('Enjoy!')
        sleep(10)

#Moving on to option 2: cocktails with one user-chosen ingredient

elif user_choice == '2':

    api_url = "http://www.thecocktaildb.com/api/json/v1/"
    api_key = '1'
    chosen_ingredient = (input("Choose an ingredient"))

    # Filter cocktails by ingredients
    one_ingred_result = requests.get(api_url + api_key + "/" + "filter.php?i=" + chosen_ingredient)
    one_ingred_cocktail_results = one_ingred_result.json()

    drinks = one_ingred_cocktail_results['drinks']

    print('Found {} drinks.'.format(len(drinks)))
    for drink in drinks:
        print(drink['strDrink'])
        sleep(0.5)

# I chose to add a sleep function here to slow the list down, might be overkill though if it is a long list...
    print('Enjoy!')
    sleep(10)
# I added the sleep here so the user has time to read the list of cocktails
# When I tested the program after making a zipped file, it just closed straight away

# I did have an issue with the above section, if the program cannot find a cocktail with that ingredient then it errors.
# I added an else statement but the code will error before it can print it.



# This is the final option which takes two user chosen ingredients and provides a list of suitable cocktails

elif user_choice == '3':
    api_url = 'http://www.thecocktaildb.com/api/json/v1/'
    api_key = '1'

    ingredient1 = input('Give me the first ingredient you want in your cocktail:')
    ingredient2 = input('And what is the second ingredient you want?')

    # It does not like blank spaces between some answers (like 'triple sec')
    # So I replaced the blank space with a +
    ingredient1 = ingredient1.replace(' ', '+')
    ingredient2 = ingredient2.replace(' ', '+')

    # Make 2 requests, one for each ingredient
    result1 = requests.get(api_url + api_key + "/" + "filter.php?i=" + ingredient1)
    result1_data = result1.json()['drinks']

    result2 = requests.get(api_url + api_key + "/" + "filter.php?i=" + ingredient2)
    result2_data = result2.json()['drinks']

    total_result = []
    count = 0
    for drink in result1_data:
        if drink in result2_data:
            total_result.append(drink)

    print('Found {} drinks.'.format(len(total_result)))
    for drink in total_result:
        print(drink['strDrink'])
        sleep(0.5)
    sleep(1)
    print('Enjoy your drink!')
    sleep(10)

# Same reason as above as to why I added a 10 second sleep


else:
    print('There seems to be an issue')
    sleep(1)
    print('Please try again - try typing either 1, 2, or 3')
    sleep(5)
    sys.exit()