question = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую"}
exitanswer = "Хорошо"
def ask_user():
    while True:
        try:
            a = input()
            for key in question:
                if a == key:
                    print (question[key])
            if a == exitanswer:
                break
        except KeyboardInterrupt:
            print ("Пока")
            break
ask_user()