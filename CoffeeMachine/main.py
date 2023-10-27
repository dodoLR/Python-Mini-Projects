MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    report_str = ""
    for res in resources:
        report_str += f"{res} : {resources[res]}\n"
    return report_str

def insufficient_resources(coffee):
    needs = MENU[coffee]["ingredients"]
    res = ['water', 'milk', 'coffee']
    insufficient = []
    for i in res:
        if i in needs and needs[i] > resources[i]:
            insufficient += [i]
    return insufficient

def transaction(coffee) :
    price = MENU[coffee]["cost"]
    print("Please insert coins.")
    quarters = int(input("How many quarters? : "))
    dimes = int(input("How many dimes? : "))
    nickles = int(input("How many nickles? : "))
    pennies = int(input("How many pennies? : "))
    sum = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if sum < price :
        print("Sorry that's not enough money. Money refunded.")
    else :
        needs = MENU[coffee]["ingredients"]
        for res in needs :
            resources[res] -= needs[res]
        print(f"Here's ${sum-price} in change.")
        print(f"Here's your {coffee} ☕. Enjoy!")

on = True
while on :
    choice = input("What do you like? (espresso/latte/cappuccino): ")
    if choice == "report":
        print(report())
    elif choice == "off" :
        print("Turning off the machine.")
        on = False
    else:
        insufficient = insufficient_resources(choice)
        if insufficient == []:
            transaction(choice)
        else :
            for resource in insufficient :
                print(f"Sorry there is not enough {resource}")