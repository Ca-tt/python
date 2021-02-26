import random
import os

# * DATA SETS
meal_sets = {
    'S': 21.75,
    'D': 25.95,
}

halls = {
    'A': 1000.00,
    'B': 850.00,
    'C': 750.00,
    'H': 0,
}

# * CONSTANTS
child_price_discount = 0.5

gratuity_rate = 0.2

weekend_charge = 0
weekend_tariff = 0.1

tax_rate = 0.06875

speedy_discount_rate = 0.02


# * FUNCTIONS
def validate_number_input(question):
    while True:
        try:
            result = int(input(question))

        except ValueError:
            print('Only numbers accepted. Try enter numbers again')
            continue

        if result < 0:
            print('Number must be greater than 0')
            continue

        else:
            return result


def validate_letter_input(question, array):
    while True:
        try:
            result = str(input(question))

        except TypeError:
            print('Only letters accepted. Try enter', array, 'again')
            continue

        if result.upper() not in array:
            print('Please, choose one from following options:', array)
            continue

        else:
            return result.upper()


# * USER INPUT
# How many guests are invited?
adults = validate_number_input('How many adults attended (numbers only):')
children = validate_number_input('How many children attended (numbers only):')

# What will they eat?
choosen_meals_set = validate_letter_input(
    'Please, choose a meal set: Deluxe (D) or Standard (S): ',
    ['D', 'S']
)

# Is it planned to be set on the weekend?
is_on_weekend = validate_letter_input(
    'Do you want to reserve a hall on the weekend [Yes\\No]: ',
    ['YES', 'NO']
)

# What hall they choose?
chosen_hall = validate_letter_input(
    'Please, choose a hall (A, B, C) or select \'H\' if you want to spend time at home: ',
    ['A', 'B', 'C', 'H']
)

# How many guests are invited?
deposit_amount = validate_number_input('How much money do you intend to deposit (numbers only): ')

# * CALCULATION
# Food prices
adult_meals_price = meal_sets[choosen_meals_set]
children_meals_price = adult_meals_price * child_price_discount

# Total food cost
total_adults_food_cost = adults * adult_meals_price
total_children_food_cost = children * children_meals_price

total_food_cost = total_adults_food_cost + total_children_food_cost

gratuity_cost = total_food_cost * gratuity_rate

hall_cost = halls[chosen_hall]

if is_on_weekend == 'YES':
    weekend_charge = total_food_cost * weekend_tariff

tax_charge = (total_food_cost + hall_cost) * tax_rate

total_price = total_food_cost + gratuity_cost + hall_cost + weekend_charge + tax_charge

# if < $1000.00 : 2%, < $2000.00: 4%, < $5000.00: 5%, > $5000.00: 7%

if total_price > 1000:
    speedy_discount_rate = 0.04
elif total_price > 2000:
    speedy_discount_rate = 0.05
elif total_price > 5000:
    speedy_discount_rate = 0.07

speedy_discount = total_price * speedy_discount_rate

left_to_pay = total_price - speedy_discount - deposit_amount

print('\n')


def get_receipt():
    company_name = 'Caswell Catering and Convention Services'
    invoice_number = random.randint(100, 999)

    def separator(sign):
        for i in range(0, 40):
            print(sign, end='')
        print('\n')

    # print headline
    separator('/-')
    print(company_name.center(50), '\n', 'Final Bill'.center(40), 'Invoice #', invoice_number)
    separator('/-')

    # attendee and rates section
    print('Number of adult:', adults)
    print('Number of adult:', children)
    print('Gratuity:', gratuity_rate * 100, '%')
    print('Weekend:', is_on_weekend)
    print('Cost per standard meal for adult: $', adult_meals_price)
    print('Cost per standard meal for child: $', children_meals_price)

    separator('-')

    print('Total cost for adult meals: $', total_adults_food_cost)
    print('Total cost for children meals: $', total_children_food_cost)
    print('\n')

    print('Total food cost: $', total_food_cost)

    separator('-')

    print('Gratuity: $', gratuity_cost)
    print('Hall', chosen_hall, '— Room fee: $', hall_cost)
    print('Weekend charge: $', weekend_charge)
    print('Taxes: $', tax_charge)

    separator('-')

    print('Subtotal: $', total_price)
    print('\n')

    print('Less deposit: $', deposit_amount)
    print('Less Speedy Payment: $', speedy_discount)
    print('Balance Due: $', left_to_pay)

    separator('/-')
    print('Thank you for using', company_name, ''.center(40))

    os.system("pause")


get_receipt()

# TODO: pause a screen at the end of the printing
# TODO: write bill in the receipt.txt file
# TODO: The format function and tabs are used to align output and print monies to 2 decimal spaces
# TODO: Use menus to display choices
# TODO: Prompts are used for catering on weekend and for speedy payment.
# TODO: sales tax is count excluding gratuity_rate_cost
