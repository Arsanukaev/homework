question = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
exitanswer = "Хорошо"
def ask_user():
    while True:
        try:
            print ('Как дела?')
            a = input()
            if a == "Как дела?":
                print (question["Как дела?"])
            if a == "Что делаешь?":
                print (question["Что делаешь?"])
            if a == exitanswer:
                break
        except KeyboardInterrupt:
            print ("Пока")
            break
ask_user()