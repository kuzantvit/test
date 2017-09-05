
for i in range(1, 10):

    print('go! '+ str(i))

prompt = 'What do you wnat to add to pizza?'
pizza_ingr =[]
topping = 1
#outputfile = open('W:/Python/files/pizza.txt', mode='w', encoding='Latin-1')
with open('W:/Python/files/pizza.txt', mode='w', encoding='Latin-1') as ft:

    print(prompt)
    print("\nEnter enough to stop\n")
    while topping != 'enough':
        topping = input("what else?\n")
        pizza_ingr.append(topping)
    for ingredient in pizza_ingr:
        print('Our pizza is going to have ' + str(ingredient))
        ft.write(ingredient.strip() + "\n")

    print(pizza_ingr)

    ft.close()