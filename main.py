water = 500
milk = 200
coffee = 1000
money = 0.0

user_command = input('What would you like? (espresso/latte/cappuccino): ')

if user_command == 'off':
    print('Switching Off, Thanks')


def check_sufficient_resources(coffeeTyp):
    global water, coffee, milk
    if coffeeTyp == 'espresso':
        if water < 50:
            print('Sorry there is not enough water.')
        elif coffee < 18:
            print('Sorry there is not enough coffee.')
        else:
            water = water - 50
            coffee = coffee - 18
            return 1

    elif coffeeTyp == 'latte':
        if water < 200:
            print('Sorry there is not enough water.')
        elif coffee < 24:
            print('Sorry there is not enough coffee.')
        elif milk < 150:
            print('Sorry there is not enough milk')
        else:
            water = water - 200
            coffee = coffee - 24
            milk = milk - 150
            return 1
    elif coffeeTyp == 'cappuccino':
        if water < 250:
            print('Sorry there is not enough water.')
        elif coffee < 24:
            print('Sorry there is not enough coffee.')
        elif milk < 100:
            print('Sorry there is not enough milk')
        else:
            water = water - 250
            coffee = coffee - 24
            milk = milk - 100
            return 1
    else:
        print('Unvalid Choice!!')


def insert_coins():
    quarters = int(input('How many quarters: '))
    dimes = int(input('How many dimes: '))
    nickles = int(input('How many nickles: '))
    pennies = int(input('How many pennies: '))

    return 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies


def check_sufficient_money(coffeeTyp, money):
    if coffeeTyp == 'espresso':
        if money < 1.5:
            print('Sorry not enough money. Money Refunded!!')
        else:
            change = round((money - 1.5), 2)
            if change > 0.0:
                print(f"Here is {change}$ in change")
            print(f"Here's your espresso ☕️, Enjoy ;)")

    if coffeeTyp == 'latte':
        if money < 2.5:
            print('Sorry not enough money. Money Refunded!!')
        else:
            change = round((money - 2.5), 2)
            if change > 0.0:
                print(f"Here is {change}$ in change")
            print(f"Here's your latte ☕️, Enjoy ;)")

    if coffeeTyp == 'cappuccino':
        if money < 3.0:
            print('Sorry not enough money. Money Refunded!!')
        else:
            change = round((money - 3.0), 2)
            if change > 0.0:
                print(f"Here is {change}$ in change")
            print(f"Here's your cappuccino ☕️, Enjoy ;)")


while user_command != 'off':
    if user_command == 'report':
        print(f'Water: {water}ml', f'Milk: {milk}ml', f'Coffee: {coffee}g', f'Money: {money}$', sep="\n")
        user_command = input('What would you like? (espresso/latte/cappuccino): ')
        continue

    if check_sufficient_resources(user_command.lower()) != 1:
        user_command = input('What would you like? (espresso/latte/cappuccino): ')
        continue
    print('Please insert your money ')
    money = insert_coins()
    check_sufficient_money(user_command.lower(), money)
    money = 0.0
    user_command = input('What would you like? (espresso/latte/cappuccino): ')


print('Switching Off, Happy to serve :D')
