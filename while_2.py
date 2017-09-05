
a_list = [i for i in range(1, 16)]
a_list.pop()
#a_list.insert(1, 'huy')
print(a_list)

while a_list:
    print('Count? ' + str(a_list))
    a_list.pop()

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
    print(pets)
print(pets)

#===================Perepis naseleniya ================
Perepis = {}
Dosie = {}
People_counter = True
while People_counter:
    name = input("Enter your name\n")
    age = input("How old are you?\n")
    politic = input("Left or right?\n")
    Perepis[name] = age
    Dosie[name] = {age, politic}
    input_end = input("More? Please answer yes or no")
    if input_end.title() == 'No':
        break
    else:
        continue
print(Perepis)
print(Dosie)