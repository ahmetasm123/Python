dik1= {
    "1: Cappuccino":3.00,
    "2: Macchiato":2.50,
    "3: Mocha":3.50,
    "4: Flat White":2.50,
    "5: Espresso":2.50,
    "6: Americano":3.00,
    "7: Latte":2.50,
}
dik2= {
    "1: medium":0,
    "2: large":1,
    "3: XL":1.5,
}
dik3= {
    "1: eat-In":0,
    "2: take away":1,
}
z=0
y=0
while True:

    try:
        print("Menü")
        for item, price in dik1.items():
            print(f"{item} = ${price:.2f}")
        x = int(input("Select your drink (1-7)= ")) - 1

        if 0 <= x < len(dik1):
            drink_name = list(dik1.keys())[x]
            drink_price = list(dik1.values())[x]
            print(f"You selected: {drink_name} = ${drink_price:.2f}")
        else:
            print("Invalid selection. Please enter a number between 1 and 7.")

        print("Menü")
        for item, price in dik2.items():
            print(f"{item} = ${price:.2f}")
        x = int(input("Select your size (1-3)= ")) - 1

        if 0 <= x < len(dik2):
            size_name = list(dik2.keys())[x]
            size_price = list(dik2.values())[x]
            print(f"You selected: {size_name} = ${size_price:.2f}")
        else:
            print("Invalid selection. Please enter a number between 1 and 3.")

        x = int(input("would you like more \n press 1 for yes \n press 2 for no"))
        z+=1
        y+=drink_price+size_price
        if x==1:
            continue
        else:
            break

    except ValueError:
        print("Invalid input. Please enter a number.")
x = int(input("Would you like take away? (1-2)= ")) - 1

for item, price in dik3.items():
    print(f"{item} = ${price:.2f}")
if 0 <= x < len(dik3):
    loc_name = list(dik3.keys())[x]
    loc_price = list(dik3.values())[x]
    print(f"You selected: {loc_name} = ${loc_price:.2f}")
else:
    print("Invalid selection. Please enter a number between 1 and 2.")
preis=y+(z*loc_price)
print("Your total is= $"+str(preis))
