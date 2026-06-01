# name: joosan
# desc: input and typecasting again

# vars
number_of_pizzas = int(input("How many pizzas? "))
price_per_pizza = 14.0

total_cost = number_of_pizzas * price_per_pizza

print(f"{number_of_pizzas} pizzas will cost ${total_cost:.2f}")

# booleans: true or false
fun = bool(1)
print(type(fun))
print(fun, not fun)