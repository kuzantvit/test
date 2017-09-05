names = ["Anton", "Andrew", "Tom", "Mike", "Danger"]

sentence = "My name is " + names[2] + " I'm the Danger!"
print(sentence)
sent2 = "Hello %s and %s" % (names[2], names[3])
print(sent2)

bikes = ['Trek', 'Cube', 'GT']
bikes.append('forward')

print(bikes)
bikes.insert(0,'stells')
print(bikes)
del bikes[0]
print(bikes)
bikes.insert(0,'stells')
print(bikes)
stells_popped = bikes.pop(0)
print(bikes)
print(stells_popped)
bikes.remove('forward')
print(bikes)
bikes.append("Merida")
bikes_new = ["Desna", "Usuzu", "Cube"]

for i in bikes_new:
    bikes.append(i)
print(bikes)

sorting_bikes = sorted(bikes)
print(sorting_bikes)
print(bikes)
bikes.sort()
print(bikes)

bikes.reverse()
print(bikes)
print(len(bikes))

for bike in bikes:
    print("I can't decide which bike should i buy!\n" + "Maybe i should buy one of " + bike +"'s bike!\n\n")

