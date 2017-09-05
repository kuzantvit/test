players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
my_foods.append('pizza')
print(my_foods)
print(friend_foods)
friend_foods = my_foods
my_foods.append('copypasta')
print(my_foods)
print(friend_foods)

players = ['charles', 'martina', 'michael', 'florence', 'eli', 'Anton', 'Tanya', "Mul-ah-Darh'ad"]
print("The first 3 players are: " + str(players[:3]))
print("The first 3 players are: %s %s %s" % (players[0].title(), players[1].title(), players[2].title()))


# --------------------- TUPLES Кортежи-------------------
sweden_table = ('orange', 'french fries', 'cheeseburger', 'onion rings', 'pineapple surprise')
for dishes in sweden_table:
    print(dishes)