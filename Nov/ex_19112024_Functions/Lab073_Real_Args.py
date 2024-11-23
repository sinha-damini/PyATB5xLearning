#Pizza Lovers

# Toppings mushroom, paneer, olives, corn, pineapple, jalapeno


def make_pizza(*toppings):
    print(toppings)
    print(*toppings)
    for i in toppings:
        print(i)

pramod = make_pizza("tomato", "olives")
print('--------')
damini = make_pizza("tomato")
print('--------')
jayati  = make_pizza("pineapple", "olives","corn","paneer")
print('--------')
vinay = make_pizza("pineapple","olives","corn","paneer","mushroom","jalapeno")