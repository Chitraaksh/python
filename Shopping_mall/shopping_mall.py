from Site import site_qr
import time

foods = {"Potato": 50, "Onion": 40, "Bread": 35, "Chocolate": 30, "Tomato": 50, "Cupcake": 120,
         "Biscuits": 40,"Chips": 20, "Cold drink": 80, "Milk": 50, "Apple": 90, "Banana": 50, "Orange": 60,
         "Butter": 55, "Cheese": 110, "Egg": 40, "Doll": 140, "Rice": 45, "Pulse": 95, "Deodorant": 200, "Soap": 40,
         "Shampoo": 130, "Cutlery": 350, "Pickle": 80, "Fan": 2200, "Dry fruits": 275, "Toothpaste": 65,
         "Toothbrush": 35, "Tube light": 1800, "Led bulb": 350, "Cream": 270, "Spices": 50, "Bottle": 110,
         "Utensils": 320, "Teddy bear": 450, "Wheat": 35, "Wheat flour": 45}
cart = {}
total = 0


def update_html_placeholder(total):
    try:
        with open("index.html", "r") as file:
            content = file.read()

        # Replace the `{total_amount}` placeholder with the actual total
        updated_content = content.replace("{total_amount}", str(total))

        with open("index.html", "w") as file:
            file.write(updated_content)
        print("HTML placeholder updated.")
    except FileNotFoundError:
        print("HTML file not found. Please check the path.")

def reset_html_placeholder(total):
    try:
        with open("index.html", "r") as file:
            content = file.read()

        # Replace the `{total_amount}` placeholder with the actual total
        updated_content = content.replace(str(total), "{total_amount}")

        with open("index.html", "w") as file:
            file.write(updated_content)
        print("HTML placeholder updated.")
    except FileNotFoundError:
        print("HTML file not found. Please check the path.")


def mall():
    global total
    while True:
        food = input("What would you like to buy (press 'c' to go to counter)? ")
        food = food.capitalize()
        if not food.lower() == "c":
            if food in foods:
                price = (foods.get(food))
                quantity = int(input("How many would you like? "))
                print(f"Price of one {food} is ₹{price}")
                finalprice = price * quantity
                if food in cart:
                    cart[food]['quantity'] += quantity
                    cart[food]['subtotal'] += finalprice
                else:
                    cart[food] = {'quantity': quantity, 'price': price, 'subtotal': finalprice}
                total += finalprice
            else:
                print(f"Sorry. We are currently out of {food}")
        else:
            break

def counter():
    print("-------YOUR CART-------")
    for item, details in cart.items():
        print(f"{item}: {details['quantity']} x ₹{details['price']} = ₹{details['subtotal']}")
    print("-----------------------")
    time.sleep(2)
    print(f"Your Total is : ₹{total}")
    print("-----------------------")
    while True:
        payment = input("How would you like to pay? (UPI / Card / Cash) ")
        if payment.upper() == "UPI":
            # Update the HTML file with the total amount paid
            update_html_placeholder(total)
            site_qr()
            break
        else:
            print("Sorry, we currently can't accept this payment method.")


def main():
    mall()
    counter()
    time.sleep(20)
    reset_html_placeholder(total)


if __name__ == '__main__':
    main()
