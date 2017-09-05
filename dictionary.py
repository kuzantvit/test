programing_language ={
    'c#': 'windows',
    'swift': 'Ios',
    'java': 'Android'
}

fav_lang = input("Enter your favorite language: ")
if fav_lang.lower() == 'c#':
    print("You should work on " + str(programing_language['c#']) + '!')
elif  fav_lang.lower() == 'swift':
    print("You should work on " + str(programing_language['swift']) + '!')
else:
    print("You should work on " + str(programing_language['java']) + '!')