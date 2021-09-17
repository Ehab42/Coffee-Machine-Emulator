# Coffee-Machine-Emulator
A simple python script for a coffee vending machine emulator

Once you run the code you will be asked the question What would you like? (espresso/latte/cappuccino) ?, you can reply with the following:
- 'off': This will turn off the machine and terminate the program.
- 'report': This will give you a report of the ingredients used in making coffee with their remaining portions.
- Your coffee choice which are either
  * 'espresso': costs 1.5$ (50ml water and 18g coffee)
  * 'latte': costs 2.5$ (200ml water, 150ml milk and 24g coffee)
  * 'cappuccino': costs 3.0$ (250ml water, 100ml milk and 24g coffee)

After the user enter his coffee choice:
- If the sufficient ingredients are avilable in the machine, the user will be asked to insert money in either quarters, dimes, nickels or pennies.
- If no sufficient ingredients available, the user will get the message of the specific ingredients lacking.
- If the amount of money entered is not sufficient, the user will also get a message of 'Insufficient Money'
- Otherwise, the user will be served the coffee ordered and if any change left the user will recieve it.
