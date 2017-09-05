prompt = 'Wellcome to the restaraunt!\n How many tables do you want to order?\n'

question = input(prompt)
if int(question) > 5:
    print("More then 5?")
else:
    print("So you want ot order " + str(question) + " tables.\nYou gonna have " + str(int(question) * 4) + " guests!")

if int(question) % 2 == 0:
    print("it's odd")
else:
    print('even!')